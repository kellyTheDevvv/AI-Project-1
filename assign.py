# Step 1 - Define the chatbot's personality
class CryptoBuddy:
    def __init__(self):
        self.greetings = "Hello! How can I assist you with cryptocurrency today?"
        self.unknown_response = "Sorry not sure how to resspond to that."

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
        # Step 3 - The Chatbot's Logic
    def respond(self, user_query):
        try:
            user_query = user_query.lower().strip()

            if 'hello' in user_query or 'hi' in user_query:
                return self.greetings
            if 'trending' in user_query or 'rising' in user_query:
                trending_coins = [
                    name for name, data in self.crypto_db.items()
                    if data['price_trend'] == 'rising'
                ]
                if trending_coins:
                    return f"{', '.join(trending_coins)} are currently trending upwards."
                else:
                    return "Hmm... I couldn't find any crypto that's currently rising."
                
                if 'sustainable' in user_query or 'eco' in user_query:
                    best = max(self.crypto_db, key= lambda x : self.crypto_db[x]['sustainability_score'])
                    score = self.crypto_db[best]['sustainability_score']
                    return f"{best} is the most sustainable crypto with a score of {score}/10."
                return self.unknown_response
            #Step 4 - Adding of Advice Rules
                if "long-term" in user_query or "growth" in user_query or "profit" in user_query:
                    recommended = [
                        name for name, data in self.crypto_db.items()
                if data["price_trend"] == "rising" and data["market_cap"] == "high"
                    ]
                if recommended:
                   return f"{', '.join(recommended)} looks strong for long-term growth with rising prices and high market cap!"
            else:
                return "I couldn't find a coin that fits long-term growth criteria right now."
                if "green" in user_query or "low energy" in user_query:
                    green_cryptos = [
                        name for name, data in self.crypto_db.items()
                if data["energy_use"] == "low" and data["sustainability_score"] > 7
                    ]
                    if green_cryptos:
                     return f"{', '.join(green_cryptos)} is super eco-friendly and a great sustainable option!"
                else:
                  return "None of the coins meet high sustainability and low energy use together right now."
        except Exception as e:
            return f"Oops! Something went wrong: {str(e)}"        
bot = CryptoBuddy()
print(bot.greetings)

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()
    if user_input in ['exit', 'quit']:
        print("Chatbot: Goodbye! See you next time!")
        break
    print(f"CryptoBuddy: {bot.respond(user_input)}")

            

                  