CryptoBuddy Chatbot - README
Overview
CryptoBuddy is a simple Python-based chatbot designed to provide basic cryptocurrency information and recommendations. It analyzes predefined crypto data to offer insights on price trends, sustainability, and investment potential.

Features
Price Trend Analysis: Identifies cryptocurrencies currently trending upwards

Sustainability Scoring: Evaluates coins based on energy use and eco-friendliness

Investment Advice: Provides recommendations for long-term growth opportunities

Interactive CLI: Simple text-based interface for user queries

Code Structure
1. CryptoBuddy Class
python
class CryptoBuddy:
    def __init__(self):
        # Initialization with greetings and database
        self.greetings = "Hello! How can I assist you with cryptocurrency today?"
        self.unknown_response = "Sorry not sure how to resspond to that."
        self.crypto_db = {...}  # Predefined cryptocurrency data
2. Cryptocurrency Database
The bot uses a predefined dictionary containing:

Bitcoin, Ethereum, and Cardano data

Metrics including:

Price trend (rising/stable)

Market cap (high/medium)

Energy use (high/medium/low)

Sustainability score (1-10)

3. Response Logic
The respond() method handles user queries with these capabilities:

Greeting recognition

Trending coin identification

Sustainability recommendations

Long-term investment advice

Eco-friendly crypto suggestions
