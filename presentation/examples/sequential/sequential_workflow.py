"""
Sequential Workflow Pattern (Prompt Chaining)

This example demonstrates how to chain multiple LLM calls where each
step's output feeds into the next step's input.

Based on Phil Schmid's workflow pattern taxonomy.
"""

from typing import List, Dict, Any
import anthropic


class SequentialWorkflow:
    """
    Implements prompt chaining - sequential LLM calls in a pipeline.

    Pattern: Step1 → Step2 → Step3 → ... → Final Output
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def step1_summarize(self, text: str) -> str:
        """Step 1: Summarize the input text"""
        prompt = f"""Summarize the following text in 2-3 sentences:

{text}

Provide only the summary, no preamble."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def step2_translate(self, summary: str, target_language: str = "French") -> str:
        """Step 2: Translate the summary"""
        prompt = f"""Translate the following text to {target_language}:

{summary}

Provide only the translation, no preamble."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def step3_format_markdown(self, translated_text: str) -> str:
        """Step 3: Format as markdown with proper structure"""
        prompt = f"""Format the following text as a markdown document with:
- A level 2 heading
- The text as a paragraph
- A horizontal rule at the end

Text to format:
{translated_text}

Provide only the markdown, no explanation."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def execute_chain(self, input_text: str, target_language: str = "French") -> Dict[str, str]:
        """
        Execute the complete sequential workflow (prompt chain).

        Returns: Dictionary with outputs from each step
        """
        print("Starting Sequential Workflow (Prompt Chain)")
        print("=" * 60)

        # Step 1: Summarize
        print("\nStep 1: Summarizing input text...")
        summary = self.step1_summarize(input_text)
        print(f"Summary: {summary[:100]}...")

        # Step 2: Translate
        print(f"\nStep 2: Translating to {target_language}...")
        translation = self.step2_translate(summary, target_language)
        print(f"Translation: {translation[:100]}...")

        # Step 3: Format
        print("\nStep 3: Formatting as Markdown...")
        formatted = self.step3_format_markdown(translation)
        print(f"Formatted:\n{formatted}")

        print("\n" + "=" * 60)
        print("Sequential Workflow Complete!")

        return {
            "input": input_text,
            "step1_summary": summary,
            "step2_translation": translation,
            "step3_formatted": formatted
        }


class ConfigurableChain:
    """
    More flexible sequential workflow with configurable steps.

    Demonstrates how to build reusable, composable chains.
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def execute_step(self, prompt: str) -> str:
        """Execute a single LLM step"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    def execute_chain(self, steps: List[Dict[str, Any]], initial_input: str) -> List[str]:
        """
        Execute a configurable chain of steps.

        Args:
            steps: List of step definitions
            initial_input: Starting input

        Returns: List of outputs from each step
        """
        outputs = []
        current_input = initial_input

        for i, step in enumerate(steps):
            print(f"\nStep {i+1}: {step['name']}")

            # Format prompt with current input
            prompt = step['prompt_template'].format(input=current_input)

            # Execute step
            output = self.execute_step(prompt)
            outputs.append(output)

            print(f"Output: {output[:100]}...")

            # Output becomes input for next step
            current_input = output

        return outputs


# Example usage
if __name__ == "__main__":
    # Example 1: Fixed pipeline
    workflow = SequentialWorkflow(api_key="your-api-key")

    input_text = """
    Agentic workflows represent a paradigm shift in software development. By combining
    large language models with tool use capabilities and autonomous decision-making,
    agents can execute complex multi-step tasks without constant human intervention.
    This enables developers to focus on high-level design and review rather than
    low-level implementation details.
    """

    result = workflow.execute_chain(input_text, target_language="French")

    print("\n" + "="*60)
    print("FINAL RESULT:")
    print("="*60)
    print(result["step3_formatted"])

    # Example 2: Configurable pipeline
    print("\n\n" + "="*60)
    print("CONFIGURABLE CHAIN EXAMPLE")
    print("="*60)

    configurable = ConfigurableChain(api_key="your-api-key")

    # Define custom pipeline steps
    custom_steps = [
        {
            "name": "Extract Key Points",
            "prompt_template": "Extract 3 key points from this text:\n\n{input}"
        },
        {
            "name": "Generate Questions",
            "prompt_template": "Generate 2 questions about these key points:\n\n{input}"
        },
        {
            "name": "Answer Questions",
            "prompt_template": "Answer these questions concisely:\n\n{input}"
        }
    ]

    outputs = configurable.execute_chain(custom_steps, input_text)

    print("\n" + "="*60)
    print("CHAIN OUTPUTS:")
    for i, output in enumerate(outputs):
        print(f"\nStep {i+1} Output:")
        print(output)

    """
    Key Insights:

    1. **Sequential Execution**: Each step completes before the next begins
    2. **Data Transformation**: Each step transforms input to output
    3. **Composability**: Steps can be reused in different chains
    4. **Predictability**: Fixed sequence, no branching logic
    5. **Debuggability**: Easy to inspect intermediate outputs

    When to use Sequential Workflow:
    - Well-defined transformation steps
    - No conditional logic needed
    - Steps must execute in specific order
    - Want to inspect intermediate results

    When NOT to use:
    - Need branching/routing based on content
    - Steps have no dependencies (use Parallel instead)
    - Need autonomous decision-making (use Agentic patterns)
    """
