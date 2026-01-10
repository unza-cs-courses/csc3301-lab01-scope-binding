# Lab 1: Scope, Binding, and Namespaces

**CSC3301 Programming Language Paradigms**  
**Estimated Time:** 1–1.5 hours  
**Points:** 100

---

## Purpose

This lab reinforces your understanding of how programming languages manage names, bindings, and scope. You will explore Python's scoping rules (LEGB), investigate how variables are resolved at runtime, and understand the difference between static and dynamic scoping through practical experiments.

---

## Learning Outcomes

By completing this lab, you will be able to:

1. Identify and explain Python's LEGB scope resolution order
2. Predict variable binding behavior in nested functions
3. Use the `global` and `nonlocal` keywords correctly
4. Distinguish between early and late binding in closures
5. Debug scope-related errors using Python's introspection tools

---

## Setup

1. Clone this repository
2. Ensure Python 3.10+ is installed: `python --version`
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests to verify setup: `pytest tests/ -v`

---

## Tasks

### Task 1: LEGB Scope Investigation (25 points)

Open `src/task1_legb.py` and complete the `investigate_legb()` function that demonstrates all four scope levels (Local, Enclosing, Global, Built-in).

Your output must match the expected format exactly.

### Task 2: Closure Binding Behavior (25 points)

Open `src/task2_closures.py`. The provided code has a "late binding" bug. Your tasks:

1. Add comments explaining WHY the bug occurs
2. Implement `create_multipliers_fixed_a()` using default parameter binding
3. Implement `create_multipliers_fixed_b()` using `functools.partial`

### Task 3: Global and Nonlocal Keywords (25 points)

Open `src/task3_scope_modifiers.py` and implement a counter system using closures:

- The counter state must persist between calls (use `nonlocal`)
- A global counter must track total operations across ALL counters (use `global`)

### Task 4: Namespace Introspection (25 points)

Open `src/task4_introspection.py` and implement:

1. `analyze_scope(func)` - returns a dict with local_vars, free_vars, global_refs, closure_values
2. `find_shadowed_builtins(module)` - finds built-in names that have been shadowed

---

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all tests pass: `pytest tests/ -v`
3. Fill out `SUBMISSION.md` with your reflection
4. Push your changes to trigger autograding

---

## Grading

| Component | Points |
|-----------|--------|
| Task 1: LEGB Demo | 25 |
| Task 2: Closure Fixes | 25 |
| Task 3: Scope Modifiers | 25 |
| Task 4: Introspection | 25 |
| **Total** | 100 |

---

## Academic Integrity

- Discuss concepts with classmates ✓
- Use Python documentation ✓
- Share or copy code ✗
- Use AI tools to generate solutions ✗
