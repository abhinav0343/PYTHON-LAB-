import re

def custom_tokenizer(text):
    patterns = [
        # URLs
        r'https?://[^\s]+',
        r'www\.[^\s]+',
        
        # Emails
        r'\b[\w.-]+?@\w+?\.\w{2,4}\b',
        
        # Dates (e.g., 24/04/2025 or 24-04-25)
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
        
        # Numbers (e.g., 33.15, 3,22,243, 313/77)
        r'\b\d{1,3}(,\d{2,3})+(.\d+)?\b',
        r'\b\d+/\d+\b',
        r'\b\d+\.\d+\b',
        r'\b\d+\b',
        
        # Social Media Handles (e.g., @username)
        r'@\w+',
        
        # Devanagari words (or replace with your language's Unicode range)
        r'[\u0900-\u097F]+',
        
        # English words
        r'[a-zA-Z]+',
        
        # Punctuation
        r'[.,!?;:"\'()\-—\[\]{}…]'
    ]

    combined_pattern = '|'.join(patterns)
    tokens = re.findall(combined_pattern, text)
    return tokens

# Example usage
text = "मेरे दोस्त @amit ने मुझे ईमेल किया amit.kumar@example.com पर 24/04/2025 को। उसकी वेबसाइट है https://amitdev.com और उसने ₹3,22,243 खर्च किए!"
tokens = custom_tokenizer(text)
print(tokens)
