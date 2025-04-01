class SimpleChatbot:
    def __init__(self, pytania):
        self.pytania = pytania
        self.counter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.pytania):
            self.counter += 1
            return self.pytania[self.counter - 1]
        else:
            raise StopIteration
        
bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
for question in bot:
    print(question)
    input() # Użytkownik wpisuje odpowiedź