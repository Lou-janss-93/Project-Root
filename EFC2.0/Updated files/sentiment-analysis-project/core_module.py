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

        # Process with YinYangModule
        self.yin_yang_module.adjust_balance(dominant_emotion)
        yy_response = self.yin_yang_module.respond()
        print(yy_response)

        # Process with SGRSModule
        sgrs_output = self.sgrs_module.process(dominant_emotion)
        print(f"SGRS output: {sgrs_output}")

        # Process with PESEBNModule
        pesebn_output = self.pesebn_module.some_functionality()
        print(f"PESEBN output: {pesebn_output}")

        # Calculate final emotion and response
        final_emotion = self.calculate_final_emotion(dominant_emotion, sgrs_output, pesebn_output)
        final_response = self.yin_yang_module.respond(final_emotion)
        print(f"Final response: {final_response}")

    def calculate_final_emotion(self, dominant_emotion, sgrs_output, pesebn_output):
        # Implement logic to calculate final emotion based on module outputs
        if sgrs_output == "positive" or (pesebn_output is not None and pesebn_output > 0.5):
            return "positive"
        elif sgrs_output == "negative" or (pesebn_output is not None and pesebn_output < 0.5):
            return "negative"
        elif sgrs_output == "neutral":
            return "neutral"
        else:
            return dominant_emotion
