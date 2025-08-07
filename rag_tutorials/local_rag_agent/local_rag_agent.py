# Import necessary libraries
from agno.agent import Agent
from agno.knowledge.json import JSONKnowledgeBase
from agno.vectordb.qdrant import Qdrant
from agno.playground import Playground, serve_playground_app

from pathlib import Path

COLLECTION_NAME = "json-reader"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

knowledge_base = JSONKnowledgeBase(
    path=Path("/Users/jasonschulz/.claude/projects"),  # Update with your path
    vector_db=vector_db,
    num_documents=5,  # Number of documents to return on search
)

# Initialize the Agent with the knowledge_base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

# Load the knowledge base, comment out after the first run to avoid reloading
knowledge_base.load(recreate=True, upsert=True)

# UI for RAG agent
app = Playground(agents=[agent]).get_app()

# Run the Playground app
if __name__ == "__main__":
    serve_playground_app("local_rag_agent:app", reload=True)
