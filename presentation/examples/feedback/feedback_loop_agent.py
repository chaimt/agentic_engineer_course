"""
Feedback Loop Pattern

This example demonstrates iterative refinement through evaluation
and feedback incorporation.

Key principle: If you can evaluate output, you can iteratively improve it.
"""

from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass
import anthropic


@dataclass
class EvaluationResult:
    """Result from evaluating agent output"""
    score: float  # 0.0 to 1.0
    passed: bool  # True if meets threshold
    feedback: str  # Specific improvement suggestions
    issues: List[str]  # Specific problems found


class FeedbackLoopAgent:
    """
    Agent that iteratively refines output based on feedback.

    Core loop:
    1. Generate output
    2. Evaluate quality
    3. Generate feedback
    4. Refine output
    5. Repeat until quality threshold met
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def generate_output(self, task: str, previous_attempt: Optional[str] = None, feedback: Optional[str] = None) -> str:
        """Generate or refine output"""
        if previous_attempt is None:
            # Initial generation
            print(f"\n[AGENT] Generating initial output...")
            prompt = f"Complete this task:\n\n{task}"
        else:
            # Refinement based on feedback
            print(f"\n[AGENT] Refining output based on feedback...")
            prompt = f"""Previous attempt:
{previous_attempt}

Feedback:
{feedback}

Improve the output by addressing the feedback. Keep what was good, fix the issues."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.content[0].text
        print(f"[AGENT] Output generated ({len(output)} chars)")

        return output

    def evaluate_output(self, output: str, criteria: str, evaluation_fn: Optional[Callable[[str], EvaluationResult]] = None) -> EvaluationResult:
        """
        Evaluate output quality.

        Can use LLM-based evaluation or custom evaluation function.
        """
        if evaluation_fn:
            # Custom evaluation logic
            return evaluation_fn(output)

        # LLM-based evaluation
        print(f"\n[EVALUATOR] Evaluating output...")

        prompt = f"""Evaluate this output against criteria:

Output:
{output}

Criteria:
{criteria}

Provide:
1. Score (0.0 to 1.0)
2. Pass/Fail (threshold: 0.8)
3. Specific feedback for improvement
4. List of issues found

Format:
SCORE: <0.0-1.0>
PASSED: <true/false>
FEEDBACK: <specific suggestions>
ISSUES:
- <issue 1>
- <issue 2>
..."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        evaluation_text = response.content[0].text

        # Parse evaluation (simplified - production would use structured output)
        score = 0.7  # Default
        passed = False
        feedback = ""
        issues = []

        for line in evaluation_text.split('\n'):
            if line.startswith('SCORE:'):
                try:
                    score = float(line.split(':')[1].strip())
                except:
                    pass
            elif line.startswith('PASSED:'):
                passed = 'true' in line.lower()
            elif line.startswith('FEEDBACK:'):
                feedback = line.split(':', 1)[1].strip()
            elif line.startswith('- '):
                issues.append(line[2:].strip())

        result = EvaluationResult(score, passed, feedback, issues)

        print(f"[EVALUATOR] Score: {result.score:.2f}, Passed: {result.passed}")
        if result.issues:
            print(f"[EVALUATOR] Issues found: {len(result.issues)}")

        return result

    def execute_feedback_loop(
        self,
        task: str,
        criteria: str,
        max_iterations: int = 5,
        quality_threshold: float = 0.8,
        evaluation_fn: Optional[Callable[[str], EvaluationResult]] = None
    ) -> Dict[str, Any]:
        """
        Execute complete feedback loop workflow.

        Returns:
            Final output with iteration history
        """
        print(f"\n{'='*60}")
        print(f"Feedback Loop: {task[:60]}...")
        print(f"Quality Threshold: {quality_threshold}")
        print(f"Max Iterations: {max_iterations}")
        print(f"{'='*60}")

        history = []
        current_output = None
        current_feedback = None

        for iteration in range(max_iterations):
            print(f"\n{'='*60}")
            print(f"ITERATION {iteration + 1}")
            print(f"{'='*60}")

            # Generate/refine output
            current_output = self.generate_output(task, current_output, current_feedback)

            # Evaluate
            evaluation = self.evaluate_output(current_output, criteria, evaluation_fn)

            # Record iteration
            history.append({
                "iteration": iteration + 1,
                "output": current_output,
                "score": evaluation.score,
                "passed": evaluation.passed,
                "feedback": evaluation.feedback,
                "issues": evaluation.issues
            })

            # Check convergence
            if evaluation.passed and evaluation.score >= quality_threshold:
                print(f"\n[SYSTEM] ✅ Quality threshold met! (Score: {evaluation.score:.2f})")
                return {
                    "status": "success",
                    "iterations": iteration + 1,
                    "final_output": current_output,
                    "final_score": evaluation.score,
                    "history": history
                }

            # Prepare feedback for next iteration
            current_feedback = evaluation.feedback

            print(f"[SYSTEM] Quality not met (Score: {evaluation.score:.2f}), iterating...")

        print(f"\n[SYSTEM] ⚠️ Max iterations reached without meeting threshold")
        return {
            "status": "max_iterations",
            "iterations": max_iterations,
            "final_output": current_output,
            "final_score": history[-1]["score"] if history else 0.0,
            "history": history
        }


class CodeGenerationWithTests:
    """
    Example: Code generation with test-driven feedback loop.

    Generate → Test → Fix → Repeat until tests pass.
    """

    def __init__(self, api_key: str):
        self.agent = FeedbackLoopAgent(api_key)

    def evaluate_code(self, code: str) -> EvaluationResult:
        """Simulate running tests on generated code"""
        # In real system, would actually run tests
        # For demo, simple heuristic checks

        issues = []
        score = 1.0

        # Check for basic code quality indicators
        if "def " not in code and "function" not in code:
            issues.append("No function definition found")
            score -= 0.3

        if "return" not in code:
            issues.append("No return statement found")
            score -= 0.2

        if len(code) < 50:
            issues.append("Implementation too brief")
            score -= 0.3

        passed = len(issues) == 0
        feedback = "; ".join(issues) if issues else "All checks passed"

        return EvaluationResult(score, passed, feedback, issues)

    def generate_with_tests(self, task: str) -> Dict[str, Any]:
        """Generate code with test-driven feedback loop"""
        criteria = """
Code must:
1. Define the requested function
2. Include proper return statement
3. Be complete and functional
4. Handle edge cases
"""

        return self.agent.execute_feedback_loop(
            task,
            criteria,
            max_iterations=5,
            quality_threshold=0.9,
            evaluation_fn=self.evaluate_code
        )


class ContentRefinement:
    """
    Example: Content creation with quality feedback loop.

    Draft → Critique → Revise → Repeat until quality standards met.
    """

    def __init__(self, api_key: str):
        self.agent = FeedbackLoopAgent(api_key)

    def execute_content_loop(self, task: str) -> Dict[str, Any]:
        """Create content with iterative refinement"""
        criteria = """
Content must:
1. Be clear and well-structured
2. Address the topic comprehensively
3. Use professional tone
4. Include concrete examples
5. Be engaging and accessible
"""

        return self.agent.execute_feedback_loop(
            task,
            criteria,
            max_iterations=4,
            quality_threshold=0.85
        )


class OptimizationLoop:
    """
    Example: Solution optimization through iterative improvement.

    Propose → Evaluate → Improve → Repeat until optimal.
    """

    def __init__(self, api_key: str):
        self.agent = FeedbackLoopAgent(api_key)

    def evaluate_solution(self, solution: str) -> EvaluationResult:
        """Evaluate solution against optimization criteria"""
        # Simplified evaluation
        # Real system would measure actual performance metrics

        issues = []
        score = 0.7

        # Check for optimization indicators
        if "time complexity" in solution.lower():
            score += 0.1

        if "space complexity" in solution.lower():
            score += 0.1

        if "optimization" not in solution.lower():
            issues.append("No explicit optimization discussion")
            score -= 0.1

        if len(solution) < 100:
            issues.append("Solution lacks detail")
            score -= 0.2

        passed = score >= 0.85 and len(issues) == 0
        feedback = "; ".join(issues) if issues else "Solution meets optimization criteria"

        return EvaluationResult(score, passed, feedback, issues)

    def optimize_solution(self, task: str) -> Dict[str, Any]:
        """Optimize solution through feedback loop"""
        criteria = """
Solution must:
1. Be optimal in time complexity
2. Be optimal in space complexity
3. Explain optimization approach
4. Consider trade-offs
5. Provide complexity analysis
"""

        return self.agent.execute_feedback_loop(
            task,
            criteria,
            max_iterations=5,
            quality_threshold=0.85,
            evaluation_fn=self.evaluate_solution
        )


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    print("="*60)
    print("EXAMPLE 1: Code Generation with Test Feedback")
    print("="*60)

    code_gen = CodeGenerationWithTests(api_key)

    task = "Write a Python function that calculates the nth Fibonacci number"
    result = code_gen.generate_with_tests(task)

    print(f"\n{'='*60}")
    print(f"FINAL RESULT:")
    print(f"Status: {result['status']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final Score: {result['final_score']:.2f}")
    print(f"\nFinal Code:\n{result['final_output'][:300]}...")
    print(f"{'='*60}\n")

    # Example 2: Content Refinement
    print("\n\n" + "="*60)
    print("EXAMPLE 2: Content Refinement Loop")
    print("="*60)

    content = ContentRefinement(api_key)

    task = "Explain the benefits of test-driven development to a junior developer"
    result = content.execute_content_loop(task)

    print(f"\n{'='*60}")
    print(f"FINAL RESULT:")
    print(f"Status: {result['status']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final Score: {result['final_score']:.2f}")
    print(f"\nQuality progression:")
    for h in result['history']:
        print(f"  Iteration {h['iteration']}: {h['score']:.2f}")
    print(f"{'='*60}\n")

    # Example 3: Optimization Loop
    print("\n\n" + "="*60)
    print("EXAMPLE 3: Solution Optimization Loop")
    print("="*60)

    optimizer = OptimizationLoop(api_key)

    task = "Design an algorithm to find duplicates in an array"
    result = optimizer.optimize_solution(task)

    print(f"\n{'='*60}")
    print(f"FINAL RESULT:")
    print(f"Status: {result['status']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final Score: {result['final_score']:.2f}")
    print(f"{'='*60}\n")

    """
    Key Insights:

    1. **Core Loop**: Generate → Evaluate → Feedback → Refine → Repeat
    2. **Convergence Criteria**:
       - Quality threshold (score >= target)
       - Max iterations (prevent infinite loops)
       - Improvement plateau (score not improving)
    3. **Evaluation Sources**:
       - Automated tests (code correctness)
       - Quality metrics (content, performance)
       - LLM-based critique (subjective quality)
       - User feedback (actual usage)

    When to use Feedback Loop:
    - Output quality is measurable
    - Iterative refinement is beneficial
    - First attempt rarely optimal
    - Cost of iteration < cost of poor quality

    Design considerations:
    - Evaluation function quality (garbage in = garbage out)
    - Convergence criteria (when to stop)
    - Cost-benefit (each iteration costs tokens/time)
    - Feedback specificity (vague feedback = poor refinement)

    Feedback Loop vs Reflection:
    - Feedback Loop: External evaluation or metrics
    - Reflection: Self-evaluation (agent critiques own work)
    - Synergy: Reflection can be the evaluation step in feedback loop

    Cost management:
    - Early stopping if score improving too slowly
    - Caching intermediate results
    - Progressive evaluation (cheap checks first, expensive later)

    Real-world applications:
    - Code generation (write → test → fix)
    - Content creation (draft → critique → revise)
    - Design optimization (propose → measure → improve)
    - Conversation (respond → assess quality → refine)
    - ML hyperparameter tuning (try → evaluate → adjust)

    Performance benefits:
    - Quality: Iterative refinement improves output
    - Automation: Reduces manual interventions
    - Adaptability: Learns from mistakes within session

    Anti-patterns:
    - Infinite loops (no max iterations)
    - Vague feedback (agent can't act on it)
    - Poor evaluation (misleading quality signals)
    - Excessive iterations (diminishing returns)
    """
