# Lab 1: Scope, Binding, and Namespaces

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Estimated Time:** 1–1.5 hours
**Points:** 100

---

## Your Unique Variant

This assignment has been personalized for you. Your specific test values are:

| Parameter | Your Value |
|-----------|------------|
| Global scope value | `{{GLOBAL_VALUE}}` |
| Enclosing scope value | `{{ENCLOSING_VALUE}}` |
| Local scope value | `{{LOCAL_VALUE}}` |
| Counter initial value | `{{COUNTER_INITIAL}}` |
| Multiplier test input | `{{MULTIPLIER_INPUT}}` |

**Important:** Your code must use these exact values to pass the tests.

---

## Tasks

### Task 1: LEGB Scope Investigation (25 points)

Open `src/task1_legb.py` and complete the `investigate_legb()` function.

**Your expected output:**
```
Built-in scope: <class 'int'>
Global scope: {{GLOBAL_VALUE}}
Enclosing scope: {{ENCLOSING_VALUE}}
Local scope: {{LOCAL_VALUE}}
```

### Task 2: Closure Binding Behavior (25 points)

Open `src/task2_closures.py`. The provided code has a "late binding" bug.

Your tasks:
1. Add comments explaining WHY the bug occurs
2. Implement `create_multipliers_fixed_a()` using default parameter binding
3. Implement `create_multipliers_fixed_b()` using `functools.partial`

**Your test input:** `{{MULTIPLIER_INPUT}}`
**Expected results:** `{{EXPECTED_RESULTS}}`

### Task 3: Global and Nonlocal Keywords (25 points)

Open `src/task3_scope_modifiers.py` and implement a counter system.

**Your test initial value:** `{{COUNTER_INITIAL}}`

Requirements:
- `increment()` returns the new value after adding 1
- `decrement()` returns the new value after subtracting 1
- `reset()` returns the initial value after resetting
- `get_value()` returns current value

### Task 4: Namespace Introspection (25 points)

Open `src/task4_introspection.py` and implement:
1. `analyze_scope(func)` - returns scope information dict
2. `find_shadowed_builtins(module)` - finds shadowed built-in names

---

## Running Tests

```bash
# Run visible tests (these are what you see)
pytest tests/visible/ -v

# Run a specific task's tests
pytest tests/visible/test_lab1.py::TestTask1LEGB -v
```

---

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all visible tests pass
3. Push your changes to trigger autograding
4. **Note:** Hidden tests will run after the deadline

---

## Grading Breakdown

| Component | Points | Type |
|-----------|--------|------|
| Visible Tests | 40 | Automatic |
| Hidden Tests | 30 | After deadline |
| Code Quality | 20 | Manual review |
| Plagiarism Check | -10 | Penalty if flagged |
| **Total** | 100 | |

---

## Academic Integrity

- Discuss concepts with classmates ✓
- Use Python documentation ✓
- Share or copy code ✗
- Use AI tools to generate solutions ✗

Your submission will be checked for similarity with other students.
