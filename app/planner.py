from app.llm import ask_gemini


def create_plan(user_request: str):
    """
    Generate an execution plan (TODO list) for the user's request.
    """

    prompt = f"""
    You are an autonomous AI agent.

    User Request:
    {user_request}

    Your job is to create a clear step-by-step execution plan.

    Return ONLY a numbered list of tasks.

    Example:

    1. Understand the request
    2. Create document outline
    3. Generate content
    4. Review content
    5. Generate Word document
    """

    response = ask_gemini(prompt)

    tasks = []

    for line in response.split("\n"):
        line = line.strip()

        if line and line[0].isdigit():
            task = line.split(".", 1)[-1].strip()
            tasks.append(task)

    return tasks