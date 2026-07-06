🌍 Multi-Agent AI Travel Planner

An Agentic AI Travel Planner built using LangChain, LangGraph, FastAPI, and Streamlit that generates personalized travel itineraries through multi-agent collaboration, tool calling, and stateful workflow orchestration. Instead of relying on a single AI response, the system decomposes a travel request into multiple subtasks handled by specialized AI agents, creating a smarter and more reliable planning experience.

✨ Features
🤖 Multi-Agent AI architecture
🧠 Intelligent task decomposition and planning
🔄 Stateful workflow orchestration using LangGraph
🛠️ Tool calling for external APIs and utilities
🌦️ Weather-aware itinerary generation
🏨 Hotel recommendations based on budget
✈️ Flight cost estimation
💰 Dynamic budget calculation
📅 Personalized day-wise itinerary generation
💬 Human-in-the-loop approval workflow
🎨 Interactive Streamlit user interface
🏗️ Architecture
                        User
                          │
                          ▼
                Planner Agent (Coordinator)
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 Flight Agent       Hotel Agent      Weather Agent
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                   Budget Agent
                          │
                          ▼
                 Itinerary Generator
                          │
                          ▼
                Human Approval Node
                          │
                          ▼
                  Final Travel Plan
🧠 What Makes It Agentic?

Unlike traditional chatbots that produce a single response, this project demonstrates Agentic AI by enabling the system to:

Break complex goals into smaller tasks
Assign tasks to specialized AI agents
Use external tools and APIs
Maintain shared state across the workflow
Make conditional decisions dynamically
Coordinate multiple agents before generating the final response
🛠️ Tech Stack
AI Frameworks
LangChain
LangGraph
Backend
Python
FastAPI
Frontend
Streamlit
LLM
OpenAI GPT / Google Gemini (configurable)
APIs & Tools
Weather API
Search API (Tavily/SerpAPI)
Google Maps API (optional)
Custom Budget Calculator
Utilities
Python Dotenv
Pydantic  

🚀 Workflow
User submits destination, budget, and trip duration.
Planner Agent analyzes the request.
Specialized agents work independently:
Flight Agent estimates travel costs.
Hotel Agent recommends accommodations.
Weather Agent retrieves live weather data.
Budget Agent calculates overall expenses.
LangGraph coordinates the workflow and manages shared state.
The Itinerary Agent creates a personalized day-wise travel plan.
The final itinerary is presented to the user for review and approval.

🎯 Key Concepts Demonstrated
Agentic AI
Multi-Agent Systems
LangChain Agents
LangGraph Workflows
Tool Calling / Function Calling
State Management
Conditional Routing
Memory Management
API Integration
Human-in-the-Loop Systems
