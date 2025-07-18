import random

dict = {
    "name": "Alice",
    "age": random.randint(18, 65),
    "height": round(random.uniform(1.5, 2.0), 2),
    "is_student": random.choice([True, False]),
    "grades": [random.randint(60, 100) for _ in range(5)],
    "address": {
        "city": random.choice(["New York", "London", "Tokyo", "Sydney"]),
        "zip": random.randint(10000, 99999),
    },
    "hobbies": random.sample(["reading", "sports", "music", "coding", "travel"], 3),
    "profile": None,
}
