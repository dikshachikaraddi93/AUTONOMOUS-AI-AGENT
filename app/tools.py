from app.document import generate_document


def document_tool(user_request: str, content: str):
    """
    Tool to generate a Word document.
    """
    return generate_document(user_request, content)


def execute_tool(tool_name: str, user_request: str, content: str):
    """
    Execute the requested tool.
    """

    if tool_name == "document_generator":
        return document_tool(user_request, content)

    raise ValueError(f"Unknown tool: {tool_name}")