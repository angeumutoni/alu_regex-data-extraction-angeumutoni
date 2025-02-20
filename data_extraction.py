import re

def extract_data(text):
    # Define regex patterns for different data types
    patterns = {
        "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "urls": r"https?://[^\s/$.?#].[^\s]*",
        "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
        "credit_cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
        "time_24": r"(?:[01]\d|2[0-3]):[0-5]\d",
        "time_12": r"(1[0-2]|[1-9]):[0-5]\d\s?[AP]M",
        "html_tags": r"<[^>]+>",
        "hashtags": r"#\w+",
        "currency": r"\$[0-9,]+(\.[0-9]{2})?"
    }

    results = {}
    for key, pattern in patterns.items():
        results[key] = re.findall(pattern, text)

    return results

# Sample text for testing
sample_text = """
Contact me at user@example.com or visit https://www.example.com.
Call me at (123) 456-7890 or 123-456-7890.
My credit card number is 1234-5678-9012-3456.
The meeting is at 2:30 PM or 14:30.
Here are some HTML tags: <div> and <p>.
Don't forget to check #example and #ThisIsAHashtag.
The price is $19.99 or $1,234.56.
"""

# Extract data
extracted_data = extract_data(sample_text)

# Print the results
print("Extracted Data:")
for data_type, values in extracted_data.items():
    print(f"{data_type.capitalize()}: {values}")
