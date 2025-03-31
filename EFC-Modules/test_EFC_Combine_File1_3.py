import unittest
import sys
import os

# Voeg het pad toe aan sys.path om de module te kunnen importeren
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from EFCCombineFile13 import detect_emotion, Rest_BalanceModule, EmotionModule, Rest_NeedModule, IntentModule

class TestEmotionDetection(unittest.TestCase):
    def setUp(self):
        self.texts = [
            "Ik ben zo blij en gelukkig vandaag.",
            "Ik voel me verdrietig en somber.",
            "Ik ben bang en nerveus.",
            "Ik ben verrast en ongelofelijk verbaasd.",
            "Ik voel walging en afschuw.",
            "Ik ben boos en kwaad.",
            "Ik voel liefde en genegenheid."
        ]
        self.expected_emotions = [
            "vreugde",
            "verdriet",
            "angst",
            "verrassing",
            "walging",
            "woede",
            "liefde"
        ]

    def test_detect_emotion(self):
        for text, expected_emotion in zip(self.texts, self.expected_emotions):
            with self.subTest(text=text):
                detected_emotion = detect_emotion(text)
                self.assertEqual(detected_emotion, expected_emotion)

class TestEmotionModules(unittest.TestCase):
    def setUp(self):
        self.mystique = IntentModule("Myst.")
        self.Neori = IntentModule("Neori")

    def test_adjust_balance(self):
        self.mystique.adjust_balance("positief/goed")
        self.assertEqual(self.mystique.balance, -1)
        self.Neori.adjust_balance_dynamic("negatief/slecht", 2)
        self.assertEqual(self.Neori.balance, 2)

    def test_adjust_rest(self):
        self.mystique.adjust_rest("rest")
        self.assertEqual(self.mystique.rest_level, 55)
        self.Neori.adjust_rest("stress")
        self.assertEqual(self.Neori.rest_level, 45)

    def test_respond(self):
        self.mystique.adjust_balance("positief/goed")
        self.Neori.adjust_balance_dynamic("negatief/slecht", 2)
        self.mystique.adjust_rest("rest")
        self.Neori.adjust_rest("stress")
        self.mystique.set_intention("critical", False)
        response = self.Neori.respond("vraag over AI filosofie en ethiek")
        self.assertIn("verdrietig", response)
        response = self.mystique.respond("vraag over AI filosofie")
        self.assertIn("blij", response)

if __name__ == '__main__':
    unittest.main()