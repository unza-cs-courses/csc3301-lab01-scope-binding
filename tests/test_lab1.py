"""
Lab 1 Test Suite
CSC3301 Programming Language Paradigms

These tests will be run by the autograder.
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
        # Capture output
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert output is not None
    
    def test_builtin_scope_output(self):
        """Should print Built-in scope line."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert "Built-in scope:" in output
        assert "<class 'int'>" in output
    
    def test_global_scope_output(self):
        """Should print Global scope line."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert "Global scope: GLOBAL_X" in output
    
    def test_enclosing_scope_output(self):
        """Should print Enclosing scope line."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert "Enclosing scope: ENCLOSING_X" in output
    
    def test_local_scope_output(self):
        """Should print Local scope line."""
        from src.task1_legb import investigate_legb
        f = io.StringIO()
        with redirect_stdout(f):
            investigate_legb()
        output = f.getvalue()
        assert "Local scope: LOCAL_X" in output


class TestTask2Closures:
    """Tests for Task 2: Closure Binding Behavior."""
    
    def test_buggy_version_demonstrates_bug(self):
        """Buggy version should show the late binding bug."""
        from src.task2_closures import create_multipliers_buggy
        mults = create_multipliers_buggy()
        results = [m(10) for m in mults]
        # All should be 40 due to the bug
        assert results == [40, 40, 40, 40, 40], "Buggy version should return all 40s"
    
    def test_fixed_a_returns_correct_results(self):
        """Fixed A should return [0, 10, 20, 30, 40]."""
        from src.task2_closures import create_multipliers_fixed_a
        mults = create_multipliers_fixed_a()
        assert mults is not None, "create_multipliers_fixed_a not implemented"
        results = [m(10) for m in mults]
        assert results == [0, 10, 20, 30, 40]
    
    def test_fixed_b_returns_correct_results(self):
        """Fixed B should return [0, 10, 20, 30, 40]."""
        from src.task2_closures import create_multipliers_fixed_b
        mults = create_multipliers_fixed_b()
        assert mults is not None, "create_multipliers_fixed_b not implemented"
        results = [m(10) for m in mults]
        assert results == [0, 10, 20, 30, 40]
    
    def test_fixed_a_uses_default_param(self):
        """Fixed A should use default parameter technique."""
        from src.task2_closures import create_multipliers_fixed_a
        import inspect
        source = inspect.getsource(create_multipliers_fixed_a)
        # Should have a default parameter in the lambda
        assert "=" in source and "lambda" in source
    
    def test_fixed_b_uses_partial(self):
        """Fixed B should use functools.partial."""
        from src.task2_closures import create_multipliers_fixed_b
        import inspect
        source = inspect.getsource(create_multipliers_fixed_b)
        assert "partial" in source


class TestTask3ScopeModifiers:
    """Tests for Task 3: Global and Nonlocal Keywords."""
    
    def test_create_counter_returns_dict(self):
        """create_counter should return a dict with required keys."""
        from src.task3_scope_modifiers import create_counter
        c = create_counter(0)
        assert c is not None, "create_counter not implemented"
        assert isinstance(c, dict)
        assert 'increment' in c
        assert 'decrement' in c
        assert 'reset' in c
        assert 'get_value' in c
    
    def test_increment_works(self):
        """increment() should add 1 and return new value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        c = create_counter(10)
        assert c['increment']() == 11
        assert c['increment']() == 12
    
    def test_decrement_works(self):
        """decrement() should subtract 1 and return new value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        c = create_counter(10)
        assert c['decrement']() == 9
        assert c['decrement']() == 8
    
    def test_reset_works(self):
        """reset() should return to initial value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        c = create_counter(10)
        c['increment']()
        c['increment']()
        assert c['reset']() == 10
    
    def test_get_value_works(self):
        """get_value() should return current value."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        c = create_counter(10)
        assert c['get_value']() == 10
        c['increment']()
        assert c['get_value']() == 11
    
    def test_global_counter_increments(self):
        """Global counter should track operations across counters."""
        from src.task3_scope_modifiers import create_counter, get_global_counter, reset_global_counter
        reset_global_counter()
        
        c1 = create_counter(10)
        c1['increment']()  # global = 1
        c1['increment']()  # global = 2
        
        c2 = create_counter(0)
        c2['increment']()  # global = 3
        
        assert get_global_counter() == 3
    
    def test_counters_are_independent(self):
        """Multiple counters should have independent state."""
        from src.task3_scope_modifiers import create_counter, reset_global_counter
        reset_global_counter()
        
        c1 = create_counter(10)
        c2 = create_counter(100)
        
        c1['increment']()
        c1['increment']()
        
        assert c1['get_value']() == 12
        assert c2['get_value']() == 100


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
        assert 'global_refs' in result
        assert 'closure_values' in result
    
    def test_analyze_scope_finds_local_vars(self):
        """Should find local variables including parameters."""
        from src.task4_introspection import analyze_scope
        
        def test_func(a, b):
            c = 10
            return a + b + c
        
        result = analyze_scope(test_func)
        assert 'a' in result['local_vars']
        assert 'b' in result['local_vars']
        assert 'c' in result['local_vars']
    
    def test_analyze_scope_finds_free_vars(self):
        """Should find free variables from enclosing scope."""
        from src.task4_introspection import analyze_scope
        
        def outer():
            x = 10
            def inner():
                return x
            return inner
        
        closure_func = outer()
        result = analyze_scope(closure_func)
        assert 'x' in result['free_vars']
    
    def test_analyze_scope_gets_closure_values(self):
        """Should get actual values from closure cells."""
        from src.task4_introspection import analyze_scope
        
        def outer():
            secret = 42
            def inner():
                return secret
            return inner
        
        closure_func = outer()
        result = analyze_scope(closure_func)
        assert result['closure_values'].get('secret') == 42
    
    def test_find_shadowed_builtins_works(self):
        """Should find shadowed built-in names."""
        from src.task4_introspection import find_shadowed_builtins
        
        # Create a test module
        test_module = types.ModuleType('test')
        test_module.list = "shadowed!"
        test_module.print = lambda x: None
        test_module.my_var = 123  # Not shadowing
        
        result = find_shadowed_builtins(test_module)
        assert result is not None, "find_shadowed_builtins not implemented"
        assert 'list' in result
        assert 'print' in result
        assert 'my_var' not in result
    
    def test_find_shadowed_builtins_returns_sorted(self):
        """Result should be sorted."""
        from src.task4_introspection import find_shadowed_builtins
        
        test_module = types.ModuleType('test')
        test_module.zip = "z"
        test_module.abs = "a"
        test_module.len = "l"
        
        result = find_shadowed_builtins(test_module)
        assert result == sorted(result)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
