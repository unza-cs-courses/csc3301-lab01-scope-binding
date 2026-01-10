"""
Lab 1 Task 4: Namespace Introspection
CSC3301 Programming Language Paradigms

Implement functions to analyze scope-related attributes of functions and modules.
"""
import builtins


def analyze_scope(func):
    """
    Analyze the scope-related attributes of a function.
    
    Args:
        func: A Python function to analyze
    
    Returns:
        dict with keys:
        - 'local_vars': List of local variable names (from func.__code__.co_varnames)
        - 'free_vars': List of free variable names (from func.__code__.co_freevars)
        - 'global_refs': List of global names referenced (from func.__code__.co_names)
        - 'closure_values': Dict mapping free var names to their values (if closure exists)
    
    Hints:
        - func.__code__ gives you the code object with metadata
        - func.__code__.co_varnames: tuple of local variable names
        - func.__code__.co_freevars: tuple of free variable names (from enclosing scope)
        - func.__code__.co_names: tuple of names used by the bytecode
        - func.__closure__: None if no closure, else tuple of cell objects
        - cell.cell_contents: gets the value stored in a cell
    
    Example:
        x = 10
        def outer():
            y = 20
            def inner(a, b):
                return a + b + x + y
            return inner
        
        result = analyze_scope(outer())
        # result['local_vars'] should include 'a', 'b'
        # result['free_vars'] should include 'y'
        # result['closure_values'] should be {'y': 20}
    """
    # YOUR CODE HERE
    pass


def find_shadowed_builtins(module):
    """
    Find built-in names that have been shadowed in the given module.
    
    A name is "shadowed" if the module defines something with the same
    name as a Python built-in (like 'list', 'str', 'print', etc.)
    
    Args:
        module: A Python module to scan
    
    Returns:
        list: Sorted list of built-in names that have been redefined in the module
    
    Hints:
        - dir(builtins) gives all built-in names
        - dir(module) gives all names defined in the module
        - getattr(module, name) gets the value of a name in the module
        - getattr(builtins, name) gets the built-in value
        - Compare with 'is' or 'is not' to check if they're the same object
    
    Example:
        # If a module defines: list = [1, 2, 3]
        # Then 'list' would be in the returned list
    """
    # YOUR CODE HERE
    pass


# ============================================================
# Test code
# ============================================================

if __name__ == "__main__":
    print("Testing analyze_scope:\n")
    
    # Create a test function with closure
    x = 10  # Global
    
    def outer():
        y = 20  # Enclosing
        z = 30  # Enclosing
        
        def inner(a, b):  # Parameters are local
            c = a + b  # Local
            return c + x + y  # Uses global x and enclosing y (not z)
        
        return inner
    
    closure_func = outer()
    result = analyze_scope(closure_func)
    
    if result is None:
        print("analyze_scope not implemented yet")
    else:
        print("Scope Analysis of 'inner' function:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    
    print("\n" + "="*50)
    print("\nTesting find_shadowed_builtins:\n")
    
    # Create a mock module for testing
    import types
    test_module = types.ModuleType('test_module')
    test_module.list = "I shadowed the list builtin!"
    test_module.print = lambda x: None
    test_module.my_var = 42  # This is not shadowing anything
    test_module.str = str  # Same object, not actually shadowing
    
    shadowed = find_shadowed_builtins(test_module)
    
    if shadowed is None:
        print("find_shadowed_builtins not implemented yet")
    else:
        print(f"Shadowed builtins: {shadowed}")
        # Expected: ['list', 'print'] (str is the same object, so not shadowed)
