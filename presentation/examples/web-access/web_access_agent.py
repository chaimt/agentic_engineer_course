"""
Web Access Pattern (Three-Agent Pipeline)

This example demonstrates a specialized sequential workflow for web content processing.

Pipeline: Search → Scrape → Summarize

Based on arunpshankar's reference implementation.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
import anthropic


@dataclass
class SearchResult:
    """Result from web search"""
    title: str
    url: str
    snippet: str


@dataclass
class ScrapedContent:
    """Extracted content from URL"""
    url: str
    title: str
    content: str
    success: bool
    error: Optional[str] = None


class SearchAgent:
    """
    Specialized agent for web search.

    Single responsibility: Query web and return relevant URLs.
    Tool: SERP API (Google Search API)
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def search(self, query: str, num_results: int = 5) -> List[SearchResult]:
        """Execute web search and return top results"""
        print(f"\n[SEARCH AGENT] Searching for: {query}")

        # In production, use actual SERP API
        # For demo, LLM generates plausible URLs
        prompt = f"""Generate {num_results} relevant web search results for this query: {query}

For each result, provide:
- Title
- URL (realistic domain)
- Snippet (brief description)

Format:
1. Title | URL | Snippet
2. Title | URL | Snippet
..."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse results (simplified - production would use actual SERP API response)
        results = []
        lines = response.content[0].text.split('\n')

        for line in lines:
            if '|' in line and line.strip()[0].isdigit():
                parts = line.split('|')
                if len(parts) >= 3:
                    # Remove number prefix
                    title = parts[0].split('.', 1)[1].strip() if '.' in parts[0] else parts[0].strip()
                    url = parts[1].strip()
                    snippet = parts[2].strip()

                    results.append(SearchResult(title, url, snippet))

        print(f"[SEARCH AGENT] Found {len(results)} results")
        return results[:num_results]


class ScrapeAgent:
    """
    Specialized agent for web scraping.

    Single responsibility: Extract content from URLs.
    Tool: Web scraping libraries (BeautifulSoup, Playwright, etc.)
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def scrape(self, url: str) -> ScrapedContent:
        """Extract content from URL"""
        print(f"\n[SCRAPE AGENT] Scraping: {url}")

        # In production, use actual web scraping
        # For demo, LLM generates plausible content based on URL
        prompt = f"""Based on this URL, generate realistic main content (200-300 words):

URL: {url}

Provide the main textual content you would expect to find at this URL."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text

            print(f"[SCRAPE AGENT] Extracted {len(content)} characters")

            return ScrapedContent(
                url=url,
                title=url.split('/')[-1] or url,
                content=content,
                success=True
            )

        except Exception as e:
            print(f"[SCRAPE AGENT] Failed to scrape {url}: {e}")
            return ScrapedContent(
                url=url,
                title="",
                content="",
                success=False,
                error=str(e)
            )


class SummarizeAgent:
    """
    Specialized agent for content summarization.

    Single responsibility: Synthesize information from multiple sources.
    Tool: LLM summarization capabilities
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"

    def summarize(self, query: str, scraped_content: List[ScrapedContent]) -> str:
        """Synthesize information from all scraped content"""
        print(f"\n[SUMMARIZE AGENT] Synthesizing {len(scraped_content)} sources...")

        # Filter successful scrapes
        successful = [sc for sc in scraped_content if sc.success]

        if not successful:
            return "No content could be extracted from the search results."

        # Combine all content
        combined = "\n\n".join([
            f"Source: {sc.url}\n{sc.content}"
            for sc in successful
        ])

        prompt = f"""Synthesize this information to answer the query: {query}

Sources:
{combined}

Provide:
1. Comprehensive answer to the query
2. Key insights from the sources
3. Any conflicting information noted
4. Limitations or gaps in coverage

Format as a clear, well-structured summary (300-400 words)."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=768,
            messages=[{"role": "user", "content": prompt}]
        )

        summary = response.content[0].text
        print(f"[SUMMARIZE AGENT] Generated summary ({len(summary)} chars)")

        return summary


class WebAccessPipeline:
    """
    Complete web access pipeline: Search → Scrape → Summarize.

    Demonstrates:
    - Sequential agent workflow
    - Single-responsibility agents
    - Tool specialization
    - Error handling at each stage
    """

    def __init__(self, api_key: str):
        self.search_agent = SearchAgent(api_key)
        self.scrape_agent = ScrapeAgent(api_key)
        self.summarize_agent = SummarizeAgent(api_key)

    def research(self, query: str, num_sources: int = 5) -> Dict[str, Any]:
        """
        Execute complete web research workflow.

        Returns:
            Research results with intermediate outputs and final summary
        """
        print(f"\n{'='*60}")
        print(f"Web Access Pipeline: {query}")
        print(f"{'='*60}")

        # Stage 1: Search
        search_results = self.search_agent.search(query, num_sources)

        # Stage 2: Scrape
        scraped_content = []
        for result in search_results:
            scraped = self.scrape_agent.scrape(result.url)
            scraped_content.append(scraped)

        # Stage 3: Summarize
        summary = self.summarize_agent.summarize(query, scraped_content)

        print(f"\n{'='*60}")
        print(f"Web Access Pipeline Complete")
        print(f"{'='*60}")

        return {
            "query": query,
            "search_results": [{"title": r.title, "url": r.url, "snippet": r.snippet} for r in search_results],
            "scraped_count": len([sc for sc in scraped_content if sc.success]),
            "failed_count": len([sc for sc in scraped_content if not sc.success]),
            "summary": summary
        }


# Example usage
if __name__ == "__main__":
    api_key = "your-api-key"

    pipeline = WebAccessPipeline(api_key)

    # Research query
    query = "Latest advances in agentic AI workflows for software engineering"

    result = pipeline.research(query, num_sources=3)

    print(f"\n{'='*60}")
    print("RESEARCH RESULTS:")
    print(f"{'='*60}")

    print(f"\nQuery: {result['query']}")

    print(f"\nSearch Results ({len(result['search_results'])}):")
    for i, sr in enumerate(result['search_results'], 1):
        print(f"  {i}. {sr['title']}")
        print(f"     {sr['url']}")

    print(f"\nScraping: {result['scraped_count']} successful, {result['failed_count']} failed")

    print(f"\n{'='*60}")
    print("SUMMARY:")
    print(f"{'='*60}")
    print(result['summary'])

    """
    Key Insights:

    1. **Single Responsibility**: Each agent does one thing well
       - SearchAgent: Only searches (SERP API)
       - ScrapeAgent: Only scrapes (web extraction)
       - SummarizeAgent: Only summarizes (synthesis)

    2. **Sequential Pipeline**: Clear data flow
       Query → URLs → Content → Summary

    3. **Tool Specialization**: Each agent uses domain-specific tools
       - Search: SERP API (Google, Bing, etc.)
       - Scrape: BeautifulSoup, Playwright, Selenium
       - Summarize: LLM capabilities

    4. **Error Handling**: Each stage can fail independently
       - Failed search: Return empty results
       - Failed scrape: Skip URL, continue with others
       - Failed summarize: Note limitations

    5. **Composability**: Pipeline can be extended
       - Add FactCheckAgent after Summarize
       - Add FilterAgent before Scrape
       - Add RankAgent to prioritize sources

    When to use Web Access Pattern:
    - Systematic web research workflows
    - Competitive intelligence gathering
    - Content aggregation and curation
    - Market research automation
    - News monitoring and summarization

    Design considerations:
    - Rate limiting (respect robots.txt)
    - Caching (avoid redundant scrapes)
    - Error recovery (retry failed scrapes)
    - Content quality (filter low-quality sources)

    Performance optimization:
    - Parallel scraping (scrape multiple URLs simultaneously)
    - Async operations (don't block on each scrape)
    - Result caching (reuse recent scrapes)
    - Smart sampling (scrape subset of results)

    Real-world applications:
    - Research assistants (academic, business)
    - Competitive analysis tools
    - News aggregation platforms
    - Market intelligence systems
    - Content curation pipelines

    Production considerations:
    - Actual SERP API integration (SerpAPI, Google Custom Search)
    - Robust web scraping (handle JavaScript, authentication, captchas)
    - Content extraction (Readability, Trafilatura)
    - Quality filtering (relevance scoring, spam detection)
    - Legal compliance (respect terms of service, copyright)
    """
