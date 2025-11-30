"""
OpenAI Agents SDK-based RAG chatbot service for the Physical AI textbook.
Uses OpenAI Agents SDK with Gemini as the LLM provider via OpenAI-compatible endpoint.
Implements proper RAG by pre-fetching context from vector database.
"""
import json
from typing import List, Dict, Optional, AsyncGenerator, Annotated
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled
from src.services.embedding_service import EmbeddingService
from src.services.vector_store_service import VectorStoreService
from src.services.db_service import db_service
from src.core.config import settings

# Disable tracing for cleaner output
set_tracing_disabled(True)

# Course navigation map for redirect functionality
COURSE_NAVIGATION = {
    "intro": {"path": "/docs", "title": "Introduction"},
    "introduction": {"path": "/docs", "title": "Introduction"},
    "home": {"path": "/docs", "title": "Introduction"},
    "module 1": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "module1": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "ros": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "ros 2": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "ros2": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "physical ai": {"path": "/docs/module-01/intro-physical-ai", "title": "Introduction to Physical AI"},
    "module 2": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "module2": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "gazebo": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "unity": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "simulation": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "digital twin": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "module 3": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "module3": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "isaac": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "nvidia": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "nvidia isaac": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "module 4": {"path": "/docs/module4/week13-conversational-robotics", "title": "Module 4: Vision-Language-Action"},
    "module4": {"path": "/docs/module4/week13-conversational-robotics", "title": "Module 4: Vision-Language-Action"},
    "vla": {"path": "/docs/module4/week13-conversational-robotics", "title": "Module 4: Vision-Language-Action"},
    "conversational": {"path": "/docs/module4/week13-conversational-robotics", "title": "Module 4: Conversational Robotics"},
    "humanoid": {"path": "/docs/module4/week11-humanoid-dev", "title": "Humanoid Development"},
    "1": {"path": "/docs/module-01/intro-physical-ai", "title": "Module 1: ROS 2 Fundamentals"},
    "2": {"path": "/docs/module2/week6-gazebo", "title": "Module 2: Gazebo & Unity"},
    "3": {"path": "/docs/module3/week8-isaac", "title": "Module 3: NVIDIA Isaac"},
    "4": {"path": "/docs/module4/week13-conversational-robotics", "title": "Module 4: Vision-Language-Action"},
}


# Define the navigation tool as a function tool
@function_tool
def navigate_to_page(
    destination: Annotated[str, "The page or module to navigate to. Can be: 'intro', 'module 1', 'module 2', 'module 3', 'module 4', 'ros', 'gazebo', 'isaac', 'vla', 'humanoid', or a module number like '1', '2', '3', '4'"]
) -> str:
    """
    Navigate the user to a specific page in the Physical AI textbook.
    Use this tool when the user asks to go to, navigate to, redirect to, or open a specific page or module.
    
    Available destinations:
    - 'intro' or 'introduction': Course introduction
    - 'module 1', '1', 'ros', 'ros 2', 'physical ai': Module 1 - ROS 2 Fundamentals
    - 'module 2', '2', 'gazebo', 'unity', 'simulation': Module 2 - Gazebo & Unity
    - 'module 3', '3', 'isaac', 'nvidia': Module 3 - NVIDIA Isaac
    - 'module 4', '4', 'vla', 'conversational', 'humanoid': Module 4 - Vision-Language-Action
    """
    destination_lower = destination.lower().strip()
    
    # Try to find matching navigation
    if destination_lower in COURSE_NAVIGATION:
        nav_info = COURSE_NAVIGATION[destination_lower]
        return json.dumps({
            "action": "redirect",
            "path": nav_info["path"],
            "title": nav_info["title"],
            "message": f"Navigating to {nav_info['title']}"
        })
    
    # Try partial matching
    for key, nav_info in COURSE_NAVIGATION.items():
        if key in destination_lower or destination_lower in key:
            return json.dumps({
                "action": "redirect",
                "path": nav_info["path"],
                "title": nav_info["title"],
                "message": f"Navigating to {nav_info['title']}"
            })
    
    # No match found
    available = "intro, module 1, module 2, module 3, module 4, ros, gazebo, isaac, vla, humanoid"
    return json.dumps({
        "action": "error",
        "message": f"Could not find page '{destination}'. Available destinations: {available}"
    })


@function_tool
def list_available_pages() -> str:
    """
    List all available pages and modules in the Physical AI textbook.
    Use this tool when the user asks what pages are available or wants to see the course structure.
    """
    pages = [
        {"title": "Introduction", "path": "/docs", "description": "Course overview and getting started"},
        {"title": "Module 1: ROS 2 Fundamentals", "path": "/docs/module-01/intro-physical-ai", "description": "The Robotic Nervous System - nodes, topics, services, URDF"},
        {"title": "Module 2: Gazebo & Unity", "path": "/docs/module2/week6-gazebo", "description": "The Digital Twin - physics simulation and environment building"},
        {"title": "Module 3: NVIDIA Isaac", "path": "/docs/module3/week8-isaac", "description": "The AI-Robot Brain - advanced perception and training"},
        {"title": "Module 4: Vision-Language-Action", "path": "/docs/module4/week13-conversational-robotics", "description": "LLMs meet Robotics - conversational AI for robots"},
    ]
    return json.dumps({"pages": pages})


class TextbookAgent:
    """Agent for answering questions about the Physical AI textbook using OpenAI Agents SDK with Gemini."""
    
    def __init__(self):
        # Use Gemini's OpenAI-compatible endpoint
        self.client = AsyncOpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url=settings.GEMINI_BASE_URL
        )
        # Create OpenAI Agents SDK model with Gemini backend
        self.model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=self.client
        )
        self.embedding_service = EmbeddingService()
        self.vector_store_service = VectorStoreService()
    
    def _search_textbook(self, query: str) -> str:
        """Search the textbook for relevant content."""
        try:
            embedding = self.embedding_service.get_embedding(query)
            results = self.vector_store_service.search_vectors(embedding, limit=8)
            
            if not results:
                return "No relevant content found in the textbook."
            
            context = "TEXTBOOK CONTENT:\n\n"
            for i, result in enumerate(results, 1):
                # Clean up source file path for display
                source = result['source_file']
                if 'physical-ai-textbook' in source:
                    source = source.split('physical-ai-textbook')[-1].replace('\\', '/')
                context += f"--- Source {i}: {source} (Relevance: {result['score']:.2f}) ---\n"
                context += f"{result['text']}\n\n"
            
            return context
        except Exception as e:
            return f"Error searching textbook: {str(e)}"
    
    def _get_user_context(self, user_id: Optional[str]) -> str:
        """Get user's background for personalization."""
        if not user_id:
            return ""
        
        try:
            user = db_service.get_user_by_id(user_id)
            if not user or not user.get('background'):
                return ""
            
            background = user['background']
            context = f"\nUSER CONTEXT:\n"
            context += f"- Name: {user.get('name', 'Unknown')}\n"
            context += f"- Programming Experience: {background.get('programming_experience', 'unknown')}\n"
            context += f"- Robotics Experience: {background.get('robotics_experience', 'unknown')}\n"
            context += f"- Preferred Languages: {', '.join(background.get('preferred_languages', []))}\n"
            context += f"- Hardware Access: {', '.join(background.get('hardware_access', []))}\n"
            
            return context
        except Exception as e:
            return ""
    
    def _get_system_prompt(self, textbook_context: str, user_context: str, current_page: Optional[str]) -> str:
        """Build dynamic system prompt with retrieved context."""
        prompt = """You are an expert assistant for the Physical AI & Humanoid Robotics textbook.
You have access to tools that allow you to navigate users to different pages in the textbook.

Your role is to help students learn about:
- Module 1: ROS 2 (Robot Operating System) - The Robotic Nervous System
- Module 2: Gazebo & Unity - The Digital Twin (physics simulation and environment building)
- Module 3: NVIDIA Isaac - The AI-Robot Brain (advanced perception and training)
- Module 4: Vision-Language-Action (VLA) - The convergence of LLMs and Robotics

IMPORTANT - NAVIGATION TOOL USAGE:
When a user asks to be redirected, navigate, go to, or open a specific page or module, you MUST use the navigate_to_page tool.
Examples of when to use the navigation tool:
- "redirect me to module 3"
- "take me to the ROS section"
- "go to the introduction"
- "navigate to gazebo"
- "open module 2"
- "show me the isaac page"

When you use the navigate_to_page tool, include the tool's response in your answer so the frontend can process the redirect.

RESPONSE LENGTH GUIDELINES:
- By DEFAULT, provide CONCISE, focused answers (2-4 paragraphs)
- Only provide DETAILED, comprehensive answers when the user explicitly asks for:
  - "in depth", "detailed", "comprehensive", "explain thoroughly", "tell me more", "elaborate"
- For simple questions, give direct answers without excessive elaboration

CRITICAL INSTRUCTIONS:
1. Base your answers primarily on the TEXTBOOK CONTENT provided below
2. Use markdown formatting for readability (headers, bullets, code blocks)
3. Reference specific sources when relevant
4. Include code examples only when directly relevant or requested
5. Tailor explanations to the user's experience level when user context is available
6. ALWAYS use the navigate_to_page tool when users ask to go to a specific page

RESPONSE FORMAT:
- Use ## headers for sections (only for detailed responses)
- Use bullet points for lists
- Use `code` for inline code and ```language for code blocks
- Keep responses scannable and well-organized

"""
        if current_page:
            prompt += f"\nUSER IS CURRENTLY VIEWING: {current_page}\n"
        
        if user_context:
            prompt += f"\n{user_context}\n"
        
        prompt += f"\n{textbook_context}\n"
        
        prompt += """
When answering:
- Reference specific sources and modules from the textbook content above
- Adapt complexity based on user's background if available
- Provide detailed, helpful explanations
- Include practical examples and code snippets when relevant
- Use the navigate_to_page tool when users want to go to a specific page"""
        
        return prompt
    
    async def chat_stream(
        self, 
        user_message: str, 
        history: List[Dict[str, str]], 
        selected_text: Optional[str] = None,
        user_id: Optional[str] = None,
        current_page: Optional[str] = None
    ) -> AsyncGenerator[str, None]:
        """
        Stream a response from the agent using OpenAI Agents SDK with proper RAG.
        
        Args:
            user_message: The user's question
            history: Previous conversation turns
            selected_text: Optional text selected by user from documentation
            user_id: User ID for personalization
            current_page: Current page URL for context
        """
        # Build search query
        search_query = user_message
        if selected_text:
            search_query = f"{user_message} {selected_text[:500]}"
        
        # Pre-fetch context from vector database
        textbook_context = self._search_textbook(search_query)
        user_context = self._get_user_context(user_id)
        
        # Build dynamic system prompt with context
        system_prompt = self._get_system_prompt(textbook_context, user_context, current_page)
        
        # Create agent with dynamic instructions and tools
        agent = Agent(
            name="Physical AI Textbook Assistant",
            instructions=system_prompt,
            model=self.model,
            tools=[navigate_to_page, list_available_pages],  # Add navigation tools
        )
        
        # Build user message
        enhanced_message = user_message
        if selected_text:
            enhanced_message += f"\n\n[User selected this text from the page: {selected_text}]"
        
        full_response = []
        
        try:
            # Use OpenAI Agents SDK Runner to execute the agent
            result = await Runner.run(
                agent,
                input=enhanced_message
            )
            
            # Get the final output
            response_text = result.final_output
            
            # Check if any tool was called and include redirect info
            for item in result.new_items:
                if hasattr(item, 'output') and item.output:
                    try:
                        tool_output = json.loads(item.output)
                        if tool_output.get('action') == 'redirect':
                            # Append redirect marker to response
                            response_text += f"\n\n[[REDIRECT:{tool_output['path']}]]"
                            break
                    except (json.JSONDecodeError, TypeError):
                        pass
            
            full_response.append(response_text)
            
            # Yield the response
            yield response_text
            
            # Log the interaction
            db_service.log_chat_interaction(
                user_message=user_message,
                ai_response="".join(full_response),
                source_documents=[]
            )
            
        except Exception as e:
            error_msg = f"\n\n**Error:** {str(e)}. Please try again."
            yield error_msg
            db_service.log_chat_interaction(
                user_message=user_message,
                ai_response=f"Error: {str(e)}",
                source_documents=[]
            )


# Singleton instance
textbook_agent = TextbookAgent()
