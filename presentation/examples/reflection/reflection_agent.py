"""
Reflection Pattern Example - Self-Improving Code Generator

This example demonstrates how an agent can generate code, critique it,
and iteratively improve the output through self-reflection.
"""

from typing import Dict, List
import anthropic


class ReflectionAgent:
    """
    Agent that uses reflection to improve its own outputs.

    Pattern: Generate → Critique → Refine → Repeat
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
        self.max_iterations = 3

    def generate_initial_code(self, task: str) -> str:
        """Generate initial code solution"""
        prompt = f"""Write a Python function to {task}.

        Requirements:
        - Include docstring
        - Add type hints
        - Handle edge cases
        - Follow PEP 8
        """

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def critique_code(self, code: str) -> Dict[str, List[str]]:
        """Agent reviews its own code and identifies improvements"""
        critique_prompt = f"""Review this code and identify specific improvements:

```python
{code}
```

Evaluate:
1. Code quality and readability
2. Edge case handling
3. Performance considerations
4. Documentation clarity
5. Security issues

Provide specific, actionable feedback."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": critique_prompt}]
        )

        # Parse critique (simplified for example)
        critique_text = response.content[0].text
        return {"feedback": [critique_text]}

    def refine_code(self, code: str, critique: Dict[str, List[str]]) -> str:
        """Apply critique to improve code"""
        refine_prompt = f"""Improve this code based on the following critique:

**Original Code:**
```python
{code}
```

**Critique:**
{critique['feedback'][0]}

Provide the refined version that addresses all feedback."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": refine_prompt}]
        )

        return response.content[0].text

    def generate_with_reflection(self, task: str) -> str:
        """
        Main workflow: Generate, critique, refine iteratively

        Returns: Final refined code after reflection cycles
        """
        print(f"Task: {task}\n")

        # Initial generation
        print("Step 1: Generating initial code...")
        code = self.generate_initial_code(task)
        print(f"Generated:\n{code[:200]}...\n")

        # Reflection loop
        for iteration in range(self.max_iterations):
            print(f"Reflection Cycle {iteration + 1}/{self.max_iterations}")

            # Critique
            print("  - Critiquing code...")
            critique = self.critique_code(code)
            print(f"  - Found {len(critique['feedback'])} areas for improvement")

            # Refine
            print("  - Refining code...")
            improved_code = self.refine_code(code, critique)

            # Check if improvement occurred (simplified check)
            if len(improved_code) > len(code):
                code = improved_code
                print("  - Code improved ✓\n")
            else:
                print("  - No further improvements needed\n")
                break

        print("Final code generated after reflection cycles")
        return code


# Example usage
if __name__ == "__main__":
    # Initialize agent
    agent = ReflectionAgent(api_key="your-api-key")

    # Task: Generate a function with reflection
    task = "validate email addresses with comprehensive edge case handling"

    # Generate with self-reflection
    final_code = agent.generate_with_reflection(task)

    print("\n" + "="*60)
    print("FINAL OUTPUT:")
    print("="*60)
    print(final_code)

    """
    Expected output demonstrates:
    1. Initial code generation (may have issues)
    2. Self-critique identifying problems
    3. Iterative refinement improving quality
    4. Final production-ready code

    Key insight: The agent improves its own work without human intervention.
    """
