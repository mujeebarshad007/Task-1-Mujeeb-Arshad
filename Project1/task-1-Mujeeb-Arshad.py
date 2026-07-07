# Rule Based AI Chatbot
# Mujeeb Arshad
# DecodeLabs AI Internship
# Project 1

print("=" * 50)
print("AI Rule-Based Chatbot")
print("Welcome! I'm DecodeBot.")
print('Type "help" to see all available commands.')
print("=" * 50)

# Ask the user for their name
name = input("Bot: What's your name? ")
print(f"Bot: Nice to meet you, {name}!")

# Keep the chatbot running
while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! How are you?")

    elif message in ["fine", "good"]:
        print("Bot: That's great to hear!")

    elif message == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif message == "who are you":
        print("Bot: I'm DecodeBot, a rule-based AI chatbot developed in Python.")

    elif message == "help":
        print("=" * 50)
        print("HELP MENU")
        print("=" * 50)
        print("- hi, hello, hey")
        print("- fine, good")
        print("- thank you")
        print("- who created you")
        print("- good morning")
        print("- good night")
        print("- bye")
        print("- what can you do")
        print("- how are you")
        print("- who are you")
        print("- motivate me")
        print("- tell me a joke")
        print("- tell me another joke")
        print("- python")
        print("- github")

    elif message == "what can you do":
        print("Bot: I can answer predefined questions.")

    elif message == "motivate me":
        print("Bot: Every expert was once a beginner. Keep learning!")

    elif message == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif message == "tell me another joke":
        print("Bot: There are only 10 kinds of people: those who understand binary and those who don't.")

    elif message in ["python", "what is python"]:
        print("Bot: Python is a beginner-friendly programming language.")

    elif message in ["github", "what is github"]:
        print("Bot: GitHub is used to host code repositories.")

    elif message in ["thank you", "thanks", "thx"]:
        print(f"Bot: You're welcome, {name}!")

    elif message == "who created you":
        print("Bot: I was created by Mujeeb.")

    elif message == "good morning":
        print(f"Bot: Good morning {name}!")

    elif message == "good night":
        print(f"Bot: Good night {name}! Sweet dreams.")


    elif message in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    else:
        print(f"Bot: Sorry {name}, I don't understand that. Type 'help' for available commands.")# Rule Based AI Chatbot
# Mujeeb Arshad
# DecodeLabs AI Internship
# Project 1

print("=" * 50)
print("AI Rule-Based Chatbot")
print("Welcome! I'm DecodeBot.")
print('Type "help" to see all available commands.')
print("=" * 50)

# Ask the user for their name
name = input("Bot: What's your name? ")
print(f"Bot: Nice to meet you, {name}!")

# Keep the chatbot running
while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! How are you?")

    elif message in ["fine", "good"]:
        print("Bot: That's great to hear!")

    elif message == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif message == "who are you":
        print("Bot: I'm DecodeBot, a rule-based AI chatbot developed in Python.")

    elif message == "help":
        print("=" * 50)
        print("HELP MENU")
        print("=" * 50)
        print("- hi, hello, hey")
        print("- fine, good")
        print("- thank you")
        print("- who created you")
        print("- good morning")
        print("- good night")
        print("- bye")
        print("- what can you do")
        print("- how are you")
        print("- who are you")
        print("- motivate me")
        print("- tell me a joke")
        print("- tell me another joke")
        print("- python")
        print("- github")

    elif message == "what can you do":
        print("Bot: I can answer predefined questions.")

    elif message == "motivate me":
        print("Bot: Every expert was once a beginner. Keep learning!")

    elif message == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif message == "tell me another joke":
        print("Bot: There are only 10 kinds of people: those who understand binary and those who don't.")

    elif message in ["python", "what is python"]:
        print("Bot: Python is a beginner-friendly programming language.")

    elif message in ["github", "what is github"]:
        print("Bot: GitHub is used to host code repositories.")

    elif message in ["thank you", "thanks", "thx"]:
        print(f"Bot: You're welcome, {name}!")

    elif message == "who created you":
        print("Bot: I was created by Mujeeb.")

    elif message == "good morning":
        print(f"Bot: Good morning {name}!")

    elif message == "good night":
        print(f"Bot: Good night {name}! Sweet dreams.")


    elif message in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye {name}! Have a nice day.")
        break

    else:
        print(f"Bot: Sorry {name}, I don't understand that. Type 'help' for available commands.")
