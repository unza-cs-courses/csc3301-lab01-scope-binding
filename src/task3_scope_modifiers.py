"""
Lab 1 Task 3: Global and Nonlocal Keywords
CSC3301 Programming Language Paradigms

Implement a counter system using closures and scope modifiers.
"""

# Global counter for total operations across all counter instances
global_counter = 0


def get_global_counter():
    """Return the global operation counter value."""
    return global_counter


def reset_global_counter():
    """Reset the global counter to 0 (for testing)."""
    global global_counter
    global_counter = 0


def create_counter(initial=0):
    """
    Create a counter with closure-based state.
    
    The counter state (count) should persist between calls using closures.
    Each operation (increment, decrement, reset) should also increment
    the global_counter to track total operations across ALL counters.
    
    Args:
        initial: Starting value for the counter (default 0)
    
    Returns:
        A dict with keys: 'increment', 'decrement', 'reset', 'get_value'
        Each value is a function that operates on the counter.
    
    Requirements:
        - Use 'nonlocal' to modify the counter's internal count
        - Use 'global' to modify the global_counter
        - increment() returns the new value after adding 1
        - decrement() returns the new value after subtracting 1
        - reset() returns the initial value after resetting
        - get_value() returns current value (does NOT increment global_counter)
    
    Example usage:
        c1 = create_counter(10)
        c1['increment']()  # Returns 11, global_counter becomes 1
        c1['increment']()  # Returns 12, global_counter becomes 2
        c2 = create_counter(0)
        c2['increment']()  # Returns 1, global_counter becomes 3
        c1['get_value']()  # Returns 12 (global_counter unchanged)
    """
    # YOUR CODE HERE
    # Remember to use 'nonlocal' for the closure variable
    # and 'global' for the global_counter
    pass


# ============================================================
# Test code
# ============================================================

if __name__ == "__main__":
    reset_global_counter()
    
    print("Testing counter system:\n")
    
    # Create first counter starting at 10
    c1 = create_counter(10)
    
    if c1 is None:
        print("create_counter not implemented yet")
    else:
        print(f"c1 created with initial=10")
        print(f"c1 increment: {c1['increment']()}")  # Expected: 11
        print(f"c1 increment: {c1['increment']()}")  # Expected: 12
        print(f"Global ops: {get_global_counter()}")  # Expected: 2
        
        # Create second counter starting at 0
        c2 = create_counter(0)
        print(f"\nc2 created with initial=0")
        print(f"c2 increment: {c2['increment']()}")  # Expected: 1
        print(f"Global ops: {get_global_counter()}")  # Expected: 3
        
        # Check c1 still has its state
        print(f"\nc1 value: {c1['get_value']()}")  # Expected: 12
        print(f"c1 decrement: {c1['decrement']()}")  # Expected: 11
        print(f"c1 reset: {c1['reset']()}")  # Expected: 10
        print(f"Global ops: {get_global_counter()}")  # Expected: 5
