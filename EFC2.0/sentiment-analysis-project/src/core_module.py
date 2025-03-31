from yin_yang_module import YinYangModule
from sgrs_module import SGRSModule
from pesebn_module import PESEBNModule
from sentiment_analysis import detect_emotion

class CoreModule:
    def __init__(self):
        self.yin_yang_module = YinYangModule("YY Module")
        self.sgrs_module = SGRSModule("SGRS Module")
        self.pesebn_module = PESEBNModule(0.6, 0.4)  # Voorbeeldwaarden voor alpha en beta

    def process_text(self, text):
        dominant_emotion = detect_emotion(text)
        print(f"Dominante emotie: {dominant_emotion}")

        self.yin_yang_module.adjust_balance(dominant_emotion)
        response = self.yin_yang_module.respond("vraag over AI filosofie")
        print(response)

        # Voeg hier de logica toe voor SGRS en PESEBN modules
        self.sgrs_module.process(dominant_emotion)
        self.pesebn_module.some_functionality()

# Voorbeeld gebruik
if __name__ == "__main__":
    core_module = CoreModule()
    core_module.process_text("Ik ben zo blij en gelukkig vandaag.")