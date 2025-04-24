import re

def custom_tokenizer(text):
    patterns = [
  
        r'https?://[^\s]+',
        r'www\.[^\s]+',

        r'\b[\w.-]+?@\w+?\.\w{2,4}\b',
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
        r'\b\d{1,3}(,\d{2,3})+(.\d+)?\b',
        r'\b\d+/\d+\b',
        r'\b\d+\.\d+\b',
        r'\b\d+\b',
        r'@\w+',
        r'[\u0900-\u097F]+',
        r'[a-zA-Z]+',
        r'[.,!?;:"\'()\-—\[\]{}…]'
    ]

    combined_pattern = '|'.join(patterns)
    tokens = re.findall(combined_pattern, text)
    return tokens

text = "मेरे दोस्त @amit ने मुझे ईमेल किया amit.kumar@example.com पर 24/04/2025 को। उसकी वेबसाइट है https://amitdev.com और उसने ₹3,22,243 खर्च किए!"
tokens = custom_tokenizer(text)
print(tokens)
