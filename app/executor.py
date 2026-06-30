from app.llm import ask_gemini
from app.tools import execute_tool


def execute_plan(user_request: str, tasks: list):
    """
    Execute the generated plan and create the final document.
    """

    prompt = f"""
    User Request:
    {user_request}

    Planned Tasks:
    {tasks}

    Generate a professional business document.

    Include:
    - Title
    - Introduction
    - Main Content
    - Conclusion
    """

    content = ask_gemini(prompt)

    document_path = execute_tool(
        "document_generator",
        user_request,
        content
    )

    return {
        "status": "success",
        "tasks": tasks,
        "document": document_path,
        "response": content
    }