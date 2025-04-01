# Sentiment Analysis Project

This project implements a lexicon-based sentiment analysis approach. It provides functionality to detect emotions and calculate sentiment scores from input text using a predefined lexicon.
Also We also have EFC2.0, the most up-to-date version, which can already be used and implemented in AI systems, Any feedback you can provide is welcome.

## Project Structure

```
This document outlines the map structure and describes the workings of the module and associated parts. Although a cleanup is required, it is operational.

EFC2.0
├── EFC-module2.0 (map)
├── sentiment-analysis-project (map)
├── updated files (map)
├── 1.4Theories_and_formulas_eng.docx
├── Analys_enTheorieënNL.docx
└── EERSTE RESULTATEN.docx

The script explains the functionality of the module and its components, and this applies similarly to other files/maps with some modifications or experimentation.
EFC-module2.0
├── Core
│   ├── calculate_core.py                           # It is the core script, to calculate the core value of the EFC module.
│   └── core 1.2-NoRestModule-Morehumanliketest.py  # This is a test file for the core without rest mode - experimental!
├── PESEBN
│   ├── pesebnmodule                                # This part calculates the value P(alfa, beta) based on the satisfaction of primary and secondary 
                                                      needs.
├── SG-RS
│   ├── sgrsmodule.py                               # This part calculates the response based on stimulus intensity and evaluation.
├── Testing-files
│   ├── EFC2.py                                     # This script showcases modular design, where each class encapsulates specific aspects of the system,
	                                              making it easier to understand, maintain, and extend.
│   ├── testfile1-Overhaull.py                      # Tests different operational scenarios for sentiment analysis modules.
	                                              This function tests various scenarios by calculating core values, adjusting balance,
                                                      and evaluating responses using different modules. It prints the results for each scenario.
│   └── testfile2-criticalpoint.py                  # Critical scenario which pushes the module to make 100% use of its modules.
├── Y&Y
│   ├── y&ymodwithintent.py                         # The provided code defines a class, `YinYangModule`, which models a system that maintains a balance value influenced by external contexts and intents.
	                                              The balance can be adjusted dynamically based on these inputs, and it gradually returns to zero when no specific context is provided.
│   └── yiyangmodule.py                             # This implementation is useful for systems that need to model dynamic states influenced by external factors. The clamping mechanism ensures the balance 
                                                      remains within a safe range, while the decay constant provides a controlled return to equilibrium over time.
	                                              This design is modular and can be extended to include additional contexts or behaviors.

Sentiment-analysis-project: The EFC module has been designed to work seamlessly after the sentiment analysis, which most AI systems already have.
├── src
│   ├── pycache
│   ├── calculate_core.py                           # It is the core script, to calculate the core value of the EFC module
│   ├── core_module.py                              # It the script for the core module
│   ├── pesebn.py                                   # This part calculates the value P(alfa, beta) based on the satisfaction of primary and secondary 
                                                      needs.
│   ├── sentiment_analysis.py                       # This is a script that calls/discribes sentimentanalysis
│   ├── sentiment_analysis_efcadded.py              # This is the EFC script that works with and after the sentimentanalysis in AI systems 
│   ├── sgrs_module.py                              # This part calculates the response based on stimulus intensity and evaluation.
│   └── yin_yang_module.py                          # This implementation is useful for systems that need to model dynamic states influenced by external 
                                                      factors based and to create balance based on good/bad/NULL.
├── requirements.txt                                # The text file to install everything you need
└── sentiment_analysis_ying-yangmodule-added.py     # This implementation is useful for systems that need to model dynamic 
                                                      states influenced by external factors. The clamping mechanism 
                                                      ensures the balance remains within a safe range, while the decay 
                                                      constant provides a controlled return to equilibrium over time.
                                                      This design is modular and can be extended to include additional 
                                                      contexts or behaviors. Also bluid for the use in AI systemen that uses sentimentanalysis.

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
