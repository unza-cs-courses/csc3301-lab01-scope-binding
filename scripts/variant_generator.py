#!/usr/bin/env python3
"""
Variant Generator for Lab 1: Scope and Binding
CSC3301 Programming Language Paradigms

Generates unique test parameters based on student ID.
Each student gets deterministic but unique values for testing.
"""
import hashlib
import json
import sys
import random
from pathlib import Path


def generate_variant(student_id: str) -> dict:
    """
    Generate a unique variant configuration based on student ID.

    Uses deterministic hashing so the same student ID always
    produces the same variant.
    """
    # Create deterministic seed from student ID
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)

    # Generate unique scope variable suffixes
    suffixes = ['ALPHA', 'BETA', 'GAMMA', 'DELTA', 'OMEGA', 'SIGMA', 'THETA', 'PHI']
    rng.shuffle(suffixes)

    # Generate unique counter test values
    counter_initials = [rng.randint(5, 50) for _ in range(3)]

    # Generate unique multiplier test input
    multiplier_input = rng.choice([5, 7, 8, 10, 12, 15, 20])

    # Generate secret value for introspection
    secret_value = rng.randint(10, 100)

    # Generate scope variable values
    global_value = f"GLOBAL_{suffixes[0]}"
    enclosing_value = f"ENCLOSING_{suffixes[1]}"
    local_value = f"LOCAL_{suffixes[2]}"

    variant = {
        "student_id": student_id,
        "variant_seed": seed,
        "scope_values": {
            "global": global_value,
            "enclosing": enclosing_value,
            "local": local_value,
            "builtin": "<class 'int'>"  # This stays constant
        },
        "counter_tests": {
            "initial_values": counter_initials,
            "expected_increments": [v + 1 for v in counter_initials],
            "expected_decrements": [v - 1 for v in counter_initials]
        },
        "closure_tests": {
            "multiplier_input": multiplier_input,
            "expected_results": [0, multiplier_input, multiplier_input*2,
                                multiplier_input*3, multiplier_input*4]
        },
        "introspection_tests": {
            "secret_value": secret_value
        }
    }

    return variant


def update_source_files(variant: dict, repo_root: Path):
    """
    Update source files with variant-specific values.
    """
    # Update task1_legb.py with variant scope values
    task1_path = repo_root / "src" / "task1_legb.py"
    if task1_path.exists():
        content = task1_path.read_text()
        scope = variant["scope_values"]

        # Update the expected output in docstring and global variable
        content = content.replace('x = "GLOBAL_X"', f'x = "{scope["global"]}"')
        content = content.replace('Global scope: GLOBAL_X', f'Global scope: {scope["global"]}')
        content = content.replace('Enclosing scope: ENCLOSING_X', f'Enclosing scope: {scope["enclosing"]}')
        content = content.replace('Local scope: LOCAL_X', f'Local scope: {scope["local"]}')

        task1_path.write_text(content)
        print(f"Updated {task1_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py john_doe")
        sys.exit(1)

    student_id = sys.argv[1]
    repo_root = Path(__file__).parent.parent

    print(f"Generating variant for student: {student_id}")

    # Generate variant
    variant = generate_variant(student_id)

    # Save variant config
    config_path = repo_root / ".variant_config.json"
    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)
    print(f"Saved variant config to {config_path}")

    # Update source files with variant values
    update_source_files(variant, repo_root)

    # Display summary
    print("\n=== Variant Summary ===")
    print(f"Student ID: {variant['student_id']}")
    print(f"Seed: {variant['variant_seed']}")
    print(f"Scope values: {variant['scope_values']}")
    print(f"Counter initials: {variant['counter_tests']['initial_values']}")
    print(f"Multiplier input: {variant['closure_tests']['multiplier_input']}")
    print(f"Secret value: {variant['introspection_tests']['secret_value']}")


if __name__ == "__main__":
    main()
