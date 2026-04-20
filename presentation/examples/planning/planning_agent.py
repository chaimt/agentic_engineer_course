"""
Planning Pattern Example - Task Decomposition and Execution

This example demonstrates how an agent can break down complex goals
into structured sub-tasks before execution.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum
import anthropic


class TaskStatus(Enum):
    """Status of a sub-task"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class SubTask:
    """Represents a single sub-task in the plan"""
    id: int
    description: str
    dependencies: List[int]  # IDs of tasks that must complete first
    status: TaskStatus = TaskStatus.PENDING
    result: str = ""


class PlanningAgent:
    """
    Agent that uses planning to decompose complex tasks.

    Pattern: Understand Goal → Decompose → Order → Execute → Verify
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def create_plan(self, goal: str) -> List[SubTask]:
        """
        Decompose a high-level goal into concrete sub-tasks

        Returns: Ordered list of sub-tasks with dependencies
        """
        planning_prompt = f"""Given this goal: "{goal}"

Break it down into specific, actionable sub-tasks.

For each sub-task, provide:
1. A clear description (what specifically to do)
2. Dependencies (which other tasks must complete first)

Format your response as a numbered list with dependencies noted."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": planning_prompt}]
        )

        plan_text = response.content[0].text

        # Parse the plan into SubTask objects (simplified for example)
        # In a real implementation, you'd use structured output
        subtasks = self._parse_plan(plan_text)

        return subtasks

    def _parse_plan(self, plan_text: str) -> List[SubTask]:
        """Parse plan text into structured SubTask objects"""
        # Simplified parsing - in reality you'd use structured output
        lines = [line.strip() for line in plan_text.split('\n') if line.strip()]

        subtasks = []
        task_id = 1

        for line in lines:
            if line[0].isdigit():
                # Extract task description (simple regex would be better)
                description = line.split('.', 1)[1].strip() if '.' in line else line

                # Determine dependencies (simplified - look for "after task X")
                dependencies = []
                if "after" in description.lower():
                    # Extract dependency IDs (very simplified)
                    parts = description.split("after")
                    if len(parts) > 1:
                        # Try to extract numbers
                        import re
                        numbers = re.findall(r'\d+', parts[1])
                        dependencies = [int(n) for n in numbers if int(n) < task_id]

                subtasks.append(SubTask(
                    id=task_id,
                    description=description,
                    dependencies=dependencies
                ))
                task_id += 1

        return subtasks

    def execute_plan(self, subtasks: List[SubTask]) -> Dict[str, Any]:
        """
        Execute sub-tasks in order, respecting dependencies

        Returns: Execution results and overall status
        """
        print(f"\nExecuting plan with {len(subtasks)} sub-tasks...\n")

        results = {
            "completed": [],
            "failed": [],
            "total": len(subtasks)
        }

        # Execute tasks in order
        for task in subtasks:
            # Check if dependencies are met
            if not self._dependencies_met(task, subtasks):
                print(f"❌ Task {task.id} blocked - dependencies not met")
                task.status = TaskStatus.FAILED
                results["failed"].append(task.id)
                continue

            # Execute the task
            print(f"→ Task {task.id}: {task.description}")
            task.status = TaskStatus.IN_PROGRESS

            try:
                # Simulate task execution
                # In a real agent, this would call tools or other agents
                task.result = f"Completed: {task.description}"
                task.status = TaskStatus.COMPLETED
                results["completed"].append(task.id)
                print(f"  ✓ Completed\n")

            except Exception as e:
                task.status = TaskStatus.FAILED
                task.result = f"Failed: {str(e)}"
                results["failed"].append(task.id)
                print(f"  ✗ Failed: {e}\n")

        return results

    def _dependencies_met(self, task: SubTask, all_tasks: List[SubTask]) -> bool:
        """Check if all dependencies for a task are completed"""
        for dep_id in task.dependencies:
            dep_task = next((t for t in all_tasks if t.id == dep_id), None)
            if not dep_task or dep_task.status != TaskStatus.COMPLETED:
                return False
        return True

    def verify_goal(self, goal: str, results: Dict[str, Any]) -> bool:
        """Verify if the original goal was achieved"""
        verification_prompt = f"""Given this goal: "{goal}"

And these completed tasks: {results['completed']}
Failed tasks: {results['failed']}

Was the goal successfully achieved? Answer YES or NO and explain why."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": verification_prompt}]
        )

        verification = response.content[0].text
        print(f"\nGoal Verification:\n{verification}")

        return "YES" in verification.upper()

    def execute_goal(self, goal: str) -> bool:
        """
        Complete workflow: Plan, Execute, Verify

        Returns: True if goal was achieved
        """
        print("="*60)
        print(f"GOAL: {goal}")
        print("="*60)

        # Step 1: Create plan
        print("\n📋 STEP 1: Creating Plan...")
        subtasks = self.create_plan(goal)

        print(f"\nGenerated plan with {len(subtasks)} sub-tasks:")
        for task in subtasks:
            deps = f" (depends on: {task.dependencies})" if task.dependencies else ""
            print(f"  {task.id}. {task.description}{deps}")

        # Step 2: Execute plan
        print("\n⚡ STEP 2: Executing Plan...")
        results = self.execute_plan(subtasks)

        # Step 3: Verify goal achieved
        print("\n✅ STEP 3: Verifying Goal...")
        success = self.verify_goal(goal, results)

        print("\n" + "="*60)
        print(f"RESULT: {'SUCCESS' if success else 'FAILED'}")
        print(f"Completed: {len(results['completed'])}/{results['total']}")
        print("="*60)

        return success


# Example usage
if __name__ == "__main__":
    # Initialize planning agent
    agent = PlanningAgent(api_key="your-api-key")

    # Example 1: Simple goal
    goal1 = "Add user authentication to a web application"

    print("\nEXAMPLE 1: User Authentication")
    agent.execute_goal(goal1)

    # Example 2: Complex goal with dependencies
    goal2 = "Build a REST API for a todo list with CRUD operations and authentication"

    print("\n\nEXAMPLE 2: Todo API")
    agent.execute_goal(goal2)

    """
    Expected output demonstrates:
    1. Goal decomposition into concrete sub-tasks
    2. Dependency identification and ordering
    3. Sequential execution respecting dependencies
    4. Verification that goal was achieved

    Key insights:
    - Planning transforms "what" into "how"
    - Dependencies ensure correct execution order
    - Verification confirms goal achievement
    - Complex tasks become manageable sequences

    This pattern is especially powerful for:
    - Multi-file changes
    - Projects with dependencies
    - Tasks requiring specific ordering
    - Complex workflows with decision points
    """
