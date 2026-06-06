from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict
from weather_tool import get_weather
from budget_validator import validate_budget
from flight_tool import get_flights
from hotel_tool import get_hotels
from flight_tool import get_flights
from langgraph.graph import StateGraph, END

load_dotenv()

llm = ChatGroq(
    # model="llama-3.3-70b-versatile"
    model="llama-3.1-8b-instant"
)

# STATE
class TravelState(TypedDict):

    query:str
    weather: str
    research:str
    budget_estimate:str
    hotels:str
    flights: str
    activities:str
    retry_count: int
    final_plan:str
    destination:str
    user_budget:int
    days:int
    validation:str


# RESEARCH
def research_agent(state):

    response = llm.invoke(
        f"Research travel info for: {state['query']}"
    )

    return {"research": response.content}


# BUDGET
def budget_agent(state):

    response = llm.invoke(
        f"""
        Using:

        {state['research']}

        Create budget estimate.
        """
    )

    return {"budget_estimate": response.content}

def weather_agent(state):

    weather = get_weather( state["query"].split("to")[1].split("under")[0].strip())

    return {
        "weather": weather
    }
# HOTELS
def hotel_agent(state):

    city = state["query"].split("to")[1].split("under")[0].strip()

    hotels = get_hotels(city)

    return {

        "hotels":
        "\n".join(hotels)

    }
# FLIGHTS
def flight_agent(state):

    flights = get_flights(
        state["destination"]
    )

    return {

        "flights":
        "\n".join(flights)

    }

# ACTIVITIES
def activity_agent(state):

    response = llm.invoke(
        f"""
        Using:

        {state['research']}

        Suggest activities.
        """
    )

    return {"activities": response.content}


# COORDINATOR
def coordinator_agent(state):

    response = llm.invoke(
        f"""
        Build a FINAL travel plan.

        IMPORTANT RULES:

        Destination: {state['destination']}
        Duration: {state['days']} days

        USER BUDGET:
        ₹{state['user_budget']}

        You MUST use EXACTLY this budget.
        Do NOT invent another budget.
        Do NOT optimize for ₹20,000.

        Hotels:
        {state['hotels']}

        Flights:
        {state['flights']}

        Activities:
        {state['activities']}

        Weather:
        {state['weather']}
        """
    )

    return {
        "final_plan": response.content
    }


# VALIDATOR
def validator_agent(state):

    result = validate_budget(
        state["final_plan"],
        state["user_budget"]
    )

    return {
        "validation": result
    }


# OPTIMIZER
def optimizer_agent(state):

    retries = state.get(
        "retry_count",
        0
    )

    response = llm.invoke(
        f"""
        Optimize this itinerary.

        USER BUDGET:
        ₹{state['user_budget']}

        IMPORTANT:
        Keep total cost CLOSE TO the user's budget.

        If user budget is ₹50000,
        do NOT reduce to ₹20000.

        Current plan:

        {state['final_plan']}
        """
    )

    return {

        "final_plan":
        response.content,

        "retry_count":
        retries + 1
    }


# CONDITIONAL ROUTING
def route_validation(state):

    retries = state.get(
        "retry_count",
        0
    )

    if state["validation"] == "VALID":

        print(
            "\n✅ PLAN VALIDATED\n"
        )

        return END

    if retries >= 2:

        print(
            "\n⚠ MAX RETRIES REACHED\n"
        )

        return END

    print(
        "\n❌ PLAN INVALID → OPTIMIZING\n"
    )

    return "optimizer"


# GRAPH
graph = StateGraph(TravelState)

graph.add_node("research", research_agent)
graph.add_node("weather",weather_agent)
graph.add_node("budget", budget_agent)
graph.add_node("hotels", hotel_agent)
graph.add_node("activities", activity_agent)

graph.add_node("coordinator", coordinator_agent)

graph.add_node("validator", validator_agent)
graph.add_node("flights", flight_agent)

graph.add_node("optimizer", optimizer_agent)

# ENTRY
graph.set_entry_point("research")

# PARALLEL
graph.add_edge("research","budget")
graph.add_edge("research","hotels")
graph.add_edge("research","activities")
graph.add_edge("research","weather")
graph.add_edge( "research","flights")

# MERGE
graph.add_edge("budget","coordinator")
graph.add_edge("hotels","coordinator")
graph.add_edge("activities","coordinator")
graph.add_edge("weather","coordinator")
graph.add_edge("flights","coordinator")
# VALIDATE
graph.add_edge("coordinator","validator")

# CONDITIONAL EDGE
graph.add_conditional_edges(
    "validator",
    route_validation
)

# RETRY LOOP
graph.add_edge("optimizer","validator")

app = graph.compile()

# RUN
