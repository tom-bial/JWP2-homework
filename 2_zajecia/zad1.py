class TextAnalyzer:
    def strip(self, text):
        to_remove = [".", "!", "?"]
        if text[-1] in to_remove:
            return text[:-1]
        else:
            return text

    def word_count(self, text):
        text = self.strip(text)
        return len(text.split(" "))
    
    def char_count(self, text):
        return len(text)
    
    def unique_words(self, text):
        text = self.strip(text)
        return len(set(text.split(" ")))

class AdvancedTextAnalyzer(TextAnalyzer):
    def __init__(self, positive_words, negative_words):
        super().__init__()
        self.positive_words = positive_words
        self.negative_words = negative_words

    def sentiment_analysis(self, text):
        text = self.strip(text)
        wyrazy = text.split(" ")
        positive_counter = 0
        negative_counter = 0
        for i in range(len(wyrazy)):
            if wyrazy[i] in self.positive_words:
                positive_counter += 1
                
            if wyrazy[i] in self.negative_words:
                negative_counter += 1

        if positive_counter > negative_counter:
            return "Pozytywny"
        elif positive_counter < negative_counter:
            return "Negatywny"
        else:
            return "Neutralny"

text1 = "To był naprawdę wspaniały dzień!"
text2 = "To był naprawdę okropny dzień!"
text3 = "Tutaj to i to się powtarza się."

analyzer = TextAnalyzer()
advanced_analyzer = AdvancedTextAnalyzer(["miły", "wspaniały", "cudowny"], ["okropny", "zły", "brzydki"])

texts = [text1, text2, text3]
for text in texts:
    print("Tekst:", text)
    print("Liczba słów:", analyzer.word_count(text))
    print("Liczba znaków:", analyzer.char_count(text))
    print("Liczba unikalnych słów:", analyzer.unique_words(text))
    print("Tekst jest:", advanced_analyzer.sentiment_analysis(text))
    print()