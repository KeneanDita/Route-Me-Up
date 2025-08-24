import requests
import pandas as pd

# Get data from API
response = requests.get(
    "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
)

# Convert response to Python dict
data = response.json()

# The questions are inside the "items" key
questions = data["items"]

# Convert to DataFrame
df = pd.DataFrame(questions)

# Save to JSON file
df.to_json("stackoverflow_questions.json", orient="records", indent=4)

print("Saved data to stackoverflow_questions.json")
