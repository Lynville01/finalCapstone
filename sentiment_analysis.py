
import spacy
import pandas as pd

# Step 3: Implement Sentiment Analysis Model
nlp = spacy.load("en_core_web_sm")

# Step 4: Preprocess text data
def preprocess_text(text):
    # Tokenize the text
    tokens = nlp(text)
    
    # Remove stopwords and punctuation
    clean_tokens = [token.text.lower() for token in tokens if not token.is_stop and not token.is_punct]
    
    # Join the tokens back into a string
    clean_text = ' '.join(clean_tokens)
    
    return clean_text

# Step 5: Load dataset
file_path = "/Users/lynville/Downloads/amazon_product_reviews.csv"
data = pd.read_csv(file_path, low_memory=False)

reviews_text = data['reviews.text']
print(reviews_text.head())

# Step 6: Remove missing values
clean_data = data.dropna(subset=['reviews.text'])

# Step 7: Sentiment Analysis Function
def analyze_sentiment(review):
    # Preprocess the review text
    clean_review = preprocess_text(review)
    
    # Analyze sentiment using spaCy model
    doc = nlp(clean_review)
    polarity = doc.sentiment
    
    # Classify sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Step 8: Test Model on Sample Reviews
sample_reviews = [
    "This product so far has not disappointed. My children love to use it and I like the ability to monitor control what content they see with ease",
    "great for beginner or experienced person. Bought as a gift and she loves it,very fast",
    "Inexpensive tablet for him to use and learn on, step up from the NABI. He was thrilled with it, learn how to Skype on it already..."
]

print("Sentiment Analysis Results:")
for review in sample_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review} | Sentiment: {sentiment}")




