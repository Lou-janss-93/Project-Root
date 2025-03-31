import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from core_module import CoreModule
from sgrs_module import SGRSModule
from pesebn_module import PESEBNModule
from sentiment_analysis import detect_emotion

# Basic Framework for Yin-Yang & Rest/balance and Emotional Response in AI
# This is a simple version of the full module but does almost the same as the final version.
# The Yin-Yang module is to look at the input to see if it's positive or negative and then adjust the balance accordingly.
# The YinYangModule is to adjust the balance based on the context and severity of the input.
class YinYangModule:
    def __init__(self, name):
        """
        Initializes the YinYangModule with a name and default balance.
        
        Args:
            name (str): The name of the module.
        """
        self.name = name
        self.balance = 0  # Yin-Yang balance value, range: -45 (Yin) to +45 (Yang)
        self.log = []  # To keep track of balance adjustments and responses

    def adjust_balance(self, context):
        """
        Adjusts Yin-Yang balance based on input context.
        
        Args:
            context (str): The context indicating positive or negative input.
        """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= 1  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += 1  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def adjust_balance_dynamic(self, context, severity):
        """
        Dynamically adjusts Yin-Yang balance based on context severity.
        
        Args:
            context (str): The context indicating positive or negative input.
            severity (int): The severity of the context.
        """
        if context in ["positief/goed", "positive", "happy"]:
            self.balance -= severity  # Move towards Yin
        elif context in ["negatief/slecht", "negative", "sad"]:
            self.balance += severity  # Move towards Yang
        # Keep balance within bounds
        self.balance = max(-45, min(45, self.balance))

    def respond(self, trigger):
        """
        Generates response based on current balance and trigger input.
        
        Args:
            trigger (str): The trigger input to respond to.
        
        Returns:
            str: The generated response.
        """
        response = f"{self.name} responds in a calm (Yin) way to {trigger}." if self.balance < 0 else f"{self.name} responds in an active (Yang) way to {trigger}."
        self.log.append((trigger, self.balance, response))
        return response

# Example usage
text = "Ik ben zo blij en gelukkig vandaag."
dominant_emotion = detect_emotion(text)
print(f"Dominante emotie: {dominant_emotion}")

# Create an instance of YinYangModule
yy_module = YinYangModule("YY Module")
yy_module.adjust_balance(dominant_emotion)
response = yy_module.respond("vraag over AI filosofie")
print(response)

# CoreModule integratie
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
        yy_response = self.yin_yang_module.respond(text)
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
        # This is a placeholder implementation
        if sgrs_output == "positive" or (pesebn_output is not None and pesebn_output > 0.5):
            return "positive"
        elif sgrs_output == "negative" or (pesebn_output is not None and pesebn_output < 0.5):
            return "negative"
        else:
            return dominant_emotion

# Example usage
if __name__ == "__main__":
    core_module = CoreModule()
    core_module.process_text("I am feeling extremely happy today!")
    core_module.process_text("I am feeling extremely sad.")