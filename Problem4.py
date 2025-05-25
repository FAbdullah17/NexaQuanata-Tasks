class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

def Localizer(language="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()

if __name__ == "__main__":
    f = Localizer("French")
    e = Localizer("English")
    s = Localizer("Spanish")

    for msg in ["car", "bike", "cycle"]:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
