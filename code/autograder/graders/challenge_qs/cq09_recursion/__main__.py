"""Autograder for Challenge Question."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="exercises/ex10",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=90.0,
    typecheck_points=5.0,
    lint_points=5.0
)

results = autograde.run(configuration)

print(results.to_json())
