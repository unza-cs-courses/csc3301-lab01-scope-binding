#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Replace placeholders
    scope = variant["scope_values"]
    counter = variant["counter_tests"]
    closure = variant["closure_tests"]
    introspection = variant["introspection_tests"]

    assignment = template
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])
    assignment = assignment.replace("{{GLOBAL_VALUE}}", scope["global"])
    assignment = assignment.replace("{{ENCLOSING_VALUE}}", scope["enclosing"])
    assignment = assignment.replace("{{LOCAL_VALUE}}", scope["local"])
    assignment = assignment.replace("{{COUNTER_INITIAL}}", str(counter["initial_values"][0]))
    assignment = assignment.replace("{{MULTIPLIER_INPUT}}", str(closure["multiplier_input"]))
    assignment = assignment.replace("{{EXPECTED_RESULTS}}", str(closure["expected_results"]))
    assignment = assignment.replace("{{SECRET_VALUE}}", str(introspection["secret_value"]))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
