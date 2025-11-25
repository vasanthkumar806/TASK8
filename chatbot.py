print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif "name" in user:
        print("Chatbot: I am a simple rule-based chatbot.")
    elif "time" in user:
        import datetime
        print("Chatbot:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif "how are you" in user:
        print("Chatbot: I'm doing great! Thanks for asking.")
    elif "bye" in user:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I didn't understand that.")
