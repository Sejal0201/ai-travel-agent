from ddgs import DDGS

def get_hotels(city):

    query = f"best hotels in {city}"

    hotels = []

    try:

        with DDGS(timeout=20) as ddgs:

            results = ddgs.text(
                query,
                max_results=5
            )

            for item in results:

                hotels.append(
                    item.get(
                        "title",
                        "Unknown Hotel"
                    )
                )

    except Exception as e:

        print("Search Error:", e)

        hotels = [
            "Goa Marriott Resort",
            "Hotel Calangute Towers",
            "Taj Resort Goa"
        ]

    return hotels

