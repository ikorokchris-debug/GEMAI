from openai import OpenAI

client = OpenAI()

print("================================")
print("          ✦ GEM AI ✦")
print("================================")
print("Hello! I'm GEM, your AI assistant.")
print("Type 'bye' whenever you want to leave.")
print()

while True:

    user = input("You: ")

    if user.lower() == "bye":
        print("GEM: Goodbye! 👋")
        break

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="""
        Your name is GEM.

        You are a friendly, intelligent and helpful AI assistant.
        Speak naturally and clearly.
        Be encouraging when helping someone learn programming.
        Your creator is currently learning Software Engineering.
        Never pretend to know something you don't know.
        """,
        input=user
    )

    print()
    print("GEM:", response.output_text)
    print()