# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0-candidate] - 2026-07-02

### Added

- Added `Trace Royalty Bridge` schema.
- Added example YAML record for royalty and value-return preparation.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log
  - Trace Re-Ignition Record
  - Trace Royalty Bridge

### Defined

- Royalty OS Bridge as the value-return preparation layer of the protocol.
- `source_re_ignition` as the re-ignited trace source.
- `derivative_context` as the derivative structure connected to the trace lineage.
- `lineage_basis` as the trace, route, rule, mutation, and re-ignition references.
- `contribution_assessment` as the human, AI, wing, system, or external-source contribution record.
- `value_return_scope` as the attribution, royalty, revenue-share, credit, donation, or compute-credit scope.
- `allocation_rules` as the proposed value-return allocation logic.
- `eligibility_conditions` as required and blocking conditions for value-return claims.
- `royalty_receipt_output` as the proposed output record for downstream value-return systems.
- `audit` as the final boundary and review layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
Re-Ignition Layer = memory reactivation
Royalty OS Bridge = memory value-return preparation

## [0.6.0-candidate] - 2026-07-02

### Added

- Added `Trace Re-Ignition Record` schema.
- Added example YAML record for trace reactivation.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log
  - Trace Re-Ignition Record

### Defined

- Re-Ignition Layer as the memory reactivation layer of the protocol.
- `source_trace` as the audited trace being reactivated.
- `trigger_context` as the condition, input, or event that caused reactivation.
- `re_ignition_conditions` as the required, optional, and blocking conditions for reuse.
- `activation_plan` as the new question, intended output, and next routes.
- `context_compatibility` as the check between prior trace meaning and current use.
- `boundary_controls` as the preservation and non-claim requirements.
- `re_ignition_output` as the newly proposed trace and handoff recommendation.
- `audit` as the final review and boundary layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
Re-Ignition Layer = memory reactivation
Notes

This release begins the second arc of the Trace Relay Protocol.

v0.1–v0.5 established:

Record -> Handoff -> Route -> Transform -> Diff

v0.6 adds the ability to reactivate an audited trace into a new question, protocol extension, derivative route, audit bridge, or value-return layer.

This prevents traces from becoming dormant archives while also preventing contextless reuse.

## [0.5.0-candidate] - 2026-07-02

### Added

- Added `Trace Diff / Mutation Log` schema.
- Added example YAML record for trace mutation auditing.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log

### Defined

- Trace Diff / Mutation Log as the change-audit layer of the protocol.
- `source_trace` as the trace being transformed.
- `source_rule` as the transformation rule governing mutation.
- `mutation_context` as the type, actor, purpose, and target output of the mutation.
- `before_state` as the trace state before transformation.
- `after_state` as the trace state after transformation.
- `diff_summary` as the preserved, added, removed, and modified elements.
- `mutation_events` as structured records of transformation operations.
- `preservation_check` as the lineage, authorship, symbolic/factual, and human review verification layer.
- `risk_delta` as the risk change after mutation.
- `approval` as the human review and next-handoff gate.
- `audit` as the final boundary and validation layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
```

### Notes

This release records what actually changed during trace transformation.

It prevents silent mutation, origin erasure, untracked semantic drift, and invisible authorship shifts.

v0.5 completes the first full arc of the Trace Relay Protocol:

```text
Record -> Handoff -> Route -> Transform -> Diff
```

---

## [0.4.0-candidate] - 2026-07-02

### Added

- Added `Trace Transformation Rule` schema.
- Added example YAML record for transformation control.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule

### Defined

- Trace Transformation Rules as the mutation-control layer of the protocol.
- `applies_to` as the trace types, wing IDs, and route IDs covered by the rule.
- `source_route` as the originating route and source trace context.
- `transformation_scope` as the intended type and purpose of transformation.
- `allowed_transformations` as operations permitted under explicit conditions.
- `prohibited_transformations` as operations that would break lineage, authorship boundaries, or symbolic safety.
- `preservation_requirements` as required elements that must remain visible.
- `mutation_controls` as the maximum allowed transformation level and review requirements.
- `risk_assessment` as the semantic drift, authorship, and mythic overextension risk layer.
- `output_requirements` as required and forbidden outputs.
- `audit` as the final review and boundary layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
```

### Notes

This release defines how conceptual traces may be transformed without becoming origin-erased, semantically drifted, or mythically overextended.

It prepares the project for future derivative output receipts, Human Gate approval records, and Trace Diff / Mutation Logs.

---

## [0.3.0-candidate] - 2026-07-02

### Added

- Added `Multi-Wing Trace Route` schema.
- Added example YAML record for multi-wing trace routing.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route

### Defined

- Multi-Wing Trace Route as the orchestration layer for passing conceptual traces across specialized AI wings.
- `source_handoff` as the originating handoff record.
- `wings` as specialized processing units with allowed operations, prohibited operations, and output contracts.
- `route_sequence` as the ordered trace movement across wings.
- `continuity_rules` as lineage and integrity preservation rules.
- `blocking_conditions` as conditions that stop routing.
- `human_gate` as the final human review layer.
- `audit` as the boundary and lineage verification layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
```

### Notes

This release extends Trace Relay Protocol from simple trace transfer into multi-wing coordination.

It prepares the project for future trace transformation rules, receiving wing responsibilities, audit bridges, and derivative lineage control.

---

## [0.2.0-candidate] - 2026-07-02

### Added

- Added `Trace Handoff Record` schema.
- Added example YAML record for trace handoff.
- Updated validation script to validate both Trace Relay and Trace Handoff records.

### Defined

- Trace Handoff as the transfer of a preserved conceptual trace into another dialogue, AI wing, memory layer, audit layer, repository, document, or derivative structure.
- `source_trace` as the trace being handed off.
- `handoff_source` as the originating system, layer, human, AI, or wing.
- `handoff_target` as the receiving context.
- `handoff_payload` as the preserved trace elements and transformation intent.
- `route` as the handoff mode, next actions, and blocking conditions.
- `continuity` as the lineage-preserving layer.
- `audit` as the authorship and boundary review layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
```

### Notes

This release extends the protocol from preserving conceptual traces to transferring them across systems and specialized contexts.

It prepares the project for future Multi-Wing Trace Handoff, where Finder, Analyst, Memory, Audit, Mythos Regulator, and Human Gate layers can pass trace payloads between each other.

---

## [0.1.0-candidate] - 2026-07-02

### Added

- Initial definition of Trace Relay Protocol.
- Added `Trace Relay Record` schema.
- Added example YAML record.
- Added validation script for schema-example consistency.
- Added GitHub Actions workflow for automated validation.
- Added initial README and CHANGELOG documentation.

### Defined

- Trace as a seed of latent structure.
- Trace Relay as a process for handing conceptual traces forward.
- Yin Layer as preserved structure and reflection.
- Yang Layer as new ignition, question, and human intent.
- Relay Output as the newly generated trace.
- Handoff as the next possible route for development.
- Audit as the human review and boundary layer.

### Core Flow

```text
Origin -> Trace -> Relay -> Derivative -> Audit -> Return
```

### Notes

This version establishes the minimum viable structure for treating dialogue-generated insights as relayable memory units.
