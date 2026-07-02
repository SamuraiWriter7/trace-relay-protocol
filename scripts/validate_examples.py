import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Trace Relay Record",
        "schema": ROOT / "schemas" / "trace-relay-record.schema.json",
        "example": ROOT / "examples" / "trace-relay-record.example.yaml",
    },
    {
        "name": "Trace Handoff Record",
        "schema": ROOT / "schemas" / "trace-handoff-record.schema.json",
        "example": ROOT / "examples" / "trace-handoff-record.example.yaml",
    },
    {
        "name": "Multi-Wing Trace Route",
        "schema": ROOT / "schemas" / "multi-wing-trace-route.schema.json",
        "example": ROOT / "examples" / "multi-wing-trace-route.example.yaml",
    },
    {
        "name": "Trace Transformation Rule",
        "schema": ROOT / "schemas" / "trace-transformation-rule.schema.json",
        "example": ROOT / "examples" / "trace-transformation-rule.example.yaml",
    },
    {
        "name": "Trace Diff Mutation Log",
        "schema": ROOT / "schemas" / "trace-diff-mutation-log.schema.json",
        "example": ROOT / "examples" / "trace-diff-mutation-log.example.yaml",
    },
    {
        "name": "Trace Re-Ignition Record",
        "schema": ROOT / "schemas" / "trace-re-ignition-record.schema.json",
        "example": ROOT / "examples" / "trace-re-ignition-record.example.yaml",
    },
    {
        "name": "Trace Royalty Bridge",
        "schema": ROOT / "schemas" / "trace-royalty-bridge.schema.json",
        "example": ROOT / "examples" / "trace-royalty-bridge.example.yaml",
    },
    {
        "name": "Structural Audit Bridge",
        "schema": ROOT / "schemas" / "structural-audit-bridge.schema.json",
        "example": ROOT / "examples" / "structural-audit-bridge.example.yaml",
    },
    {
        "name": "Human Gate Approval Receipt",
        "schema": ROOT / "schemas" / "human-gate-approval-receipt.schema.json",
        "example": ROOT / "examples" / "human-gate-approval-receipt.example.yaml",
    },
    {
        "name": "Unified Trace Relay Lifecycle",
        "schema": ROOT / "schemas" / "unified-trace-relay-lifecycle.schema.json",
        "example": ROOT / "examples" / "unified-trace-relay-lifecycle.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_target(target):
    schema_path = target["schema"]
    example_path = target["example"]

    print(f"[validate] {target['name']}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    instance = load_yaml(example_path)

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)

    if errors:
        for error in errors:
            path = ".".join(str(p) for p in error.path)
            location = path if path else "<root>"
            print(f"[error] {location}: {error.message}")
        raise SystemExit(1)

    print(f"[ok] {example_path.name} is valid")


def main():
    for target in VALIDATION_TARGETS:
        validate_target(target)


if __name__ == "__main__":
    main()
