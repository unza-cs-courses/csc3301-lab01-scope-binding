#!/usr/bin/env python3
"""Display test results from pytest JSON report."""
import json
import sys
from pathlib import Path

def main():
    results_file = Path('test_results.json')
    if not results_file.exists():
        print("No test results found")
        sys.exit(0)

    with open(results_file) as f:
        data = json.load(f)

    tests = data.get('tests', [])
    passed = sum(1 for t in tests if t['outcome'] == 'passed')
    failed = sum(1 for t in tests if t['outcome'] == 'failed')
    total = passed + failed

    print(f'Passed: {passed}/{total}')
    print(f'Score: {passed * 100 // max(total, 1)}%')
    print()

    for t in tests:
        status = '✓' if t['outcome'] == 'passed' else '✗'
        name = t['nodeid'].split('::')[-1]
        print(f'  {status} {name}')

if __name__ == '__main__':
    main()
