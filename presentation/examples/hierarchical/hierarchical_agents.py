"""
Hierarchical Workflow Pattern (Orchestrator-Workers)

This example demonstrates parent-child delegation where a coordinator
breaks down tasks and assigns them to specialized workers.

Closely related to Phil Schmid's Planning pattern but with explicit hierarchy.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import anthropic


class WorkerType(Enum):
    """Types of specialized workers"""
    FRONTEND = "frontend"
    BACKEND = "backend"
    DATABASE = "database"
    TESTING = "testing"


@dataclass
class Task:
    """A task to be executed by a worker"""
    id: int
    description: str
    worker_type: WorkerType
    dependencies: List[int]  # Task IDs that must complete first
    status: str = "pending"  # pending, in_progress, completed
    result: Optional[str] = None


class WorkerAgent:
    """Specialized worker agent for specific domain"""

    def __init__(self, worker_type: WorkerType, api_key: str):
        self.worker_type = worker_type
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def execute_task(self, task: Task) -> str:
        """Execute the assigned task"""
        print(f"\n[{self.worker_type.value.upper()} Worker] Executing task {task.id}:")
        print(f"  {task.description}")

        # Craft specialized prompt based on worker type
        prompt = self._create_specialized_prompt(task)

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text
        print(f"[{self.worker_type.value.upper()} Worker] Task {task.id} complete")

        return result

    def _create_specialized_prompt(self, task: Task) -> str:
        """Create prompt specialized for this worker type"""
        role_context = {
            WorkerType.FRONTEND: "As a frontend specialist, focus on UI/UX, components, and user interaction.",
            WorkerType.BACKEND: "As a backend specialist, focus on business logic, APIs, and data processing.",
            WorkerType.DATABASE: "As a database specialist, focus on schema design, queries, and data integrity.",
            WorkerType.TESTING: "As a testing specialist, focus on test coverage, edge cases, and quality assurance."
        }

        context = role_context.get(self.worker_type, "")

        return f"""{context}

Task: {task.description}

Provide:
1. Implementation approach
2. Key considerations
3. Potential challenges
4. Deliverable summary

Be concise (150-200 words)."""


class CoordinatorAgent:
    """
    Parent agent that orchestrates the hierarchical workflow.

    Responsibilities:
    - Break down high-level goals into tasks
    - Assign tasks to specialized workers
    - Manage dependencies
    - Monitor progress
    - Synthesize results
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
        self.workers: Dict[WorkerType, WorkerAgent] = {}
        self.tasks: List[Task] = []

    def register_worker(self, worker_type: WorkerType):
        """Register a specialized worker"""
        self.workers[worker_type] = WorkerAgent(worker_type, self.api_key)
        print(f"[COORDINATOR] Registered {worker_type.value} worker")

    def decompose_goal(self, goal: str) -> List[Task]:
        """
        Break down high-level goal into concrete tasks.

        This is where the coordinator's planning intelligence comes in.
        """
        print(f"\n[COORDINATOR] Decomposing goal: {goal}")

        prompt = f"""Break down this development goal into concrete tasks:

Goal: {goal}

For each task, provide:
- Task description
- Which specialist should handle it (frontend, backend, database, or testing)
- Which other tasks it depends on (if any)

Format as numbered list (1-6 tasks)."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        plan_text = response.content[0].text
        print(f"\n[COORDINATOR] Generated plan:\n{plan_text}")

        # Parse plan into tasks (simplified - in production, use structured output)
        tasks = self._parse_plan(plan_text)

        return tasks

    def _parse_plan(self, plan_text: str) -> List[Task]:
        """Parse plan text into Task objects"""
        # Simplified parsing - in production, use LLM with structured output
        # For demo, we'll create a fixed set of tasks

        tasks = [
            Task(1, "Design database schema for todo items", WorkerType.DATABASE, []),
            Task(2, "Implement backend API endpoints (CRUD)", WorkerType.BACKEND, [1]),
            Task(3, "Create frontend components for todo list", WorkerType.FRONTEND, [2]),
            Task(4, "Write tests for backend API", WorkerType.TESTING, [2]),
            Task(5, "Write tests for frontend components", WorkerType.TESTING, [3]),
        ]

        self.tasks = tasks
        return tasks

    def execute_workflow(self, goal: str) -> Dict[str, Any]:
        """
        Execute the complete hierarchical workflow.

        Steps:
        1. Decompose goal into tasks
        2. Assign tasks to workers respecting dependencies
        3. Collect results
        4. Synthesize final deliverable
        """
        print(f"\n{'='*60}")
        print(f"[COORDINATOR] Starting hierarchical workflow")
        print(f"Goal: {goal}")
        print(f"{'='*60}")

        # Step 1: Decompose
        tasks = self.decompose_goal(goal)

        # Step 2: Execute tasks respecting dependencies
        results = {}

        for task in tasks:
            # Check dependencies
            if not self._dependencies_met(task):
                print(f"\n[COORDINATOR] Task {task.id} blocked by dependencies")
                task.status = "blocked"
                continue

            # Assign to worker
            worker_type = task.worker_type
            if worker_type not in self.workers:
                print(f"\n[COORDINATOR] No worker available for {worker_type.value}")
                continue

            # Execute
            task.status = "in_progress"
            worker = self.workers[worker_type]
            result = worker.execute_task(task)

            task.status = "completed"
            task.result = result
            results[task.id] = {
                "task": task.description,
                "worker": worker_type.value,
                "result": result
            }

        # Step 3: Synthesize
        print(f"\n[COORDINATOR] Synthesizing results...")
        synthesis = self._synthesize_results(goal, results)

        print(f"\n{'='*60}")
        print(f"[COORDINATOR] Workflow complete")
        print(f"{'='*60}")

        return {
            "goal": goal,
            "tasks": [t.__dict__ for t in tasks],
            "individual_results": results,
            "synthesis": synthesis
        }

    def _dependencies_met(self, task: Task) -> bool:
        """Check if all dependencies for a task are completed"""
        for dep_id in task.dependencies:
            dep_task = next((t for t in self.tasks if t.id == dep_id), None)
            if not dep_task or dep_task.status != "completed":
                return False
        return True

    def _synthesize_results(self, goal: str, results: Dict[int, Dict[str, Any]]) -> str:
        """Synthesize individual worker results into final deliverable"""
        combined = "\n\n".join([
            f"**Task {tid}** ({r['worker']}):\n{r['result']}"
            for tid, r in results.items()
        ])

        prompt = f"""As the project coordinator, synthesize these worker outputs into a cohesive final deliverable for: {goal}

Worker Outputs:
{combined}

Provide:
1. Overall project summary
2. Integration approach
3. Next steps
4. Success criteria

Be concise (200-250 words)."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    # Create coordinator
    coordinator = CoordinatorAgent(api_key)

    # Register specialized workers
    coordinator.register_worker(WorkerType.FRONTEND)
    coordinator.register_worker(WorkerType.BACKEND)
    coordinator.register_worker(WorkerType.DATABASE)
    coordinator.register_worker(WorkerType.TESTING)

    # Execute hierarchical workflow
    goal = "Build a todo list web application with CRUD operations"

    results = coordinator.execute_workflow(goal)

    # Display results
    print("\n" + "="*60)
    print("WORKFLOW RESULTS:")
    print("="*60)

    print(f"\nGoal: {results['goal']}")

    print(f"\nTasks ({len(results['tasks'])}):")
    for task in results['tasks']:
        status_icon = "✓" if task['status'] == "completed" else "○"
        print(f"  {status_icon} Task {task['id']}: {task['description']}")
        print(f"     Worker: {task['worker_type']}, Status: {task['status']}")

    print(f"\nIndividual Results:")
    for task_id, result in results['individual_results'].items():
        print(f"\n  Task {task_id} ({result['worker']}):")
        print(f"  {result['result'][:150]}...")

    print(f"\n{'='*60}")
    print("FINAL SYNTHESIS:")
    print("="*60)
    print(results['synthesis'])

    """
    Key Insights:

    1. **Clear Hierarchy**: Coordinator (parent) delegates to workers (children)
    2. **Specialized Workers**: Each worker has domain expertise
    3. **Dependency Management**: Coordinator ensures correct execution order
    4. **Centralized Control**: Coordinator has full visibility and control
    5. **Synthesis**: Coordinator integrates individual outputs

    Hierarchical vs Multi-Agent:
    - Hierarchical: Clear parent-child relationships, centralized control
    - Multi-Agent: Can be peer-to-peer, distributed coordination

    Hierarchical vs Planning:
    - Planning: Single agent decomposes and executes
    - Hierarchical: Coordinator delegates to specialized workers

    When to use Hierarchical:
    - Tasks have clear hierarchy
    - Need centralized coordination
    - Benefit from specialized workers
    - Want single point of control

    Design considerations:
    - How to break down goals? (Coordinator's intelligence)
    - How to handle worker failures? (Retry, reassign, escalate)
    - How to balance load? (Worker capacity management)
    - How to scale? (Add more workers of each type)

    Real-world applications:
    - Software development projects (architect coordinates specialists)
    - Complex data pipelines (orchestrator manages stages)
    - Multi-stage approvals (coordinator manages workflow)
    - Resource allocation systems (dispatcher assigns tasks)
    """
