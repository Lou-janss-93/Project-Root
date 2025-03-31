# Sentiment Analysis Project

This project implements a lexicon-based sentiment analysis approach. It provides functionality to detect emotions and calculate sentiment scores from input text using a predefined lexicon.
Also We have the EFC2.0 this one is the most uptodate one an can already be used and implemented is to AI systems, Any feedback you can provide is welcome.

## Project Structure

```
this is the map structure (yes still needs a clean up, but working on it ;P)

EFC2.0
├── EFC-module2.0 (map)
├── sentiment-analysis-project (map)
├── updated files (map)
├── 1.4Theories_and_formulas_eng.docx
├── Analys_enTheorieënNL.docx
└──EERSTE RESULTATEN.docx

This scprit discribes the working of the module and the part of it, this is de same for the other files/maps with some changes or experimentation.

EFC-module2.0
├── Core
│   ├──calculate_core.py  #Its the core of the EFC module.
│   └──core 1.2-NoRestModule-Morehumanliketest.py  #This is a test file with no rest mode innit - experimental!
├── PESEBN
│   ├──pesebnmodule        #Dit deel berekend de waarde P(alfa, beta) op basis van de voldoening van primaire en secundaire behoeften.
├── SG-RS
│   ├──sgrsmodule.py       #dit deel berekend de respons op basis van stimulusintensiteit en evaluatie.
├── Testing-files
│   ├──EFC2.py             #This script showcases modular design, where each class encapsulates a specific aspect of the system,
     making it easier to understand, maintain, and extend.
│   ├──testfile1-Overhaull.py #Test different operational scenarios for sentiment analysis modules.
     this function tests various scenarios by calculating core values, adjusting balance,
     and evaluating responses using different modules. It prints the results for each scenario.
│   └── testfile2-criticalpoint.py                # Critical scenario witch pushes the module to make 100% use of its modules.
├── Y&Y
│   ├── y&ymodwithintent.py    #The provided code defines a class, `YinYangModule`, which models a system that maintains a balance value influenced by external contexts and intents.
    The balance can be adjusted dynamically based on these inputs, and it gradually returns to zero when no specific context is provided.
│   └── yiyangmodule.py        # This implementation is useful for systems that need to model dynamic states influenced by external factors. The clamping mechanism ensures the balance remains within a safe range, while the decay constant provides a controlled return to equilibrium over time.
    This design is modular and can be extended to include additional contexts or behaviors.


sentiment-analysis-project here i made the EFC module in a way that it would work right after the sentimentanalysis most AI systems already have.
├── src
│   ├──__pychace__
│   ├──calculate_core.py
│   ├──core_module.py
│   ├──pesebn.py
│   ├──sentiment_analsis.py
│   ├──sentiment_analysis_efcadded.py
│   ├──sgrs_module.py
│   └──yin_yang_module.py
├── readme.md
├── reqiurements.txt
└──sentiment_analysis_ying-yangmodule-added.py
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the sentiment analysis functionality, import the necessary functions from the `sentiment_analysis` module in your Python scripts. 

Example:

```python
from src.sentiment_analysis import detect_emotion, calculate_sentiment

text = "Ik ben zo blij en gelukkig vandaag."
emotion = detect_emotion(text)
print(f"Detected emotion: {emotion}")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
