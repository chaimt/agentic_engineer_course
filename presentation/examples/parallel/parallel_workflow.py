"""
Parallel Workflow Pattern (Parallelization)

This example demonstrates how to execute independent subtasks concurrently
and aggregate the results.

Based on Phil Schmid's workflow pattern taxonomy.
"""

from typing import List, Dict, Any
import anthropic
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed


class ParallelWorkflow:
    """
    Implements parallelization - concurrent execution of independent subtasks.

    Pattern: Split → [Task1 || Task2 || Task3] → Aggregate
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def execute_subtask(self, task_prompt: str, task_name: str) -> Dict[str, str]:
        """Execute a single subtask"""
        print(f"  → Executing: {task_name}")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": task_prompt}]
        )

        result = response.content[0].text
        print(f"  ✓ Completed: {task_name}")

        return {
            "task_name": task_name,
            "result": result
        }

    def aggregate_results(self, results: List[Dict[str, str]], context: str) -> str:
        """Aggregate parallel results into final output"""
        print("\nAggregating results...")

        # Combine all results
        combined = "\n\n".join([
            f"**{r['task_name']}**:\n{r['result']}"
            for r in results
        ])

        # Final synthesis
        aggregate_prompt = f"""Given these parallel analysis results for: "{context}"

{combined}

Synthesize a comprehensive final answer that incorporates insights from all analyses.
Provide a cohesive response that highlights the most important points."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": aggregate_prompt}]
        )

        return response.content[0].text

    def execute_parallel(
        self,
        subtasks: List[Dict[str, str]],
        context: str,
        max_workers: int = 3
    ) -> Dict[str, Any]:
        """
        Execute subtasks in parallel using ThreadPoolExecutor.

        Args:
            subtasks: List of {name, prompt} dicts
            context: Context for aggregation
            max_workers: Maximum concurrent executions

        Returns: Dictionary with individual results and aggregated output
        """
        print("Starting Parallel Workflow")
        print("=" * 60)
        print(f"Executing {len(subtasks)} subtasks in parallel...")

        results = []

        # Execute subtasks concurrently
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_task = {
                executor.submit(
                    self.execute_subtask,
                    task['prompt'],
                    task['name']
                ): task
                for task in subtasks
            }

            # Collect results as they complete
            for future in as_completed(future_to_task):
                result = future.result()
                results.append(result)

        # Aggregate results
        final_output = self.aggregate_results(results, context)

        print("\n" + "=" * 60)
        print("Parallel Workflow Complete!")

        return {
            "subtask_count": len(subtasks),
            "individual_results": results,
            "aggregated_output": final_output
        }


class ParallelRAG:
    """
    Example: Parallel RAG with query decomposition.

    Demonstrates a common use case for parallelization.
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def decompose_query(self, complex_query: str) -> List[str]:
        """Break complex query into simpler sub-queries"""
        prompt = f"""Break this complex question into 3 simpler, independent sub-questions
that can be answered separately:

Question: {complex_query}

Provide only the 3 sub-questions, one per line, numbered."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse sub-queries (simplified)
        sub_queries = [
            line.strip().split('. ', 1)[1] if '. ' in line else line.strip()
            for line in response.content[0].text.split('\n')
            if line.strip() and any(c.isdigit() for c in line[:3])
        ]

        return sub_queries[:3]

    def search_documents(self, query: str) -> str:
        """Simulate document search (in real system, this would query a vector DB)"""
        # In a real implementation, this would:
        # 1. Embed the query
        # 2. Search vector database
        # 3. Return relevant passages

        # For demo, we simulate with an LLM
        prompt = f"""Provide a brief answer (2-3 sentences) to this question:

{query}

Answer based on general knowledge."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def parallel_search_and_aggregate(self, complex_query: str) -> str:
        """Execute parallel RAG workflow"""
        print(f"Query: {complex_query}\n")

        # Step 1: Decompose
        print("Step 1: Decomposing query...")
        sub_queries = self.decompose_query(complex_query)
        for i, sq in enumerate(sub_queries, 1):
            print(f"  {i}. {sq}")

        # Step 2: Parallel search
        print("\nStep 2: Executing parallel searches...")
        results = []

        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_query = {
                executor.submit(self.search_documents, query): query
                for query in sub_queries
            }

            for future in as_completed(future_to_query):
                query = future_to_query[future]
                result = future.result()
                results.append({"query": query, "answer": result})
                print(f"  ✓ Completed: {query[:50]}...")

        # Step 3: Aggregate
        print("\nStep 3: Aggregating results...")
        combined = "\n\n".join([
            f"Q: {r['query']}\nA: {r['answer']}"
            for r in results
        ])

        aggregate_prompt = f"""Given these sub-question answers for the complex question:
"{complex_query}"

{combined}

Synthesize a comprehensive answer to the original complex question."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": aggregate_prompt}]
        )

        return response.content[0].text


# Example usage
if __name__ == "__main__":
    # Example 1: General parallel workflow
    workflow = ParallelWorkflow(api_key="your-api-key")

    # Define parallel subtasks analyzing different aspects
    subtasks = [
        {
            "name": "Technical Analysis",
            "prompt": """Analyze the technical feasibility of building an AI-powered
code review system. Focus on: architecture, scalability, tech stack."""
        },
        {
            "name": "Business Analysis",
            "prompt": """Analyze the business viability of an AI-powered code review
system. Focus on: market demand, monetization, competition."""
        },
        {
            "name": "UX Analysis",
            "prompt": """Analyze the user experience requirements for an AI-powered
code review system. Focus on: workflows, integrations, feedback loops."""
        }
    ]

    result = workflow.execute_parallel(
        subtasks,
        context="AI-powered code review system",
        max_workers=3
    )

    print("\n" + "=" * 60)
    print("FINAL AGGREGATED OUTPUT:")
    print("=" * 60)
    print(result["aggregated_output"])

    # Example 2: Parallel RAG
    print("\n\n" + "=" * 60)
    print("PARALLEL RAG EXAMPLE")
    print("=" * 60)

    rag = ParallelRAG(api_key="your-api-key")

    complex_question = """
    How do agentic workflows improve software development productivity,
    what are the key implementation challenges, and what tools are available?
    """

    final_answer = rag.parallel_search_and_aggregate(complex_question)

    print("\n" + "=" * 60)
    print("FINAL ANSWER:")
    print("=" * 60)
    print(final_answer)

    """
    Key Insights:

    1. **Independence Requirement**: Subtasks must not depend on each other
    2. **Latency Improvement**: N tasks in parallel ≈ 1 task's time (vs N×time sequential)
    3. **Quality Enhancement**: Diverse parallel approaches provide broader coverage
    4. **Scalability**: Add more workers as needed (respecting API rate limits)
    5. **Map-Reduce Pattern**: Split → Process → Aggregate

    When to use Parallel Workflow:
    - Subtasks are independent (no data dependencies)
    - Want to reduce latency
    - Benefit from diverse perspectives
    - Have sufficient compute resources

    When NOT to use:
    - Tasks have sequential dependencies (use Sequential instead)
    - Single task is sufficient
    - Rate limits prevent parallelization
    - Aggregation step negates latency benefits

    Performance considerations:
    - ThreadPoolExecutor for I/O-bound LLM calls
    - ProcessPoolExecutor for CPU-bound tasks
    - Watch API rate limits (max_workers should respect them)
    - Aggregation adds latency but improves quality
    """
