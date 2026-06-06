import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "AVIATIONSTACK_API_KEY"
)

def get_flights(destination):

    url = (
        "http://api.aviationstack.com/v1/flights"
        f"?access_key={API_KEY}"
        "&limit=3"
    )

    response = requests.get(url)

    data = response.json()

    flights = []

    try:

        for flight in data["data"]:

            airline = flight.get(
                "airline",
                {}
            ).get(
                "name",
                "Unknown Airline"
            )

            dep = flight.get(
                "departure",
                {}
            ).get(
                "airport",
                "Unknown Airport"
            )

            arr = flight.get(
                "arrival",
                {}
            ).get(
                "airport",
                "Unknown Airport"
            )

            flights.append(
                f"{airline}: {dep} → {arr}"
            )

    except Exception as e:

        print("Flight API Error:", e)

        flights = [
            "IndiGo Delhi → Goa (~₹4500)",
            "Air India Mumbai → Goa (~₹4000)"
        ]

    return flights