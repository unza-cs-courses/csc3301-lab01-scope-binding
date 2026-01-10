"""
Lab 1 Task 1: LEGB Scope Investigation
CSC3301 Programming Language Paradigms

Complete the function to demonstrate all four LEGB scope levels.
Your output must match the expected format exactly.
"""

# Global scope variable
x = "GLOBAL_X"


def investigate_legb():
    """
    Create a demonstration of all four LEGB scopes.
    
    Expected output (exact):
    Built-in scope: <class 'int'>
    Global scope: GLOBAL_X
    Enclosing scope: ENCLOSING_X
    Local scope: LOCAL_X
    
    Hints:
    - Built-in: 'int', 'str', 'print' are built-in names
    - Global: Variables defined at module level
    - Enclosing: Variables in outer function (for nested functions)
    - Local: Variables defined inside the current function
    """
    # YOUR CODE HERE
    # Demonstrate all four scope levels
    pass


if __name__ == "__main__":
    investigate_legb()
