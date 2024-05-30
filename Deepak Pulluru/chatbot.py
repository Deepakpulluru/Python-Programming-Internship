import spacy
from transformers import pipeline

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the Hugging Face pipeline for conversational response generation
chatbot_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")
def generate_response(user_input):
    # Preprocess the user input using spaCy
    doc = nlp(user_input)
    
    # Extract keywords and entities (optional, can be used to enhance response generation)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Generate a response using the Hugging Face pipeline
    conversation = chatbot_pipeline(user_input)
    response = conversation.generated_responses[-1]
    
    return response

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
