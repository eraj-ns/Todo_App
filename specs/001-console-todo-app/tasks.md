---
description: "Task list for console-based todo application"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan with src/models, src/services, src/cli directories

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T002 [P] Define Todo data class in src/models/todo.py with id, title, description, status attributes
- [x] T003 [P] Implement in-memory storage mechanism in src/models/todo.py using dictionary
- [x] T004 [P] Create TodoService class in src/services/todo_service.py with basic CRUD methods
- [x] T005 [P] Implement CLI argument parsing framework in src/cli/main.py
- [x] T006 Create basic application entry point in src/cli/main.py that initializes services

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo tasks with a description via console command

**Independent Test**: Can be fully tested by running the add command with a task description and verifying the task appears in the list. Delivers core value of capturing tasks.

### Implementation for User Story 1

- [x] T007 [US1] Implement add_todo method in src/services/todo_service.py that creates new todo with auto-generated ID
- [x] T008 [US1] Add validation for task title in src/services/todo_service.py to handle empty descriptions
- [x] T009 [US1] Implement 'add' command parsing in src/cli/main.py
- [x] T010 [US1] Connect 'add' command to service method in src/cli/main.py
- [x] T011 [US1] Add success message output when todo is added in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Tasks (Priority: P2)

**Goal**: Allow users to see all their pending todo tasks at once with their status

**Independent Test**: Can be fully tested by adding several tasks and then running the view command to display all tasks. Delivers value by showing the user's task list.

### Implementation for User Story 2

- [x] T012 [US2] Implement get_all_todos method in src/services/todo_service.py that returns all todos
- [x] T013 [US2] Implement 'view' command parsing in src/cli/main.py
- [x] T014 [US2] Connect 'view' command to service method in src/cli/main.py
- [x] T015 [US2] Format and display todos in a user-friendly way in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Task as Complete (Priority: P3)

**Goal**: Allow users to mark specific todo tasks as complete using a unique identifier

**Independent Test**: Can be fully tested by adding a task, marking it complete, and then viewing the list to confirm the status change. Delivers value by allowing progress tracking.

### Implementation for User Story 3

- [x] T016 [US3] Implement mark_complete method in src/services/todo_service.py that updates todo status
- [x] T017 [US3] Add validation for task ID in src/services/todo_service.py to handle non-existent tasks
- [x] T018 [US3] Implement 'complete' command parsing in src/cli/main.py
- [x] T019 [US3] Connect 'complete' command to service method in src/cli/main.py
- [x] T020 [US3] Add success/error message output in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: Additional Functionality - Delete and Update

**Goal**: Implement remaining CRUD operations for complete functionality

### Implementation for Delete Functionality

- [x] T021 [P] [US4] Implement delete_todo method in src/services/todo_service.py
- [x] T022 [P] [US4] Implement 'delete' command parsing in src/cli/main.py
- [x] T023 [US4] Connect 'delete' command to service method in src/cli/main.py

### Implementation for Update Functionality

- [x] T024 [P] [US5] Implement update_todo method in src/services/todo_service.py
- [x] T025 [P] [US5] Implement 'update' command parsing in src/cli/main.py
- [x] T026 [US5] Connect 'update' command to service method in src/cli/main.py

**Checkpoint**: Full CRUD functionality is now available

---

## Phase 7: Error Handling and Edge Cases

**Goal**: Handle invalid inputs and edge conditions gracefully

- [x] T027 [P] Add error handling for invalid commands in src/cli/main.py
- [x] T028 [P] Add error handling for invalid task IDs in src/services/todo_service.py
- [x] T029 [P] Add validation for special characters and long descriptions in src/services/todo_service.py
- [x] T030 [P] Add appropriate error messages for all failure cases

**Checkpoint**: Application handles edge cases and errors gracefully

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T031 [P] Add proper logging throughout the application
- [x] T032 [P] Add help command to display available commands
- [x] T033 [P] Improve output formatting and user experience
- [x] T034 [P] Add basic documentation in README.md
- [x] T035 Run quickstart validation to ensure all commands work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Additional Functionality (Phase 6)**: Depends on foundational user stories
- **Error Handling (Phase 7)**: Can be implemented in parallel with other functionality
- **Polish (Final Phase)**: Depends on all desired functionality being complete

### Within Each User Story

- Models before services
- Services before CLI implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members
- Tasks within different user stories can run in parallel (e.g., T007 [US1] and T012 [US2])

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
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add additional functionality → Test → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [US1], [US2], [US3] labels map task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence