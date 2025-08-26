"""
Contains core business logic for the app.
"""

def get_message(name: str = "World") -> str:
    """
    Returns a hello message.
    
    Args:
        name (str): Name to greet.
    
    Returns:
        str: A hello message.
    """
    return f"Hello, {name}!"
