responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "hey": "Hey!",
    "how are you": "I'm doing great!",
    "who are you": "I'm an AI chatbot.",
    "what is your name": "I'm Niko.",
    "what can you do": "I can answer basic questions.",
    "help": "Ask me anything!",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a great day!",
    "exit": "Exiting chatbot..."
}

while True: 
    raw_input =input('You : ')
    user_input=raw_input.lower().strip()
    
    if user_input=="exit":
        print("Thank you for using me.Bye bye")
        break
    reply =responses.get(user_input,"I do not Understand")
    print("Bot: ",reply)