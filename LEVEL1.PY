#building a Python function that takes a customer message, strips out stop words, and classifies the message into either "Technical Support", "Billing Support", or "General Inquiry" using an if-else decision structure.
text = input("please enter your query regarding your issue:")
STOP_WORDS = ["a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "in", "on", "at", "to", "for", "with", "of"]

def clean_and_tokenize(text):
    filtered_words = [word for word in text.lower().split() if word not in STOP_WORDS]
    return filtered_words
def classify_text(filtered_words):
        if any(word in filtered_words for word in ["crash", "bug", "error", "broken"]):
             return"technical support"
        elif any(word in filtered_words for word in ["bill","charged","payment","subscription"]):
            return "billing support"
        else:
            return "general inquiry"
print(classify_text(clean_and_tokenize(text)))