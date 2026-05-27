# Artificial Intelligence - Project 3
# AI Recommendation Logic
# DecodeLabs Internship Project

# Sample database of items
items = [
    {
        "name": "AI for Beginners",
        "tags": ["AI", "Technology", "Programming"]
    },
    {
        "name": "Football Highlights",
        "tags": ["Sports", "Football"]
    },
    {
        "name": "Gym Workout Guide",
        "tags": ["Fitness", "Health"]
    },
    {
        "name": "Python Programming Masterclass",
        "tags": ["Programming", "Technology"]
    },
    {
        "name": "Top Gaming Setups",
        "tags": ["Gaming", "Technology"]
    },
    {
        "name": "Music Production Basics",
        "tags": ["Music", "Creativity"]
    }
]

# Take user interests
user_input = input("Enter your interests separated by commas: ")

# Convert input into a list
user_preferences = [interest.strip().title() for interest in user_input.split(",")]

print("\nYour Interests:", user_preferences)

# Recommendation logic
recommendations = []

for item in items:
    score = 0

    for tag in item["tags"]:
        if tag in user_preferences:
            score += 1

    if score > 0:
        recommendations.append((item["name"], score))

# Sort recommendations by score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
print("\nRecommended Items:")

if recommendations:
    for rec in recommendations:
        print(f"- {rec[0]} (Match Score: {rec[1]})")
else:
    print("No recommendations found.")