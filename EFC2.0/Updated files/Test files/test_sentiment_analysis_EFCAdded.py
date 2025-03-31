import unittest
from core_module import CoreModule

class TestSentimentAnalysisEFCAdded(unittest.TestCase):
    def setUp(self):
        self.core_module = CoreModule()

    def test_positive_emotion(self):
        text = "I am very happy today!"
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("positive", final_response)

    def test_negative_emotion(self):
        text = "I am feeling very sad."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("negative", final_response)

    def test_neutral_emotion(self):
        text = "I am just okay."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("neutral", final_response)

    def test_mixed_emotion(self):
        text = "I am happy but also a bit sad."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("mixed", final_response)

    def test_custom_emotion(self):
        text = "I am feeling anxious and excited."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("anxious", final_response)

    def test_critical_positive_emotion(self):
        text = "I am extremely happy today!"
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("positive", final_response)

    def test_critical_negative_emotion(self):
        text = "I am feeling extremely sad."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("negative", final_response)

    def test_critical_neutral_emotion(self):
        text = "I am just okay, nothing special."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("neutral", final_response)

    def test_critical_mixed_emotion(self):
        text = "I am extremely happy but also very sad."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("mixed", final_response)

    def test_critical_custom_emotion(self):
        text = "I am feeling extremely anxious and excited."
        self.core_module.process_text(text)
        final_response = self.core_module.yin_yang_module.log[-1][2]
        print(f"Final response: {final_response}")
        self.assertIn("anxious", final_response)

if __name__ == "__main__":
    unittest.main(verbosity=2)