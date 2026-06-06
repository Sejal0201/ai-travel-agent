from fastapi import FastAPI
from pydantic import BaseModel
from main import app as travel_app

api = FastAPI()


@api.get("/")
def home():
    return {
        "message": "AI Travel Planner API is running 🚀"
    }


class TravelRequest(BaseModel):
    destination: str
    budget: int
    days: int


@api.post("/plan")
def generate_plan(req: TravelRequest):

    result = travel_app.invoke({

        "destination": req.destination,

        "user_budget": req.budget,

        "days": req.days,

        "query":
        f"""
        Plan a {req.days}-day trip to
        {req.destination}
        under ₹{req.budget}
        """,

        "retry_count": 0
    })

    return {
        "plan": result["final_plan"]
    }