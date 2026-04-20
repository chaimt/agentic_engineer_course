"""
Tool Use Pattern Example - Agent with File System and Shell Tools

This example demonstrates how an agent can use external tools
to interact with the file system and execute shell commands.
"""

import os
import subprocess
from typing import List, Dict, Any, Callable
import anthropic


class ToolUseAgent:
    """
    Agent that can call external tools to accomplish tasks.

    Pattern: Define Tools → Plan → Execute → Observe → Act
    """

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
        self.tools = self._register_tools()

    def _register_tools(self) -> List[Dict[str, Any]]:
        """Define available tools for the agent"""
        return [
            {
                "name": "read_file",
                "description": "Read contents of a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "File path to read"}
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "File path to write"},
                        "content": {"type": "string", "description": "Content to write"}
                    },
                    "required": ["path", "content"]
                }
            },
            {
                "name": "list_files",
                "description": "List files in a directory",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "directory": {"type": "string", "description": "Directory path"}
                    },
                    "required": ["directory"]
                }
            },
            {
                "name": "execute_command",
                "description": "Execute a shell command",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Shell command to execute"}
                    },
                    "required": ["command"]
                }
            }
        ]

    def _execute_tool(self, tool_name: str, tool_input: Dict[str, Any]) -> str:
        """Execute a tool and return the result"""
        try:
            if tool_name == "read_file":
                with open(tool_input["path"], "r") as f:
                    return f.read()

            elif tool_name == "write_file":
                with open(tool_input["path"], "w") as f:
                    f.write(tool_input["content"])
                return f"File written successfully to {tool_input['path']}"

            elif tool_name == "list_files":
                files = os.listdir(tool_input["directory"])
                return "\n".join(files)

            elif tool_name == "execute_command":
                result = subprocess.run(
                    tool_input["command"],
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                return result.stdout if result.returncode == 0 else result.stderr

            else:
                return f"Unknown tool: {tool_name}"

        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

    def execute_task(self, task: str, max_iterations: int = 5) -> str:
        """
        Execute a task using tool calls in a loop

        The agent:
        1. Receives the task
        2. Decides which tool(s) to use
        3. Executes tools
        4. Observes results
        5. Repeats until task complete
        """
        messages = [{"role": "user", "content": task}]
        iteration = 0

        print(f"Task: {task}\n")

        while iteration < max_iterations:
            iteration += 1
            print(f"Iteration {iteration}:")

            # Agent decides next action
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                tools=self.tools,
                messages=messages
            )

            # Check if agent wants to use tools
            if response.stop_reason == "tool_use":
                tool_calls = [block for block in response.content if block.type == "tool_use"]

                for tool_call in tool_calls:
                    tool_name = tool_call.name
                    tool_input = tool_call.input

                    print(f"  → Using tool: {tool_name}")
                    print(f"    Input: {tool_input}")

                    # Execute the tool
                    tool_result = self._execute_tool(tool_name, tool_input)
                    print(f"    Result: {tool_result[:100]}...")

                    # Add tool result to conversation
                    messages.append({"role": "assistant", "content": response.content})
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": tool_call.id,
                            "content": tool_result
                        }]
                    })

            else:
                # Agent is done - no more tool calls needed
                final_response = response.content[0].text
                print(f"\n✓ Task complete: {final_response}")
                return final_response

        return "Max iterations reached"


# Example usage
if __name__ == "__main__":
    # Initialize agent with tools
    agent = ToolUseAgent(api_key="your-api-key")

    # Example 1: File system operations
    task1 = """
    Create a new file called 'hello.txt' with the content 'Hello, Agentic World!',
    then read it back to confirm it was created correctly.
    """

    print("="*60)
    print("EXAMPLE 1: File Operations")
    print("="*60)
    agent.execute_task(task1)

    # Example 2: Shell command execution
    task2 = """
    List all Python files in the current directory using a shell command,
    then count how many there are.
    """

    print("\n" + "="*60)
    print("EXAMPLE 2: Shell Commands")
    print("="*60)
    agent.execute_task(task2)

    """
    Key insights:
    1. Agent chooses which tools to use based on the task
    2. Agent can chain multiple tool calls together
    3. Agent observes tool results and adjusts its approach
    4. Execution is autonomous - no human intervention needed

    This is the core of agentic behavior: decision → action → observation → next decision
    """
