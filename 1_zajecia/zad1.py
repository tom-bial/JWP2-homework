import json

class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja

    def nowy_model():
        ModelAI.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli
    
    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as file:
            text = file.read()
            params = json.loads(text)
        return cls(params["name"], params["version"])

model = ModelAI("model", 1)
model_z_pliku = ModelAI.z_pliku("model.json")

print(model.nazwa_modelu)
print(model_z_pliku.nazwa_modelu)
