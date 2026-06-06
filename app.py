import streamlit as st
from main import app

st.title("🌍 Multi-Agent AI Travel Planner")

destination = st.text_input(
    "Destination",
    "Goa"
)

budget = int(st.number_input(
    "Budget (₹)",
    value=20000
))

days = st.number_input(
    "Trip Duration (Days)",
    value=3
)

if st.button("Generate Plan"):

    with st.spinner(
        "Generating AI Travel Plan..."
    ):

        result = app.invoke({

            "destination": destination,

            "user_budget": int(budget),

            "days": days,

            "query": f"""
            Plan a {days}-day trip to
            {destination}
            under ₹{budget}
            """,

            "retry_count": 0

        })

        st.success("Plan Generated!")

        st.markdown(
            result["final_plan"]
        )