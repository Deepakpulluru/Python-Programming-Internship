def generate_response(user_input):
    # Define some basic responses based on keywords
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! How can I assist you?",
        "what can you do": "I can chat with you. Feel free to ask me anything!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "who is the president of the united states": "As of 2024, the president of the United States is Joe Biden.",
        "bye": "Goodbye! Have a great day!"
    }

    # Normalize the user input
    normalized_input = user_input.lower().strip()

    # Find a matching response
    for key in responses:
        if key in normalized_input:
            return responses[key]
    
    return "I'm not sure how to respond to that."

def chat():
    print("Chatbot: Hi! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = generate_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
