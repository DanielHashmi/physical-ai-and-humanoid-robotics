
import os
from datetime import datetime

# Define the feature name based on the current context
feature_name = "module-1-content"
phr_dir = f"history/prompts/{feature_name}/"
os.makedirs(phr_dir, exist_ok=True)

# Find the next available PHR ID
existing_phrs = [f for f in os.listdir(phr_dir) if f.endswith(".prompt.md")]
last_id = 0
for phr_file in existing_phrs:
    try:
        phr_id = int(phr_file.split('-')[0])
        if phr_id > last_id:
            last_id = phr_id
    except ValueError:
        continue
new_id = last_id + 1

# Define PHR details
title = "Generate Module 1 Chapter 1 - ROS 2 Foundations"
slug = "generate-module-1-chapter-1-ros2-foundations"
stage = "explainer" # Or 'green' if it's considered implementation
date_iso = datetime.now().strftime("%Y-%m-%d")
model = "claude-sonnet-4-5-20250929" # Assuming this is the current model
branch = "1-module-1-content" # From env or context
user_name = "User" # Placeholder
command_executed = "Generate the first chapter for Module 1 of the Physical AI & Humanoid Robotics syllabus."
labels = ["ROS 2", "Module 1", "Documentation", "Physical AI"]
links_spec = "null"
links_ticket = "null"
links_adr = "null"
links_pr = "null"
files_yaml = """  - docs/module-1/chapter-1-ros2-foundations.mdx""" # Assuming this is the output file
tests_yaml = "  - None" # No specific tests run for this content generation

prompt_text = """Please generate the first chapter for Module 1 of the Physical AI & Humanoid Robotics syllabus. Focus on introducing the core concepts for this module."""

response_text = """Generated Module 1, Chapter 1 content covering ROS 2 Nodes, Topics, DDS, and Jetson Orin Nano hardware reality, following the 5-Step Concept Loop and Docusaurus MDX format."""

# PHR content
phr_content = f'''---
id: {new_id}
title: "{title}"
stage: "{stage}"
date: {date_iso}
surface: "agent"
model: "{model}"
feature: "{feature_name}"
branch: "{branch}"
user: "{user_name}"
command: "{command_executed}"
labels: {labels}
links:
  spec: {links_spec}
  ticket: {links_ticket}
  adr: {links_adr}
  pr: {links_pr}
files:
{files_yaml}
tests:
{tests_yaml}
---

## Prompt\n\n```text\n{prompt_text.replace("'''", "\'\'\'")}\n```\n\n## Response\n\n```text\n{response_text.replace("'''", "\'\'\'")}\n```\n
'''
phr_file_path = os.path.join(phr_dir, f\"{new_id}-{slug}.{stage}.prompt.md\")\n\nwith open(phr_file_path, \"w\") as f:\n    f.write(phr_content)\n\nprint(f\"PHR created at: {phr_file_path}\")
