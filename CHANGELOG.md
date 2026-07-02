# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0-candidate] - 2026-07-02

### Added

- Added `Multi-Wing Trace Route` schema.
- Added example YAML record for multi-wing trace routing.
- Updated validation script to validate Trace Relay, Trace Handoff, and Multi-Wing Trace Route records.

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

## [0.1.0-candidate] - 2026-07-02

### Added

- Initial definition of Trace Relay Protocol.
- Added `Trace Relay Record` schema.
- Added example YAML record.
- Added validation script for schema-example consistency.
- Added GitHub Actions workflow for automated validation.

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
Notes

This version establishes the minimum viable structure for treating dialogue-generated insights as relayable memory units.
