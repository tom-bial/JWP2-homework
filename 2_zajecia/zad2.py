class NegativeValueError(ValueError):
    pass

class DataClassifier:
    def classify(self, value):
        if type(value) not in [type(4), type(1.3)]:
            raise TypeError("Nieprawidłowy typ 'value'")

        if value < 0:
            raise NegativeValueError("Wartość 'value' nie może być ujemna")
        elif value < 30:
            return "Niska wartość"
        elif value <= 70:
            return "Średnia wartosć"
        else:
            return "Wysoka wartość"

classifier = DataClassifier()
try:
    print(classifier.classify(50)) # „Średnia wartość”
    #print(classifier.classify(-10)) # Powinien rzucić NegativeValueError
    print(classifier.classify("abc")) # Powinien rzucić TypeError
except Exception as e:
    print(f"Błąd: {e}")