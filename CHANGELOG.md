# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0-candidate] - 2026-07-02

### Added

- Added `Unified Trace Relay Lifecycle` schema.
- Added example YAML record for the complete Trace Relay lifecycle.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log
  - Trace Re-Ignition Record
  - Trace Royalty Bridge
  - Structural Audit Bridge
  - Human Gate Approval Receipt
  - Unified Trace Relay Lifecycle

### Defined

- Unified Trace Relay Lifecycle as the lifecycle-continuity layer of the protocol.
- `origin_summary` as the origin context of the lifecycle.
- `layer_refs` as the references to all lifecycle layer records.
- `phase_sequence` as the ordered progression across record, handoff, route, transform, diff, re-ignition, royalty bridge, structural audit, and human gate.
- `current_state` as the current lifecycle phase, status, open conditions, and blocked claims.
- `completion_criteria` as the requirements for lifecycle completion.
- `continuity_controls` as the preservation, non-claim, and carry-forward requirements.
- `next_cycle` as the next allowed cycle or derivative route.
- `governance` as the human authority and AI support boundary.
- `audit` as the lifecycle validity and final boundary layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
Re-Ignition Layer = memory reactivation
Royalty OS Bridge = memory value-return preparation
Structural Audit Bridge = memory causality verification
Human Gate Approval Receipt = memory governance approval
Unified Trace Relay Lifecycle = memory lifecycle continuity
```

### Notes

This release completes the first full Trace Relay Protocol lifecycle.

v0.1–v0.9 defined the individual layers.

v1.0 connects those layers into a unified lifecycle that can track a trace from dialogue origin to human-approved continuation.

The first lifecycle arc is now:

```text
Record -> Handoff -> Route -> Transform -> Diff -> Re-Ignition -> Royalty Bridge -> Structural Audit -> Human Gate -> Next Cycle
```

This establishes Trace Relay Protocol as a complete dialogue-memory lifecycle protocol.

---

## [0.9.0-candidate] - 2026-07-02

### Added

- Added `Human Gate Approval Receipt` schema.
- Added example YAML record for human approval after structural audit.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log
  - Trace Re-Ignition Record
  - Trace Royalty Bridge
  - Structural Audit Bridge
  - Human Gate Approval Receipt

### Defined

- Human Gate Approval Receipt as the human decision and governance layer of the protocol.
- `source_structural_audit` as the audit record being reviewed.
- `approval_subject` as the publication, derivative, attribution, royalty review, repository release, or protocol extension under approval.
- `reviewer` as the human originator, reviewer, collective review body, or maintainer.
- `decision` as the approval, conditional approval, revision request, rejection, or deferral.
- `approved_scope` as the actions, claims, and outputs allowed to proceed.
- `rejected_scope` as the actions and claims explicitly blocked.
- `conditions` as the requirements before next handoff, publication, or value allocation.
- `risk_acknowledgement` as the accepted and unaccepted risks.
- `next_handoff` as the next allowed route and required conditions.
- `audit` as the receipt validity and final boundary layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
Re-Ignition Layer = memory reactivation
Royalty OS Bridge = memory value-return preparation
Structural Audit Bridge = memory causality verification
Human Gate Approval Receipt = memory governance approval
```

### Notes

This release adds the human governance layer.

v0.8 verifies structural causality and evidence.

v0.9 records the human decision that follows that verification.

It prevents structural audit from being mistaken for final approval and ensures that conditional approval, rejected claims, and next-handoff conditions remain explicit.

---

## [0.8.0-candidate] - 2026-07-02

### Added

- Added `Structural Audit Bridge` schema.
- Added example YAML record for structural causality and value-claim audit.
- Updated validation script to validate:
  - Trace Relay Record
  - Trace Handoff Record
  - Multi-Wing Trace Route
  - Trace Transformation Rule
  - Trace Diff Mutation Log
  - Trace Re-Ignition Record
  - Trace Royalty Bridge
  - Structural Audit Bridge

### Defined

- Structural Audit Bridge as the causality-verification layer of the protocol.
- `source_royalty_bridge` as the value-return bridge being audited.
- `audit_subject` as the derivative, attribution, royalty, lineage, or authorship claim under review.
- `structural_causality` as the causal-link assessment between traces, derivatives, mutation logs, re-ignition, and bridge records.
- `evidence_map` as the supporting and missing evidence layer.
- `similarity_assessment` as the similarity and independent-convergence review.
- `dependency_assessment` as the structural dependency review.
- `attribution_review` as the attribution requirement and risk layer.
- `value_claim_review` as the allowed and blocked value-claim layer.
- `audit_decision` as the approval, revision, rejection, or pending decision layer.
- `handoff` as the next recommended review or approval route.
- `audit` as the final boundary layer.

### Core Distinction

```text
Trace Relay = memory circulation
Trace Handoff = memory transfer
Multi-Wing Trace Route = memory orchestration
Trace Transformation Rules = memory mutation control
Trace Diff / Mutation Log = memory change audit
Re-Ignition Layer = memory reactivation
Royalty OS Bridge = memory value-return preparation
Structural Audit Bridge = memory causality verification
```

### Notes

This release strengthens the protocol’s audit layer.

v0.7 prepared attribution and value-return claims.

v0.8 verifies whether those claims are supported by trace lineage, structural causality, evidence, and human review.

It prevents value-return logic from becoming automatic, unsupported, or detached from origin evidence.

---

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
```

### Notes

This release connects Trace Relay Protocol to attribution and value-return structures.

It does not define automatic monetary royalty.

Instead, it prepares lineage-aware attribution, contribution assessment, and royalty eligibility conditions while preserving human review, derivative evidence, and structural audit requirements.

---

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
```

### Notes

This release begins the second arc of the Trace Relay Protocol.

v0.1–v0.5 established:

```text
Record -> Handoff -> Route -> Transform -> Diff
```

v0.6 adds the ability to reactivate an audited trace into a new question, protocol extension, derivative route, audit bridge, or value-return layer.

This prevents traces from becoming dormant archives while also preventing contextless reuse.

---

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
