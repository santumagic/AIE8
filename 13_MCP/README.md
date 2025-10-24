<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">AI Makerspace: MCP Session Repo for Session 13</h1>

This project is a demonstration of the MCP (Model Context Protocol) server, which utilizes the Tavily API for web search capabilities. The server is designed to run in a standard input/output (stdio) transport mode.

## Project Overview

The MCP server is set up to handle web search queries using the Tavily API. It is built with the following key components:

- **TavilyClient**: A client for interacting with the Tavily API to perform web searches.

## Prerequisites

- Python 3.13 or higher
- A valid Tavily API key

## ⚠️NOTE FOR WINDOWS:⚠️

You'll need to install this on the *Windows* side of your OS. 

This will require getting two CLI tool for Powershell, which you can do as follows:

- `winget install astral-sh.uv`
- `winget install --id Git.Git -e --source winget`

After you have those CLI tools, please open Cursor *into Windows*.

Then, you can clone the repository using the following command in your Cursor terminal:

```bash
git clone https://AI-Maker-Space/AIE8-MCP-Session.git
```

After that, you can follow from Step 2. below!

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Configure environment variables**:
Copy the `.env.sample` to `.env` and add your Tavily API key:
   ```
   TAVILY_API_KEY=your_api_key_here
   ```

3. 🏗️ **Add a new tool to your MCP Server** 🏗️

Create a new tool in the `server.py` file, that's it!

## Running the MCP Server

To start the MCP server, you will need to add the following to your MCP Profile in Cursor:

> NOTE: To get to your MCP config. you can use the Command Pallete (CMD/CTRL+SHIFT+P) and select "View: Open MCP Settings" and replace the contents with the JSON blob below.

```
{
    "mcpServers":  {
        "mcp-server": {
            "command" : "uv",
            "args" : ["--directory", "/PATH/TO/REPOSITORY", "run", "server.py"]
        }
    }
}
```

The server will start and listen for commands via standard input/output.

## Usage

The server provides a `web_search` tool that can be used to search the web for information about a given query. This is achieved by calling the `web_search` function with the desired query string.

## Activities: 

There are a few activities for this assignment!

### 🏗️ Activity #1: 

Choose an API that you enjoy using - and build an MCP server for it!

✅ Answer:

- **Built a Currency Converter Tool** using ExchangeRate-API (exchangerate-api.com) - a free REST API providing real-time exchange rates for 160+ currencies without requiring an API key
- **Implementation:** Created `convert_currency()` function in `server.py` (lines 84-162) with parameters for amount, from_currency, and to_currency, featuring input validation, error handling, and formatted output with exchange rate information
- **Testing:** Successfully tested via `test_currency_converter.py` and integrated with Cursor's MCP interface - example: "Convert 500 USD to EUR" returns 430.71 EUR with current exchange rates


### 🏗️ Activity #2: 

Build a simple LangGraph application that interacts with your MCP Server.

You can find details [here](https://github.com/langchain-ai/langchain-mcp-adapters)!

✅ Answer:

- **What I Built:** Connected my MCP server to a LangGraph agent so it can intelligently use all the tools (currency converter, password generator, dice roller, web search)
- **How I Did It:** Created a Jupyter notebook (`MCP_LangGraph_Assignment.ipynb`) that connects to the MCP server, loads all the tools, and creates an agent using `langchain-mcp-adapters` with GPT-4o-mini
- **Results:** Tested it with different queries - it successfully converted currencies (1000 USD = 152,476 JPY), generated secure passwords, rolled dice, and handled multi-step requests. The agent figured out which tools to use on its own!

