"""
Routing Pattern (Intelligent Handoff)

This example demonstrates how to classify requests and route them
to specialized handlers.

Based on Phil Schmid's workflow pattern taxonomy.
"""

from typing import Dict, Any, Optional
from enum import Enum
import anthropic


class RequestCategory(Enum):
    """Request categories for routing"""
    TECHNICAL = "technical"
    BILLING = "billing"
    PRODUCT = "product"
    GENERAL = "general"


class RouterAgent:
    """
    Classifier that analyzes requests and routes to appropriate handlers.

    Phil Schmid: "An initial LLM classifies user input and directs it
    to specialized downstream handlers based on category"
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def classify_request(self, request: str) -> RequestCategory:
        """Classify the incoming request"""
        print(f"\n[ROUTER] Classifying request...")

        prompt = f"""Classify this customer support request into ONE category:

Request: {request}

Categories:
- technical: Login issues, bugs, system problems
- billing: Payments, invoices, refunds
- product: Features, how-to questions, capabilities
- general: Everything else

Respond with ONLY the category name (technical, billing, product, or general)."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        classification = response.content[0].text.strip().lower()

        # Map to enum
        category_map = {
            "technical": RequestCategory.TECHNICAL,
            "billing": RequestCategory.BILLING,
            "product": RequestCategory.PRODUCT,
            "general": RequestCategory.GENERAL
        }

        category = category_map.get(classification, RequestCategory.GENERAL)
        print(f"[ROUTER] Classified as: {category.value}")

        return category

    def route(self, request: str) -> Dict[str, Any]:
        """
        Complete routing workflow: Classify → Route → Handle

        Returns: Routing decision and handler assignment
        """
        category = self.classify_request(request)

        handler = self._select_handler(category)

        return {
            "request": request,
            "category": category.value,
            "handler": handler,
            "routing_reason": self._get_routing_reason(category)
        }

    def _select_handler(self, category: RequestCategory) -> str:
        """Select appropriate handler based on category"""
        handler_map = {
            RequestCategory.TECHNICAL: "Technical Support Specialist",
            RequestCategory.BILLING: "Billing Department Agent",
            RequestCategory.PRODUCT: "Product Expert",
            RequestCategory.GENERAL: "General Support Agent"
        }
        return handler_map[category]

    def _get_routing_reason(self, category: RequestCategory) -> str:
        """Explain why this routing was chosen"""
        reasons = {
            RequestCategory.TECHNICAL: "Requires technical expertise and system access",
            RequestCategory.BILLING: "Requires financial system access and policies knowledge",
            RequestCategory.PRODUCT: "Requires product features and capabilities knowledge",
            RequestCategory.GENERAL: "General inquiry suitable for any support agent"
        }
        return reasons[category]


class SpecializedHandler:
    """Base class for specialized handlers"""

    def __init__(self, name: str, specialty: str, api_key: str):
        self.name = name
        self.specialty = specialty
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def handle(self, request: str) -> str:
        """Handle the routed request"""
        print(f"\n[{self.name}] Handling request...")

        prompt = f"""As a {self.specialty}, respond to this customer request:

{request}

Provide a helpful, specific response based on your expertise."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text
        print(f"[{self.name}] Response generated")

        return result


class RoutingSystem:
    """
    Complete routing system with router and handlers.

    Demonstrates full end-to-end routing workflow.
    """

    def __init__(self, api_key: str):
        self.router = RouterAgent(api_key)
        self.handlers: Dict[str, SpecializedHandler] = {}
        self._init_handlers(api_key)

    def _init_handlers(self, api_key: str):
        """Initialize specialized handlers"""
        self.handlers = {
            "technical": SpecializedHandler(
                "Tech Support",
                "technical support specialist with system access",
                api_key
            ),
            "billing": SpecializedHandler(
                "Billing Agent",
                "billing specialist with financial system access",
                api_key
            ),
            "product": SpecializedHandler(
                "Product Expert",
                "product specialist with deep feature knowledge",
                api_key
            ),
            "general": SpecializedHandler(
                "General Support",
                "general customer support agent",
                api_key
            )
        }

    def process_request(self, request: str) -> Dict[str, Any]:
        """
        Process customer request through routing system

        Returns: Complete flow with routing decision and response
        """
        print(f"\n{'='*60}")
        print(f"Processing Request: {request[:80]}...")
        print(f"{'='*60}")

        # Step 1: Route
        routing_decision = self.router.route(request)

        # Step 2: Hand off to handler
        category = routing_decision["category"]
        handler = self.handlers[category]

        # Step 3: Handle
        response = handler.handle(request)

        # Step 4: Return complete flow
        return {
            **routing_decision,
            "response": response
        }


class ModelTiering:
    """
    Alternative routing use case: Route to different models based on complexity.

    Simple queries → Fast/cheap model
    Complex queries → Advanced/expensive model
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def assess_complexity(self, query: str) -> str:
        """Assess query complexity"""
        # Use a small model for assessment
        prompt = f"""Rate this query's complexity (simple or complex):

Query: {query}

Simple: Factual, straightforward, single concept
Complex: Multi-part, reasoning required, technical depth

Answer with ONLY: simple or complex"""

        response = self.client.messages.create(
            model="claude-haiku-4-5",  # Use small model for routing
            max_tokens=10,
            messages=[{"role": "user", "content": prompt}]
        )

        complexity = response.content[0].text.strip().lower()
        return complexity if complexity in ["simple", "complex"] else "complex"

    def route_by_complexity(self, query: str) -> Dict[str, Any]:
        """Route to appropriate model based on complexity"""
        complexity = self.assess_complexity(query)

        model_map = {
            "simple": "claude-haiku-4-5",  # Fast & cheap
            "complex": "claude-sonnet-4-6"  # Advanced & expensive
        }

        selected_model = model_map[complexity]

        print(f"\n[MODEL ROUTER] Query complexity: {complexity}")
        print(f"[MODEL ROUTER] Routing to: {selected_model}")

        return {
            "query": query,
            "complexity": complexity,
            "model": selected_model,
            "cost_tier": "low" if complexity == "simple" else "high"
        }


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    print("="*60)
    print("EXAMPLE 1: Category-Based Routing")
    print("="*60)

    routing_system = RoutingSystem(api_key)

    # Test different request types
    requests = [
        "I can't log in to my account, getting error 500",
        "Why was I charged twice on my last invoice?",
        "Does your product support API integration?",
        "What are your business hours?"
    ]

    for request in requests:
        result = routing_system.process_request(request)

        print(f"\n{'='*60}")
        print(f"REQUEST: {result['request']}")
        print(f"CATEGORY: {result['category']}")
        print(f"HANDLER: {result['handler']}")
        print(f"REASON: {result['routing_reason']}")
        print(f"\nRESPONSE:\n{result['response'][:200]}...")
        print(f"{'='*60}\n")

    # Example 2: Model Tiering
    print("\n\n" + "="*60)
    print("EXAMPLE 2: Complexity-Based Model Routing")
    print("="*60)

    tiering = ModelTiering(api_key)

    queries = [
        "What is 2+2?",
        "Explain the architectural trade-offs between microservices and monoliths"
    ]

    for query in queries:
        result = tiering.route_by_complexity(query)

        print(f"\nQuery: {result['query']}")
        print(f"Complexity: {result['complexity']}")
        print(f"Routed to: {result['model']}")
        print(f"Cost tier: {result['cost_tier']}\n")

    """
    Key Insights:

    1. **Classification First**: Router analyzes request before delegation
    2. **Specialized Handlers**: Each category has optimized handler
    3. **Separation of Concerns**: Router logic separate from handling logic
    4. **Cost Optimization**: Simple queries → cheap handlers, complex → expensive
    5. **85-95% Accuracy**: Routing accuracy from 2025 architecture guide

    Routing vs Multi-Agent:
    - Routing: Single classification step, no collaboration
    - Multi-Agent: Ongoing collaboration between agents

    Routing vs Hierarchical:
    - Routing: Flat delegation based on category
    - Hierarchical: Parent-child relationships with task breakdown

    When to use Routing:
    - Clear request categories
    - Specialized handlers available
    - Want cost optimization
    - Need fast classification

    Design considerations:
    - Classification accuracy critical (85-95% achievable)
    - Fallback for misclassification
    - Handling edge cases (multiple categories)
    - Load balancing across handlers

    Real-world applications:
    - Customer support triage
    - Model selection (complexity-based)
    - Load balancing (capacity-based)
    - Domain routing (expertise-based)

    Performance benefits:
    - Cost: Route simple queries to cheaper models
    - Latency: Route to faster models when possible
    - Quality: Route to specialists for better accuracy
    """
