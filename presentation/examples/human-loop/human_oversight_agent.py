"""
Human-in-the-Loop Pattern

This example demonstrates how to integrate human oversight
at critical decision points in agentic workflows.

Combines autonomous agent execution with strategic human checkpoints.
"""

from typing import Dict, Any, Optional, Callable
from enum import Enum
import anthropic


class HumanDecision(Enum):
    """Possible human decisions at checkpoints"""
    APPROVE = "approve"
    REJECT = "reject"
    MODIFY = "modify"
    ESCALATE = "escalate"


class CheckpointResult:
    """Result from a human review checkpoint"""

    def __init__(self, decision: HumanDecision, feedback: Optional[str] = None, modified_content: Optional[str] = None):
        self.decision = decision
        self.feedback = feedback
        self.modified_content = modified_content


class HumanInTheLoopAgent:
    """
    Agent that pauses for human oversight at critical checkpoints.

    Design principle: Agents handle routine work, humans make critical decisions.
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def generate_initial_output(self, task: str) -> str:
        """Agent generates initial output"""
        print(f"\n[AGENT] Generating initial output for: {task}")

        prompt = f"""Complete this task:

{task}

Provide a thorough, well-structured response."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.content[0].text
        print(f"[AGENT] Initial output generated ({len(output)} chars)")

        return output

    def request_human_review(self, output: str, context: str, human_review_fn: Callable[[str, str], CheckpointResult]) -> CheckpointResult:
        """
        Pause execution for human review.

        Args:
            output: Agent's output to review
            context: Context for the human reviewer
            human_review_fn: Function to simulate human review

        Returns:
            CheckpointResult with human's decision
        """
        print(f"\n[SYSTEM] ⏸️  Pausing for human review...")
        print(f"[SYSTEM] Context: {context}")
        print(f"[SYSTEM] Output preview: {output[:200]}...")

        # In real system, this would present to actual human
        # For demo, we call the human_review_fn (simulates human)
        result = human_review_fn(output, context)

        print(f"\n[HUMAN] Decision: {result.decision.value}")
        if result.feedback:
            print(f"[HUMAN] Feedback: {result.feedback}")

        return result

    def incorporate_feedback(self, original_output: str, feedback: str) -> str:
        """Agent incorporates human feedback into output"""
        print(f"\n[AGENT] Incorporating human feedback...")

        prompt = f"""Original output:
{original_output}

Human feedback:
{feedback}

Update the output based on the human feedback. Preserve what was good, address the feedback points."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        revised = response.content[0].text
        print(f"[AGENT] Feedback incorporated")

        return revised

    def execute_with_human_oversight(
        self,
        task: str,
        checkpoints: list[tuple[str, Callable[[str, str], CheckpointResult]]],
        max_iterations: int = 3
    ) -> Dict[str, Any]:
        """
        Execute task with human-in-the-loop checkpoints.

        Args:
            task: Task description
            checkpoints: List of (context, review_fn) tuples for each checkpoint
            max_iterations: Maximum refinement iterations

        Returns:
            Complete workflow results with history
        """
        print(f"\n{'='*60}")
        print(f"Human-in-the-Loop Workflow: {task[:60]}...")
        print(f"{'='*60}")

        history = []
        current_output = self.generate_initial_output(task)

        for checkpoint_idx, (context, review_fn) in enumerate(checkpoints):
            iteration = 0

            while iteration < max_iterations:
                # Human review checkpoint
                result = self.request_human_review(current_output, context, review_fn)

                history.append({
                    "checkpoint": checkpoint_idx,
                    "iteration": iteration,
                    "decision": result.decision.value,
                    "output": current_output
                })

                if result.decision == HumanDecision.APPROVE:
                    print(f"\n[SYSTEM] ✅ Checkpoint {checkpoint_idx} approved, continuing...")
                    break

                elif result.decision == HumanDecision.MODIFY:
                    if result.modified_content:
                        print(f"[SYSTEM] Using human-modified content")
                        current_output = result.modified_content
                    elif result.feedback:
                        current_output = self.incorporate_feedback(current_output, result.feedback)
                    iteration += 1

                elif result.decision == HumanDecision.REJECT:
                    print(f"\n[SYSTEM] ❌ Checkpoint {checkpoint_idx} rejected, regenerating...")
                    current_output = self.generate_initial_output(f"{task}\n\nAddress this concern: {result.feedback}")
                    iteration += 1

                elif result.decision == HumanDecision.ESCALATE:
                    print(f"\n[SYSTEM] ⚠️ Escalated to higher authority")
                    return {
                        "status": "escalated",
                        "reason": result.feedback,
                        "output": current_output,
                        "history": history
                    }

            if iteration >= max_iterations:
                print(f"\n[SYSTEM] ⚠️ Max iterations reached at checkpoint {checkpoint_idx}")
                return {
                    "status": "max_iterations",
                    "output": current_output,
                    "history": history
                }

        print(f"\n[SYSTEM] ✅ All checkpoints passed!")
        return {
            "status": "approved",
            "output": current_output,
            "history": history
        }


class ApprovalWorkflow:
    """
    Example: Document approval workflow with multiple HITL checkpoints.

    Demonstrates strategic checkpoint placement for quality and compliance.
    """

    def __init__(self, api_key: str):
        self.agent = HumanInTheLoopAgent(api_key)

    def simulate_legal_review(self, output: str, context: str) -> CheckpointResult:
        """Simulate legal team review"""
        # In real system, actual lawyer reviews
        # For demo, simple heuristic

        if "confidential" in output.lower() or "proprietary" in output.lower():
            return CheckpointResult(
                HumanDecision.MODIFY,
                feedback="Add standard confidentiality disclaimer"
            )

        return CheckpointResult(HumanDecision.APPROVE)

    def simulate_client_review(self, output: str, context: str) -> CheckpointResult:
        """Simulate client approval"""
        # In real system, client reviews
        # For demo, always approve if reasonable length

        if len(output) < 100:
            return CheckpointResult(
                HumanDecision.REJECT,
                feedback="Response too brief, provide more detail"
            )

        return CheckpointResult(HumanDecision.APPROVE)

    def execute_document_workflow(self, task: str) -> Dict[str, Any]:
        """Execute document generation with legal and client review"""
        checkpoints = [
            ("Legal review for compliance", self.simulate_legal_review),
            ("Client approval of final content", self.simulate_client_review)
        ]

        return self.agent.execute_with_human_oversight(task, checkpoints)


class SafetyCheck:
    """
    Example: Safety-critical system with mandatory human approval.

    For high-stakes domains: medical, financial, legal, safety-critical.
    """

    def __init__(self, api_key: str):
        self.agent = HumanInTheLoopAgent(api_key)

    def safety_review(self, output: str, context: str) -> CheckpointResult:
        """Mandatory safety review"""
        # In real system, safety expert reviews
        # For demo, check for safety keywords

        risk_keywords = ["delete", "irreversible", "permanent", "cannot undo"]

        if any(keyword in output.lower() for keyword in risk_keywords):
            return CheckpointResult(
                HumanDecision.ESCALATE,
                feedback="Contains irreversible action - requires senior approval"
            )

        return CheckpointResult(HumanDecision.APPROVE)

    def execute_safety_workflow(self, task: str) -> Dict[str, Any]:
        """Execute with mandatory safety checkpoint"""
        checkpoints = [
            ("Safety review for high-stakes operation", self.safety_review)
        ]

        return self.agent.execute_with_human_oversight(task, checkpoints)


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    print("="*60)
    print("EXAMPLE 1: Document Approval Workflow")
    print("="*60)

    approval_workflow = ApprovalWorkflow(api_key)

    task = "Draft a partnership agreement between Company A and Company B for joint product development"
    result = approval_workflow.execute_document_workflow(task)

    print(f"\n{'='*60}")
    print(f"FINAL RESULT:")
    print(f"Status: {result['status']}")
    print(f"Checkpoints passed: {len(result['history'])}")
    print(f"Output:\n{result['output'][:300]}...")
    print(f"{'='*60}\n")

    # Example 2: Safety-Critical System
    print("\n\n" + "="*60)
    print("EXAMPLE 2: Safety-Critical System")
    print("="*60)

    safety_check = SafetyCheck(api_key)

    task = "Generate SQL commands to archive old user data"
    result = safety_check.execute_safety_workflow(task)

    print(f"\n{'='*60}")
    print(f"FINAL RESULT:")
    print(f"Status: {result['status']}")
    if result['status'] == 'escalated':
        print(f"Escalation reason: {result['reason']}")
    print(f"{'='*60}\n")

    """
    Key Insights:

    1. **Strategic Checkpoints**: Place HITL where human expertise adds value
    2. **Checkpoint Types**:
       - Quality review (content, code)
       - Compliance review (legal, regulatory)
       - Safety review (high-stakes, irreversible)
       - Approval (client, stakeholder)
    3. **Decisions**: Approve, Reject (regenerate), Modify (with feedback), Escalate
    4. **Balance**: Too many checkpoints = slow, too few = risky

    When to use HITL:
    - High-stakes decisions (medical, legal, financial)
    - Irreversible actions (delete, deploy, send)
    - Low confidence (agent uncertain)
    - Regulatory requirements (compliance mandates)
    - Trust building (user wants oversight)

    Design considerations:
    - Where to place checkpoints? (before irreversible actions)
    - Who reviews? (domain experts, stakeholders)
    - What if human unavailable? (timeout, escalation)
    - How to present for review? (summary, full output, highlights)

    Cost-benefit:
    - Cost: Human time, workflow latency
    - Benefit: Risk reduction, quality improvement, compliance

    Real-world applications:
    - Legal document generation (lawyer review)
    - Medical diagnosis assistance (doctor review)
    - Financial transactions (approver review)
    - Code deployment (human final check)
    - Content moderation (human review of edge cases)

    Synergy with other patterns:
    - Reflection + HITL: Agent self-reviews before human review
    - Planning + HITL: Human approves plan before execution
    - Tool Use + HITL: Human approves before tool execution
    """
