# 🌐 Browser MCP Agent

![Area](https://github.com/user-attachments/assets/285a6a02-c1a9-4581-b32b-b244f665f648)

A Streamlit application that allows you to browse and interact with websites using natural language commands through the Model Context Protocol (MCP) and [MCP-Agent](https://github.com/lastmile-ai/mcp-agent) with Puppeteer integration. **Supports OpenAI and any OpenAI API-compatible LLM provider!**

## Features

- **Natural Language Interface**: Control a browser with simple English commands
- **Full Browser Navigation**: Visit websites and navigate through pages
- **Interactive Elements**: Click buttons, fill forms, and scroll through content
- **Visual Feedback**: Take screenshots of webpage elements
- **Information Extraction**: Extract and summarize content from webpages
- **Multi-step Tasks**: Complete complex browsing sequences through conversation
- **Flexible LLM Support**: Use OpenAI or any OpenAI-compatible API (local models, alternative providers)

## Setup

### Requirements

- Python 3.8+
- Node.js and npm (for Puppeteer)
  - This is a critical requirement! The app uses Puppeteer to control a headless browser
  - Download and install from [nodejs.org](https://nodejs.org/)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd mcp_ai_agents/browser_mcp_agent
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify Node.js and npm are installed:
   ```bash
   node --version
   npm --version
   ```
   Both commands should return version numbers. If they don't, please install Node.js.

4. Configure your LLM provider (see Configuration section below)

## Configuration

### Option 1: OpenAI

1. Copy the secrets file:
   ```bash
   cp mcp_agent.secrets.yaml.example mcp_agent.secrets.yaml
   ```

2. Edit `mcp_agent.secrets.yaml`:
   ```yaml
   openai:
     api_key: YOUR_OPENAI_API_KEY
   ```

3. The default configuration in `mcp_agent.config.yaml` will use OpenAI's API.

### Option 2: Local Models (LM Studio, Ollama, etc.)

1. Edit `mcp_agent.config.yaml`:
   ```yaml
   openai:
     # For LM Studio
     base_url: "http://localhost:1234/v1"
     default_model: "your-model-name"  # e.g., "qwen/qwen3-coder-30b"
     
     # For Ollama
     # base_url: "http://localhost:11434/v1"
     # default_model: "llama2"
   ```

2. Copy and edit the secrets file:
   ```bash
   cp mcp_agent.secrets.yaml.example mcp_agent.secrets.yaml
   ```

3. For local models, use a dummy API key:
   ```yaml
   openai:
     api_key: dummy  # Local models don't need a real key
   ```

### Option 3: Alternative Providers (Together AI, Groq, etc.)

1. Edit `mcp_agent.config.yaml`:
   ```yaml
   openai:
     base_url: "https://api.together.xyz/v1"  # Your provider's endpoint
     default_model: "meta-llama/Llama-2-70b-chat-hf"
   ```

2. Add your provider's API key to `mcp_agent.secrets.yaml`:
   ```yaml
   openai:
     api_key: YOUR_PROVIDER_API_KEY
   ```

## Supported LLM Providers

- **OpenAI**: GPT-4, GPT-3.5-turbo, etc.
- **LM Studio**: Any loaded model (local)
- **Ollama**: Llama 2, Mistral, CodeLlama, etc. (local)
- **Together AI**: Open source models via API
- **Groq**: Fast inference models
- **Anyscale**: Various models
- **Perplexity**: Via OpenAI compatibility
- **Any OpenAI-compatible API**: Custom deployments, self-hosted models

## Running the App

1. Start your LLM server (if using local models):
   - **LM Studio**: Start the server from the UI
   - **Ollama**: Run `ollama serve`

2. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

3. In the app interface:
   - Enter your browsing command
   - Click "Run Command"
   - View the results and screenshots

## Example Commands

### Basic Navigation
- "Go to www.lastmileai.dev"
- "Go back to the previous page"

### Interaction
- "Click on the login button"
- "Scroll down to see more content"

### Content Extraction
- "Summarize the main content of this page"
- "Extract the navigation menu items"
- "Take a screenshot of the hero section"

### Multi-step Tasks
- "Go to the blog, find the most recent article, and summarize its key points"

## Architecture

The application uses:
- Streamlit for the user interface
- MCP (Model Context Protocol) to connect the LLM with tools
- Puppeteer for browser automation
- [MCP-Agent](https://github.com/lastmile-ai/mcp-agent/) for the Agentic Framework
- OpenAI-compatible LLMs for interpreting commands and generating responses

## Troubleshooting

### Common Issues

1. **"API key not provided" error**: 
   - Make sure you've created `mcp_agent.secrets.yaml` from the example file
   - For local models, use `api_key: dummy`

2. **Connection refused errors**: 
   - For local models, ensure your LLM server is running
   - Check that the `base_url` in config matches your server's address

3. **Model not found**: 
   - Verify the `default_model` name matches exactly what your provider expects
   - For LM Studio, use the exact model name shown in the UI

4. **Validation errors**:
   - Ensure your `mcp_agent.config.yaml` has the `openai:` section properly formatted
   - Check that `mcp_agent.secrets.yaml` exists and has the `openai:` section

### LM Studio Specific Setup

1. Load a model in LM Studio
2. Start the server (usually on port 1234)
3. Note the exact model name from LM Studio
4. Update `mcp_agent.config.yaml`:
   ```yaml
   openai:
     base_url: "http://localhost:1234/v1"
     default_model: "exact-model-name-from-lm-studio"
   ```
5. Create `mcp_agent.secrets.yaml`:
   ```yaml
   openai:
     api_key: dummy
   ```