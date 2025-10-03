# chatbot.py

def chatbot():
    print("🤖 Hello! I'm your friendly chatbot. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Goodbye! Have a great day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you today?")

        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Bot: I'm a rule-based chatbot created for Task 8.")

        elif "help" in user_input:
            print("Bot: Sure! You can ask me about my name, how I'm doing, or say hello.")

        elif "bye" in user_input:
            print("Bot: Bye! Take care.")

        elif "what do you do" in user_input:
            print("Bot: I chat with users and respond to simple questions using if-else logic.")

        elif "joke" in user_input:
            print("Bot: I'm not programmed for humor yet, but I can still make you smile 😊")

        elif "chatbot" in user_input:
            print("Bot: A chatbot is a program designed to simulate conversation with human users.")

        elif "difference between =" in user_input or "difference between ==" in user_input:
            print("Bot: '=' assigns a value, while '==' compares two values.")

        elif "lower()" in user_input:
            print("Bot: The lower() function converts text to lowercase for easier comparison.")

        elif "limitation" in user_input and "bot" in user_input:
            print("Bot: Rule-based bots can't understand complex language or learn from new conversations.")

        elif "exit this" in user_input or "how to exit" in user_input:
            print("Bot: Just type 'exit' and I'll say goodbye!")

        elif "multiple intents" in user_input:
            print("Bot: I’d check for keywords and prioritize based on context or use NLP techniques.")

        elif "test this" in user_input:
            print("Bot: You can test it manually or write unit tests for each response.")

        elif "organize code" in user_input:
            print("Bot: Break it into functions, use comments, and keep logic modular.")

        elif "ml bot" in user_input or "machine learning" in user_input:
            print("Bot: You can train a model on conversation data and use NLP to evolve into an ML bot.")

        elif "capital of france" in user_input:
            print("Bot: I'm not sure about that. Try asking a geography bot!")

        elif "love chatting" in user_input:
            print("Bot: That’s so kind of you! I’m here whenever you need me.")

        elif "favorite color" in user_input:
            print("Bot: I don’t have preferences, but I think blue is pretty popular!")

        elif "weather" in user_input:
            print("Bot: I wish I could check that, but I’m not connected to live data.")

        elif "who made you" in user_input:
            print("Bot: I was created as part of a Python internship task by a developer like you!")

        elif "purpose" in user_input:
            print("Bot: To help you learn control flow, loops, and input handling in Python.")

        elif "are you real" in user_input:
            print("Bot: I’m real in code—but not in flesh and bones!")

        elif "speak hindi" in user_input:
            print("Bot: मैं थोड़ा बहुत हिंदी समझ सकता हूँ, लेकिन मैं अंग्रेज़ी में बेहतर जवाब देता हूँ।")

        elif "2 + 2" in user_input:
            print("Bot: That’s easy! It’s 4.")

        elif "sing" in user_input or "song" in user_input:
            print("Bot: I wish I could sing, but I don’t have vocal cords—just code!")

        elif "favorite movie" in user_input:
            print("Bot: I don’t watch movies, but I’ve heard 'The Matrix' is popular among bots.")

        elif "interesting" in user_input:
            print("Bot: Did you know honey never spoils? Archaeologists found pots of it in ancient Egyptian tombs!")

        elif "meaning of life" in user_input:
            print("Bot: Philosophers say 42. I say—keep learning and stay curious!")

        else:
            print("Bot: I'm not sure how to respond to that. Try asking something else.")

if __name__ == "__main__":
    chatbot()