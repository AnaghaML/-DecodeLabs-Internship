from datetime import datetime
import random

# Knowledge Base
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you!",
        "Hey! What can I do for you?"
    ],

    "wellbeing": [
        "I'm doing great! Thanks for asking.",
        "I'm functioning perfectly and ready to help!"
    ],

    "identity": [
        "I am a Rule-Based Chatbot created to interact with users through predefined responses.",
        "I'm a simple chatbot that responds using predefined rules."
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ]
}


# Display available commands
def show_help():
    print("\nI can help you with the following:")
    print("- Greetings")
    print("- Tell you about myself")
    print("- Tell you how I am")
    print("- Show the current time")
    print("- Show today's date")
    print("- Respond to thanks")
    print("- Help")
    print("- Exit the conversation")


# Welcome Message
print("=" * 50)
print("Welcome to the Rule-Based Chatbot!")
print("=" * 50)
print("Type 'help' to see what I can do.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")


# Continuous Conversation Loop
while True:

    # Get and sanitize user input
    user_input = input("\nYou: ").strip().lower().rstrip("?!., ")

    # Exit Intent
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Greeting Intent
    elif user_input in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]:
        print("Bot:", random.choice(responses["greeting"]))

    # Well-being Intent
    elif user_input in [
        "how are you",
        "how are you doing",
        "are you okay"
    ]:
        print("Bot:", random.choice(responses["wellbeing"]))

    # Identity Intent
    elif user_input in [
        "what is your name",
        "who are you",
        "tell me about yourself"
    ]:
        print("Bot:", random.choice(responses["identity"]))

    # Help Intent
    elif user_input == "help":
        show_help()

    # Gratitude Intent
    elif user_input in [
        "thanks",
        "thank you",
        "thank you so much"
    ]:
        print("Bot:", random.choice(responses["thanks"]))

    # Time Intent
    elif user_input in [
        "what time is it",
        "tell me the time",
        "current time",
        "time"
    ]:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Date Intent
    elif user_input in [
        "what is today's date",
        "tell me today's date",
        "what date is it",
        "date"
    ]:
        current_date = datetime.now().strftime("%d %B %Y")
        print(f"Bot: Today's date is {current_date}.")

    # Fallback Response
    else:
        print("Bot: Sorry, I don't understand that yet.")
        print("Bot: Type 'help' to see what I can do.")