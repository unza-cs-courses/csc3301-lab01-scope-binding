"""
Pytest configuration for visible tests.
Loads variant configuration if available.
"""
import json
import pytest
from pathlib import Path


def load_variant_config():
    """Load variant configuration from .variant_config.json."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Return default values if no variant config exists (template repo)
    return {
        "student_id": "template",
        "scope_values": {
            "global": "GLOBAL_X",
            "enclosing": "ENCLOSING_X",
            "local": "LOCAL_X",
            "builtin": "<class 'int'>"
        },
        "counter_tests": {
            "initial_values": [10, 20, 30],
            "expected_increments": [11, 21, 31],
            "expected_decrements": [9, 19, 29]
        },
        "closure_tests": {
            "multiplier_input": 10,
            "expected_results": [0, 10, 20, 30, 40]
        },
        "introspection_tests": {
            "secret_value": 42
        }
    }


@pytest.fixture(scope="session")
def variant_config():
    """Fixture providing variant configuration."""
    return load_variant_config()


@pytest.fixture
def scope_values(variant_config):
    """Fixture providing scope test values."""
    return variant_config["scope_values"]


@pytest.fixture
def counter_tests(variant_config):
    """Fixture providing counter test values."""
    return variant_config["counter_tests"]


@pytest.fixture
def closure_tests(variant_config):
    """Fixture providing closure test values."""
    return variant_config["closure_tests"]


@pytest.fixture
def introspection_tests(variant_config):
    """Fixture providing introspection test values."""
    return variant_config["introspection_tests"]
