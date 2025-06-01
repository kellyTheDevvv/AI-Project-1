# Step 1 - Define the chatbot's personality
class CryptoBuddy:
    def __init__(self):
        self.greetings = "Hello! How can I assist you with cryptocurrency today?"
        self.unknown_response = "Sorry not sure how to respond to that."

# Add this list of random disclaimers
        self.disclaimers = [
        "Remember: Cryptocurrency investments are volatile and risky.",
        "Disclaimer⚠️: This is not financial advice. Always do your own research.",
        "Note: Past performance doesn't guarantee future results.",
        "Warning⚠️: Never invest more than you can afford to lose.",
        "Important: Cryptocurrency regulations vary by region.",
        "FYI: The crypto market can be highly unpredictable."
          ]

        # Step 2 - Predefined Crypto Data
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8
                }
        }

    def get_random_disclaimer(self):
        import random
        return random.choice(self.disclaimers)

        # Step 3 - The Chatbot's Logic
    def respond(self, user_query):
        try:
            user_query = user_query.lower().strip()
            responses = []  # Store all matching responses
        
        # 1. Greeting check
            if 'hello' in user_query or 'hi' in user_query:
                responses.append(f"{self.greetings}")
            
            # 2. Combined query check
            if ('trending' in user_query or 'rising' in user_query) and \
            ('sustainable' in user_query or 'eco' in user_query or 'green' in user_query):
                trending_sustainable = [
                    name for name, data in self.crypto_db.items()
                    if data['price_trend'] == 'rising' and data['sustainability_score'] >= 6
                ]
                if trending_sustainable:
                    responses.append(f"Trending & sustainable: {', '.join(trending_sustainable)}")
                else:
                    responses.append("No coins meet both trending and sustainable criteria")
            
            # 3. Individual checks
            if 'trending' in user_query or 'rising' in user_query:
                trending_coins = [
                    name for name, data in self.crypto_db.items()
                    if data['price_trend'] == 'rising'
                ]
                if trending_coins:
                    responses.append(f"Trending coins: {', '.join(trending_coins)}")
                else:
                    responses.append("No currently trending coins found")
            
            if 'sustainable' in user_query or 'eco' in user_query or 'green' in user_query:
                best = max(self.crypto_db.items(), key=lambda x: x[1]['sustainability_score'])
                responses.append(f"Most sustainable: {best[0]} (Score: {best[1]['sustainability_score']}/10)")
            
            if "long-term" in user_query or "growth" in user_query or "profit" in user_query:
                recommended = [
                    name for name, data in self.crypto_db.items()
                    if data["price_trend"] == "rising" and data["market_cap"] == "high"
                ]
                if recommended:
                    responses.append(f"Good for long-term growth: {', '.join(recommended)}")
                else:
                    responses.append("No strong long-term options currently")
            
            if "low energy" in user_query:
                green_coins = [
                    name for name, data in self.crypto_db.items()
                    if data["energy_use"] == "low" and data["sustainability_score"] > 7
                ]
                if green_coins:
                    responses.append(f"Low-energy coins: {', '.join(green_coins)}")
                else:
                    responses.append("No qualifying low-energy coins found")
            
            # 4. Final response assembly
            if responses:
                return f"{'. '.join(responses)}. {self.get_random_disclaimer()}"
            else:
                return f"{self.unknown_response}"
                
        except Exception as e:
            return f"Error: {str(e)}."
    
bot = CryptoBuddy()
print(bot.greetings)

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()
    if user_input in ['exit', 'quit']:
        print("Chatbot: Goodbye! See you next time!")
        break
    print(f"CryptoBuddy: {bot.respond(user_input)}")

            

                  
