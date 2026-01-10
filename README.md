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

## Getting Started

### For Students (via GitHub Classroom)

When you accept this assignment, a unique variant is automatically generated for you:

1. Your repository will have a `.variant_config.json` file with your personalized test values
2. Check `ASSIGNMENT.md` for your specific requirements
3. Your code must produce output matching your variant values

### Manual Setup (Instructors/Testing)

```bash
# Clone the repository
git clone <repo-url>
cd csc3301-lab01-scope-binding

# Install dependencies
pip install -r requirements.txt

# Generate a variant manually (optional)
python scripts/variant_generator.py <student_id>

# Run tests
pytest tests/visible/ -v
```

---

## Tasks

### Task 1: LEGB Scope Investigation (25 points)

Open `src/task1_legb.py` and complete the `investigate_legb()` function that demonstrates all four scope levels (Local, Enclosing, Global, Built-in).

Your output must match the expected format in your `ASSIGNMENT.md` exactly.

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

## Running Tests

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run tests for a specific task
pytest tests/visible/test_lab1.py::TestTask1LEGB -v
pytest tests/visible/test_lab1.py::TestTask2Closures -v
pytest tests/visible/test_lab1.py::TestTask3ScopeModifiers -v
pytest tests/visible/test_lab1.py::TestTask4Introspection -v
```

**Note:** Visible tests run on every push. Hidden tests with additional edge cases will run after the submission deadline.

---

## Submission

1. Complete all tasks in the `src/` directory
2. Ensure all visible tests pass: `pytest tests/visible/ -v`
3. Push your changes to trigger autograding
4. Check the Actions tab for your results

---

## Grading

| Component | Points | When |
|-----------|--------|------|
| Visible Tests | 40 | Every push |
| Hidden Tests | 30 | After deadline |
| Code Quality | 20 | Manual review |
| Plagiarism | -10 | If flagged |
| **Total** | 100 | |

---

## File Structure

```
.
├── .github/
│   ├── scripts/
│   │   └── display_results.py
│   └── workflows/
│       ├── autograding.yml      # Runs visible tests
│       └── generate-variant.yml # Generates student variant
├── scripts/
│   ├── variant_generator.py     # Creates unique test values
│   └── generate_assignment.py   # Creates personalized ASSIGNMENT.md
├── src/
│   ├── task1_legb.py
│   ├── task2_closures.py
│   ├── task3_scope_modifiers.py
│   └── task4_introspection.py
├── tests/
│   └── visible/
│       ├── conftest.py          # Loads variant config
│       └── test_lab1.py         # Visible test suite
├── .variant_config.json         # Your unique test values (generated)
├── ASSIGNMENT.md                # Your personalized assignment (generated)
├── ASSIGNMENT_TEMPLATE.md       # Template for generating ASSIGNMENT.md
└── README.md                    # This file
```

---

## Academic Integrity

- Discuss concepts with classmates ✓
- Use Python documentation ✓
- Share or copy code ✗
- Use AI tools to generate solutions ✗

Your submission will be checked for similarity with other students using automated plagiarism detection.
