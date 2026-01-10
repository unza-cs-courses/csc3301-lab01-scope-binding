"""
Lab 1 Task 2: Closure Binding Behavior
CSC3301 Programming Language Paradigms

Fix the late binding bug in create_multipliers using two different approaches.
"""
import functools


def create_multipliers_buggy():
    """
    This version has a bug - all functions return the same result.
    
    YOUR TASK: Add comments below explaining WHY this bug occurs.
    The key concept is "late binding" - explain what this means.
    """
    # BUG EXPLANATION:
    # [Add your explanation here - at least 3-4 sentences]
    # 
    # 
    # 
    multipliers = []
    for i in range(5):
        multipliers.append(lambda x: x * i)
    return multipliers


def create_multipliers_fixed_a():
    """
    Fix using default parameter binding.
    
    Hint: Default parameters are evaluated at function DEFINITION time,
    not at function CALL time. This captures the current value of the
    loop variable.
    
    Expected: create_multipliers_fixed_a()[2](10) returns 20
    """
    # YOUR CODE HERE
    pass


def create_multipliers_fixed_b():
    """
    Fix using functools.partial.
    
    Hint: functools.partial creates a new function with some arguments
    pre-filled. This binds the value immediately.
    
    Expected: create_multipliers_fixed_b()[3](10) returns 30
    """
    # YOUR CODE HERE
    pass


# ============================================================
# Test code - DO NOT MODIFY
# ============================================================

def test_multipliers(create_func, name):
    """Test a multiplier factory function."""
    mults = create_func()
    if mults is None:
        print(f"{name}: Not implemented - SKIP")
        return False
    
    results = [m(10) for m in mults]
    expected = [0, 10, 20, 30, 40]
    status = "PASS" if results == expected else "FAIL"
    print(f"{name}: {results} - {status}")
    return results == expected


if __name__ == "__main__":
    print("Testing multiplier functions:\n")
    test_multipliers(create_multipliers_buggy, "Buggy (expected to fail)")
    test_multipliers(create_multipliers_fixed_a, "Fixed A (default param)")
    test_multipliers(create_multipliers_fixed_b, "Fixed B (partial)")
