<!-- Sync Impact Report:
Version change: None → 1.0.0
List of modified principles: All principles are new.
Added sections: Hackathon Constraints
Removed sections: [SECTION_3_NAME], [SECTION_3_CONTENT]
Templates requiring updates:
- ./.specify/templates/plan-template.md: ⚠ pending
- ./.specify/templates/spec-template.md: ⚠ pending
- ./.specify/templates/tasks-template.md: ⚠ pending
- ./.specify/templates/commands/*.md: ⚠ pending
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Textbook Constitution

## Core Principles

### I. Spec-First, AI-Augmented Development
All development, including code and content creation, must begin with a clear, approved specification. This methodology ensures alignment with project goals and leverages AI for augmentation, not as a replacement for structured planning.

### II. Non-Negotiable Technical Stack
The project adheres strictly to the defined technical stack: Docusaurus (React, TypeScript, MDX) for frontend/content, Python 3.12+ with FastAPI for backend/AI, Neon Serverless Postgres and Qdrant for databases, Better-Auth for authentication, and Claude Code CLI + Spec-Kit Plus for orchestration. No deviations are permitted without explicit architectural review and ADR.

### III. Rigorous Quality Standards
*   **Python Code:** Strict type hints (`mypy` compliant), Google-style docstrings, and comprehensive `pytest` coverage for all backend logic.
*   **Frontend Code:** TypeScript strict mode and a mandate for reusable components, especially for common UI elements like "Translate" and "Personalize" buttons.
*   **Content (Markdown):** Each chapter must include "Learning Outcomes" at the beginning and "Assessments" at the end, strictly following the "Physical AI & Humanoid Robotics" syllabus modules.

### IV. Structured Architecture & Methodology
*   **ADRs:** Architectural Decision Records are mandatory for critical components: RAG retrieval logic, Urdu translation pipeline design, and User Personalization data schema.
*   **Checkpoints:** Work is broken down into atomic tasks, each with an estimated duration of less than 2 hours.
*   **Validation:** No code is committed without passing all associated tests. No content is committed without passing a "Curriculum Alignment" check.

### V. Hackathon-Driven Execution
Prioritize rapid development and delivery while maintaining mandatory stability. The platform must fully support the four bonus features: RAG Chatbot, Auth, Personalization, and Urdu Translation.

## Hackathon Constraints

Speed is key, but stability is mandatory.
The platform must support the 4 bonus features: RAG Chatbot, Auth, Personalization, and Urdu Translation.

## Governance

This constitution serves as the immutable standard for the "Physical AI & Humanoid Robotics Textbook" project. All changes, including amendments to principles or architectural rules, require a formal review process documented via an Architectural Decision Record (ADR) that outlines options considered, trade-offs, and rationale. Compliance with all principles must be verified in every Pull Request and code review. Any proposed deviations from the defined technical stack or quality standards must be rigorously justified and approved by the Lead Architect.

**Version**: 1.0.0 | **Ratified**: 2025-11-28 | **Last Amended**: 2025-11-28
