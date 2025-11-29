# Tasks: Content - Module 1: The Robotic Nervous System

**Input**: Design documents from `/specs/1-module-1-content/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit test tasks were requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths for content are `docs/module-01/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic content structure

- [X] T001 Create directory `docs/module-01/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 Verify Docusaurus project is runnable after content creation in the `physical-ai-textbook` directory

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Learning Foundations of Physical AI (Priority: P1) 🎯 MVP

**Goal**: Establish a fundamental understanding of Physical AI through the introductory chapter.

**Independent Test**: Review `01-intro-physical-ai.md` to confirm all foundational concepts (Embodied Intelligence, Digital vs Physical AI, Sensors) are clearly defined and explained.

### Implementation for User Story 1

- [X] T003 [US1] Create `01-intro-physical-ai.md` with Learning Outcomes, content, and Assessments in `docs/module-01/01-intro-physical-ai.md`
- [X] T004 [US1] Define "Embodied Intelligence" in `docs/module-01/01-intro-physical-ai.md`
- [X] T005 [P] [US1] Contrast "Digital AI" (ChatGPT) vs "Physical AI" (Tesla Bot) in `docs/module-01/01-intro-physical-ai.md`
- [X] T006 [P] [US1] Explain Sensors (LiDAR, Depth Cameras, IMUs) in `docs/module-01/01-intro-physical-ai.md`
- [X] T007 [US1] Add Docusaurus Admonitions for hardware safety warnings to `docs/module-01/01-intro-physical-ai.md`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mastering ROS 2 Fundamentals (Priority: P1)

**Goal**: Gain a working knowledge of the Robotic Operating System through the ROS 2 basics chapter.

**Independent Test**: Review `02-ros2-basics.md` to confirm understanding of ROS 2 concepts (Nervous System analogy, Nodes, Topics, Services), code examples, and URDF for robot description.

### Implementation for User Story 2

- [X] T008 [US2] Create `02-ros2-basics.md` with Learning Outcomes, content, and Assessments in `docs/module-01/02-ros2-basics.md`
- [X] T009 [US2] Explain the "Nervous System" analogy for ROS 2 in `docs/module-01/02-ros2-basics.md`
- [X] T010 [P] [US2] Cover ROS 2 Core Concepts: Nodes, Topics, Services in `docs/module-01/02-ros2-basics.md`
- [X] T011 [P] [US2] Provide Python (`rclpy`) code snippets for a basic Publisher/Subscriber in `docs/module-01/02-ros2-basics.md`
- [X] T012 [P] [US2] Explain URDF for describing a robot's body in XML in `docs/module-01/02-ros2-basics.md`
- [X] T013 [US2] Use Mermaid.js diagrams to visualize ROS 2 Node connections in `docs/module-01/02-ros2-basics.md`
- [X] T014 [US2] Add Docusaurus Admonitions for hardware safety warnings to `docs/module-01/02-ros2-basics.md`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Ensure overall quality and adherence to formatting standards.

- [X] T015 Ensure all links between `01-intro-physical-ai.md` and `02-ros2-basics.md` work in `docs/module-01/`
- [X] T016 Validate content is technically accurate regarding ROS 2 Humble/Iron in `docs/module-01/`
- [X] T017 Verify code blocks are syntax-highlighted (Python/XML) in `docs/module-01/`
- [X] T018 Confirm "Assessments" sections exist at the bottom of every page in `docs/module-01/`
- [X] T019 Run Docusaurus build process to check for any errors or warnings in `physical-ai-textbook` directory

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Content creation before cross-cutting concerns like link validation.
- Core content before formatting elements (admonitions, diagrams).

### Parallel Opportunities

- `T005` and `T006` for US1 can run in parallel.
- `T010`, `T011`, `T012` for US2 can run in parallel.
- User Story 1 and User Story 2 can be worked on in parallel by different team members after the Foundational phase.

---

## Parallel Example: User Story 1

```bash
# Launch parallel content creation for User Story 1:
Task: "Contrast Digital AI vs Physical AI in docs/module-01/01-intro-physical-ai.md"
Task: "Explain Sensors (LiDAR, Depth Cameras, IMUs) in docs/module-01/01-intro-physical-ai.md"
```

## Parallel Example: User Story 2

```bash
# Launch parallel content creation for User Story 2:
Task: "Cover ROS 2 Core Concepts: Nodes, Topics, Services in docs/module-01/02-ros2-basics.md"
Task: "Provide Python (rclpy) code snippets for a basic Publisher/Subscriber in docs/module-01/02-ros2-basics.md"
Task: "Explain URDF for describing a robot's body in XML in docs/module-01/02-ros2-basics.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
