"""
Multi-Agent Collaboration Pattern

This example demonstrates how multiple specialized agents work together
with distinct roles and expertise.

Based on Phil Schmid's agentic pattern taxonomy.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import anthropic


class AgentRole(Enum):
    """Possible agent roles in the system"""
    COORDINATOR = "coordinator"
    RESEARCHER = "researcher"
    WRITER = "writer"
    REVIEWER = "reviewer"


@dataclass
class Message:
    """Message passed between agents"""
    from_agent: str
    to_agent: str
    content: str
    context: Dict[str, Any]


class BaseAgent:
    """Base class for all agents"""

    def __init__(self, name: str, role: AgentRole, api_key: str):
        self.name = name
        self.role = role
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
        self.message_history: List[Message] = []

    def receive_message(self, message: Message):
        """Receive a message from another agent"""
        self.message_history.append(message)
        print(f"\n[{self.name}] Received message from {message.from_agent}")
        print(f"  Content: {message.content[:100]}...")

    def send_message(self, to_agent: str, content: str, context: Dict[str, Any]) -> Message:
        """Send a message to another agent"""
        message = Message(
            from_agent=self.name,
            to_agent=to_agent,
            content=content,
            context=context
        )
        print(f"\n[{self.name}] Sending message to {to_agent}")
        return message

    def execute_task(self, task: str, context: Dict[str, Any]) -> str:
        """Execute agent's specialized task"""
        raise NotImplementedError("Subclasses must implement execute_task")


class ResearcherAgent(BaseAgent):
    """Agent specialized in research and information gathering"""

    def __init__(self, api_key: str):
        super().__init__("Researcher", AgentRole.RESEARCHER, api_key)

    def execute_task(self, task: str, context: Dict[str, Any]) -> str:
        """Research and gather information"""
        print(f"\n[{self.name}] Researching: {task}")

        prompt = f"""As a research specialist, gather key information about: {task}

Provide:
1. Core concepts and definitions
2. Current state of the field
3. Key challenges and opportunities
4. 3-4 important facts or statistics

Context: {context}

Keep response concise (200-300 words)."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text
        print(f"[{self.name}] Research complete")
        return result


class WriterAgent(BaseAgent):
    """Agent specialized in content creation"""

    def __init__(self, api_key: str):
        super().__init__("Writer", AgentRole.WRITER, api_key)

    def execute_task(self, task: str, context: Dict[str, Any]) -> str:
        """Create content based on research"""
        print(f"\n[{self.name}] Writing: {task}")

        research = context.get("research", "")

        prompt = f"""As a content writer, create engaging content about: {task}

Use this research:
{research}

Requirements:
- Clear, accessible writing
- Engaging introduction
- Well-structured body
- Practical takeaways
- 300-400 words

Create the content now."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=768,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text
        print(f"[{self.name}] Writing complete")
        return result


class ReviewerAgent(BaseAgent):
    """Agent specialized in review and quality assurance"""

    def __init__(self, api_key: str):
        super().__init__("Reviewer", AgentRole.REVIEWER, api_key)

    def execute_task(self, task: str, context: Dict[str, Any]) -> str:
        """Review content for quality"""
        print(f"\n[{self.name}] Reviewing: {task}")

        content = context.get("content", "")

        prompt = f"""As a content reviewer, evaluate this content:

{content}

Provide:
1. Overall quality assessment (1-10)
2. Strengths (2-3 points)
3. Areas for improvement (2-3 points)
4. Specific suggestions

Be constructive and specific."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text
        print(f"[{self.name}] Review complete")
        return result


class CoordinatorAgent(BaseAgent):
    """Agent that orchestrates multi-agent workflows"""

    def __init__(self, api_key: str):
        super().__init__("Coordinator", AgentRole.COORDINATOR, api_key)
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        """Register a specialized agent"""
        self.agents[agent.name] = agent
        print(f"[{self.name}] Registered agent: {agent.name} ({agent.role.value})")

    def execute_workflow(self, goal: str) -> Dict[str, Any]:
        """
        Execute a multi-agent collaborative workflow

        Returns: Dictionary with outputs from each agent
        """
        print(f"\n{'='*60}")
        print(f"[{self.name}] Starting multi-agent workflow")
        print(f"Goal: {goal}")
        print(f"{'='*60}")

        results = {}

        # Step 1: Research phase
        if "Researcher" in self.agents:
            research_result = self.agents["Researcher"].execute_task(
                goal,
                {"goal": goal}
            )
            results["research"] = research_result

        # Step 2: Writing phase (uses research)
        if "Writer" in self.agents:
            writing_result = self.agents["Writer"].execute_task(
                goal,
                {"goal": goal, "research": results.get("research", "")}
            )
            results["content"] = writing_result

        # Step 3: Review phase (evaluates writing)
        if "Reviewer" in self.agents:
            review_result = self.agents["Reviewer"].execute_task(
                goal,
                {"goal": goal, "content": results.get("content", "")}
            )
            results["review"] = review_result

        print(f"\n{'='*60}")
        print(f"[{self.name}] Multi-agent workflow complete")
        print(f"{'='*60}")

        return results

    def execute_task(self, task: str, context: Dict[str, Any]) -> str:
        """Coordinator's task execution delegates to workflow"""
        workflow_result = self.execute_workflow(task)
        return workflow_result.get("content", "")


class HandoffCoordinator:
    """
    Alternative coordination pattern: Agent-to-agent handoff

    Instead of central orchestrator, agents hand off directly to each other.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        """Register an agent"""
        self.agents[agent.name] = agent

    def execute_handoff_workflow(self, initial_task: str) -> Dict[str, Any]:
        """Execute workflow with agent-to-agent handoff"""
        print(f"\n{'='*60}")
        print(f"Handoff Workflow: {initial_task}")
        print(f"{'='*60}")

        results = {}
        current_agent = "Researcher"
        current_task = initial_task
        context = {"goal": initial_task}

        # Researcher → Writer → Reviewer (sequential handoff)
        workflow = ["Researcher", "Writer", "Reviewer"]

        for agent_name in workflow:
            if agent_name not in self.agents:
                continue

            agent = self.agents[agent_name]

            # Execute task
            result = agent.execute_task(current_task, context)
            results[agent_name.lower()] = result

            # Update context for next agent
            if agent_name == "Researcher":
                context["research"] = result
            elif agent_name == "Writer":
                context["content"] = result

            # Handoff message (if not last agent)
            if agent_name != workflow[-1]:
                next_agent = workflow[workflow.index(agent_name) + 1]
                message = agent.send_message(
                    next_agent,
                    f"Completed {agent_name.lower()} phase",
                    context
                )
                self.agents[next_agent].receive_message(message)

        print(f"\n{'='*60}")
        print(f"Handoff Workflow Complete")
        print(f"{'='*60}")

        return results


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    print("="*60)
    print("EXAMPLE 1: Central Coordinator Pattern")
    print("="*60)

    # Create specialized agents
    researcher = ResearcherAgent(api_key)
    writer = WriterAgent(api_key)
    reviewer = ReviewerAgent(api_key)

    # Create coordinator
    coordinator = CoordinatorAgent(api_key)
    coordinator.register_agent(researcher)
    coordinator.register_agent(writer)
    coordinator.register_agent(reviewer)

    # Execute workflow
    goal = "Agentic workflow patterns in software development"
    results = coordinator.execute_workflow(goal)

    print("\n" + "="*60)
    print("FINAL OUTPUTS:")
    print("="*60)
    print(f"\nResearch:\n{results['research'][:200]}...\n")
    print(f"\nContent:\n{results['content'][:200]}...\n")
    print(f"\nReview:\n{results['review'][:200]}...\n")

    # Example 2: Handoff pattern
    print("\n\n" + "="*60)
    print("EXAMPLE 2: Agent-to-Agent Handoff Pattern")
    print("="*60)

    handoff = HandoffCoordinator(api_key)
    handoff.register_agent(ResearcherAgent(api_key))
    handoff.register_agent(WriterAgent(api_key))
    handoff.register_agent(ReviewerAgent(api_key))

    results2 = handoff.execute_handoff_workflow(goal)

    print("\n" + "="*60)
    print("HANDOFF RESULTS:")
    print("="*60)
    for role, output in results2.items():
        print(f"\n{role.upper()}:\n{output[:150]}...\n")

    """
    Key Insights:

    1. **Specialization**: Each agent has unique role and expertise
    2. **Autonomy**: Agents work independently within their domain
    3. **Collaboration**: Agents communicate via messages or shared context
    4. **Coordination Patterns**:
       - Central Orchestrator: Coordinator manages all agents
       - Handoff: Agents pass work directly to each other
    5. **Scalability**: Easy to add new specialized agents

    When to use Multi-Agent:
    - Task requires diverse expertise
    - Benefit from specialized handling
    - Want to mimic team dynamics
    - Can parallelize some work

    Design considerations:
    - How do agents communicate? (Messages vs shared state)
    - Who coordinates? (Central vs distributed)
    - How to handle failures? (Retry, escalate, skip)
    - How to resolve conflicts? (Priority, voting, human)

    Real-world applications:
    - Software development teams (PM, dev, QA, ops)
    - Content creation pipelines (research, write, edit, publish)
    - Customer service (triage, billing, technical, escalation)
    - Data analysis (collect, clean, analyze, visualize)
    """
