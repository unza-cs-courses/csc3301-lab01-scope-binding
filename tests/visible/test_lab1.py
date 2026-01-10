"""
Lab 1 Visible Test Suite
CSC3301 Programming Language Paradigms

These tests are visible to students and run on every push.
Tests use variant configuration for personalized values.

Note: Hidden tests with additional edge cases run after the deadline.
"""
import pytest
import sys
import io
from contextlib import redirect_stdout
import types


class TestTask1LEGB:
    """Tests for Task 1: LEGB Scope Investigation."""

    def test_investigate_legb_runs(self):
        """Function should run without errors."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert output is not None

    def test_builtin_scope_output(self, scope_values):
        """Should print Built-in scope line."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert "Built-in scope:" in output
        assert scope_values["builtin"] in output

    def test_global_scope_output(self, scope_values):
        """Should print Global scope line with your variant value."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        expected = f"Global scope: {scope_values['global']}"
        assert expected in output, f"Expected '{expected}' in output"

    def test_enclosing_scope_output(self, scope_values):
        """Should print Enclosing scope line with your variant value."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        expected = f"Enclosing scope: {scope_values['enclosing']}"
        assert expected in output, f"Expected '{expected}' in output"

    def test_local_scope_output(self, scope_values):
        """Should print Local scope line with your variant value."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        expected = f"Local scope: {scope_values['local']}"
        assert expected in output, f"Expected '{expected}' in output"


class TestTask2Closures:
    """Tests for Task 2: Closure Binding Behavior."""

    def test_buggy_version_demonstrates_bug(self, closure_tests):
        """Buggy version should show the late binding bug."""
        from src.task2_closures import create_multipliers_buggy
        mults = create_multipliers_buggy()
        test_input = closure_tests["multiplier_input"]
        results = [m(test_input) for m in mults]
        # All should be 4 * input due to the bug (last value of i is 4)
        expected_buggy = [4 * test_input] * 5
        assert results == expected_buggy, f"Buggy version should return all {4 * test_input}s"

    def test_fixed_a_returns_correct_results(self, closure_tests):
        """Fixed A should return correct multiplied results."""
        from src.task2_closures import create_multipliers_fixed_a
        mults = create_multipliers_fixed_a()
        assert mults is not None, "create_multipliers_fixed_a not implemented"
        test_input = closure_tests["multiplier_input"]
        results = [m(test_input) for m in mults]
        assert results == closure_tests["expected_results"]

    def test_fixed_b_returns_correct_results(self, closure_tests):
        """Fixed B should return correct multiplied results."""
        from src.task2_closures import create_multipliers_fixed_b
        mults = create_multipliers_fixed_b()
        assert mults is not None, "create_multipliers_fixed_b not implemented"
        test_input = closure_tests["multiplier_input"]
        results = [m(test_input) for m in mults]
        assert results == closure_tests["expected_results"]

    def test_fixed_a_uses_default_param(self):
        """Fixed A should use default parameter technique."""
        from src.task2_closures import create_multipliers_fixed_a
        import inspect
        source = inspect.getsource(create_multipliers_fixed_a)
        assert "=" in source and "lambda" in source

    def test_fixed_b_uses_partial(self):
        """Fixed B should use functools.partial."""
        from src.task2_closures import create_multipliers_fixed_b
        import inspect
        source = inspect.getsource(create_multipliers_fixed_b)
        assert "partial" in source


class TestTask3ScopeModifiers:
    """Tests for Task 3: Global and Nonlocal Keywords."""

    def test_create_counter_returns_dict(self, counter_tests):
        """create_counter should return a dict with required keys."""
        from src.task3_scope_modifiers import create_counter
        initial = counter_tests["initial_values"][0]
        c = create_counter(initial)
        assert c is not None, "create_counter not implemented"
        assert isinstance(c, dict)
        assert 'increment' in c
        assert 'decrement' in c
        assert 'reset' in c
        assert 'get_value' in c

    def test_increment_works(self, counter_tests):
        """increment() should add 1 and return new value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        initial = counter_tests["initial_values"][0]
        expected = counter_tests["expected_increments"][0]
        c = create_counter(initial)
        result = c['increment']()
        assert result == expected, f"Expected {expected}, got {result}"

    def test_decrement_works(self, counter_tests):
        """decrement() should subtract 1 and return new value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        initial = counter_tests["initial_values"][0]
        expected = counter_tests["expected_decrements"][0]
        c = create_counter(initial)
        result = c['decrement']()
        assert result == expected, f"Expected {expected}, got {result}"

    def test_reset_works(self, counter_tests):
        """reset() should return to initial value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        initial = counter_tests["initial_values"][0]
        c = create_counter(initial)
        c['increment']()
        c['increment']()
        result = c['reset']()
        assert result == initial, f"Expected {initial}, got {result}"

    def test_get_value_works(self, counter_tests):
        """get_value() should return current value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        initial = counter_tests["initial_values"][0]
        c = create_counter(initial)
        assert c['get_value']() == initial
        c['increment']()
        assert c['get_value']() == initial + 1


class TestTask4Introspection:
    """Tests for Task 4: Namespace Introspection."""

    def test_analyze_scope_returns_dict(self):
        """analyze_scope should return a dict with required keys."""
        from src.task4_introspection import analyze_scope

        def simple_func(a, b):
            c = a + b
            return c

        result = analyze_scope(simple_func)
        assert result is not None, "analyze_scope not implemented"
        assert isinstance(result, dict)
        assert 'local_vars' in result
        assert 'free_vars' in result

    def test_analyze_scope_finds_local_vars(self):
        """Should find local variables including parameters."""
        from src.task4_introspection import analyze_scope

        def test_func(a, b):
            c = 10
            return a + b + c

        result = analyze_scope(test_func)
        assert 'a' in result['local_vars']
        assert 'b' in result['local_vars']

    def test_find_shadowed_builtins_works(self):
        """Should find shadowed built-in names."""
        from src.task4_introspection import find_shadowed_builtins

        test_module = types.ModuleType('test')
        test_module.list = "shadowed!"
        test_module.print = lambda x: None
        test_module.my_var = 123

        result = find_shadowed_builtins(test_module)
        assert result is not None, "find_shadowed_builtins not implemented"
        assert 'list' in result
        assert 'print' in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
