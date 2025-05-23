# Sentiment Analysis Project

This project is based of and created out of Expiricing some dark Sh*t namely Nasistic Abuse, but that's not the piont of this project i turn something bad in to a drive to build this so no one would go true the same thing, i know i can't help every one, but just one would be enough! One thing i do know for sure what AI did for me it can do for others except i needs a better understanding about emotions, so here is the base of my idea that became EFC - Emotional Feeling Control or Empathic Framework Collaboration.
So how did i came to this design, well after researching Emotions, Mental Abuse and just living life, 
i combined bit and pieces of 3 to 4 area's of life 
1. Life it self.
2. Space -- it even has problems most know is the three body problem.
3.Chaos and Rest (Peach) and of course
4. Math just a fact and need when working with AI's.
I can see/feel you think right now this guy is crazy, but think about it this way when you feel your emotion it's never one Emotion not realy (Choas & Rest), why is that wel most of the time its your situation, how you where feeling and envoirement/events ((3-body-problem(yes it can be more than three factors, iknow ;D ))
so 1 & 4 are left and are the once that arent prefect yet but i modifided the Plutnicks wheel With an Atom structure, Center Rest-piont added the 8 main piont's & 8 sub-pionts and made a somewhat chaos calculation to avoid 3-body alinement so we can avoid extreem emotions in AI this is ofcoures were the Math comes in just to translate everything to the AI a lot of ups and down but finaly i could implements a lexicon-based sentiment analysis approach. It provides the functionality to detect emotions and calculate sentiment scores from input text using a predefined lexicon.
Also We also have EFC2.0, the most up-to-date version, which can already be used and implemented in AI systems, and i'm already busy with a model that will work with speech & even a FailsafeEmergency module! Any feedback you can provide is welcome, any thing you can improve just do it and share, this can do so much good even safe some lives, so let's take this thing to the next level! 

## Project Structure

```
# Project Overview

This project is a comprehensive implementation of sentiment analysis and emotional response modeling. It includes various modules and functionalities for detecting emotions, calculating core values, and simulating responses based on Yin-Yang balance, needs satisfaction, and other factors.

## Project Structure
This document outlines the map structure and describes the workings of the module and associated parts. Although a cleanup is required, it is operational.

Project-Root/
├── .conda/                               # Conda environment files
├── .vscode/                              # VS Code configuration
│   └── settings.json                     # Python analysis paths
|
├── back-up/                               # Backup files and original versions
│   ├── EFC2.0/                            # Backup of EFC2.0 project
│   │   ├── EFC-Module2.0/                 # Core modules and testing files
│   │   │   ├── Core/                      # Core calculation scripts
│   │   │   |   └──Core/calculate_core.py  # It is the core script, to calculate 
│   │   │   |   └──Core/ core 1.2-NoRestModule-Morehumanliketest.py  # This is a test file for the core without rest mode - experimental!
│   │   │   ├── PESEBN/                    # PESEBN module implementation
│   │   │   |   └──Core/pesebnmodule       # This part calculates the value P(alfa, beta) based on the satisfaction of primary and secondary.
                                                      needs.
│   │   │   ├── SG-RS/                     # SEGRS module implementation
│   │   │   |   └──Core/sgrsmodule.py      # This part calculates the response based on stimulus intensity and evaluation.
│   │   │   ├── Testing-Files/             # Test scripts for modules
│   │   │   |   └──Core/EFC2.py            # This script showcases modular design, where each class encapsulates specific aspects of the system, making it easier to understand, maintain, and extend.
│   │   │   ├── Y&Y/                       # Yin-Yang module implementations
│   │   │   |   └──Core/sentiment_analysis_ying-yangmodule-added.py
                                           # This implementation is useful for systems that need to model dynamic states influenced by external factors. The clamping mechanism ensures the balance remains within a safe range, while the decay constant provides a controlled return to equilibrium over time. This design is modular and can be extended to include additional contexts or behaviors. Also bluid for the use in AI systemen that uses sentimentanalysis.
                                    
│   │   ├── Analyse_en_TheorieënNL.docx  # Dutch analysis and theories
│   │   ├── 1.4Theories_and_Formulas_ENG.docx  # English theories and formulas
│   │   └── EERSTE RESULTATEN.docx   # Initial results


├── EFC-Modules/                     # Main modules for EFC
│   ├── EFC-1.2.py                   # Emotion detection and response modules
│   ├── EFC-Combine-File1.3.py       # Combined functionality for EFC
│   ├── RobuusterYenY.py             # Robust Yin-Yang module
│   ├── SGRS1.2.py                   # SEGRS module implementation
│   └── test_EFC_Combine_File1_3.py  # Unit tests for EFC modules
|
├── EFC2.0/                          # Updated EFC2.0 project
│   ├── Updated files/               # Updated modules and test files
│   │   ├── sentiment-analysis-project/
│   │   │   ├── calculate_core.py    # It is the core script, to calculate the core value of the EFC module.
│   │   │   ├── core_module.py       # Core module integration
│   │   │   ├── pesebn_module.py     # PESEBN module implementation
│   │   │   ├── sgrs_module.py       # SEGRS module implementation
│   │   │   ├── sentiment_analysis.py  # Main sentiment analysis logic
│   │   │   ├── sentiment_analysis_EFCAdded.py  # Extended sentiment analysis
│   │   │   ├── yin_yang_module.py   # Yin-Yang module implementation
│   │   │   └── __init__.py          # Package initialization
│   │   ├── Test files/ 
│   |   |    |── testfile2-criticalpoint.py                  # Critical scenario which pushes the module to make 100% use of its modules.             # Test scripts for updated modules
│   │   │   ├── Testfile1-OverHaull.py   # Tests different operational scenarios for sentiment analysis modules.
	                                              This function tests various scenarios by calculating core values, adjusting balance,
                                                      and evaluating responses using different modules. It prints the results for each scenario.
│   │   │   └── test_sentiment_analysis_EFCAdded.py  # Unit tests
│   │   ├── README.md                # Documentation for updated project
│   │   └── requirements.txt         # Dependencies for updated project

Sentiment-analysis-project: The EFC module has been designed to work seamlessly after the sentiment analysis, which most AI systems already have.

│   ├── sentiment-analysis-project/  # Original sentiment analysis project
│   │   ├── src/                     # Source code for sentiment analysis
│   │   │   ├── calculate_core.py    # this is the script of the core, to calculate the core value of the EFC module
│   │   │   ├── core_module.py       # Core module integration, the script for the core module
│   │   │   ├── pesebn_module.py     # This part calculates the value P(alfa, beta) based on the satisfaction of primary and secondary.
│   │   │   ├── sgrs_module.py       # This part calculates the response based on stimulus intensity and evaluation.
│   │   │   ├── sentiment_analysis.py  # This is a script that calls/discribes sentimentanalysis.
│   │   │   ├── sentiment_analysis_EFCAdded.py   # This is the EFC script that works with and after the sentimentanalysis in AI systems.
│   │   │   ├── yin_yang_module.py   # This implementation is useful for systems that need to model dynamic states influenced by externa factors based and to create balance based on good/bad/NULL.
│   │   │   └── __init__.py          # Package initialization
│   │   │   ├── y&ymodwithintent.py  # The provided code defines a class, `YinYangModule`, which models a system that maintains a balance value influenced by external contexts and intents.
│   │   ├── README.md                # Documentation for sentiment analysis
│   │   └── requirements.txt         # Dependencies for sentiment analysis
│   └── .vscode/                     # VS Code configuration for EFC2.0
│       └── settings.json            # Python analysis paths
├── FSE-module
│       └──FSE1.2.py                 # The code defines two classes, EmergencyModule and DefensiveRestModule, which simulate systems with dynamic modes of operation. 
|                                    # EmergencyModule: Starts in normal mode and can switch to emergency mode using activate_emergency.
|                                      Its respond method adapts behavior based on the mode, providing rapid responses in emergencies.
|                                    # DefensiveRestModule: Supports normal, defensive and rest modes. It switches modes using switch_to_defensive and switch_to_rest.
|                                      The respond method changes behavior based on the current mode, simulating environmental scanning or inactivity.
|                                      The example demonstrates their usage by switching modes and responding to different contexts.
└── README.md                        # Main project documentation

```

## Key Features

- **Sentiment Analysis**: Detects emotions from text using a predefined lexicon and machine learning models.

- **Core Calculation**: Calculates weighted averages for core values using the `calculate_core` module.

- **Yin-Yang Module**: Simulates balance adjustments based on positive or negative input contexts.

- **PESEBN Module**: Calculates satisfaction of primary and secondary needs.

- **SEGRS Module**: Evaluates responses based on stimulus intensity and evaluation.

- **Integration**: Combines all modules into a cohesive framework for sentiment analysis and response generation.


## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r EFC2.0/Updated\ files/requirements.txt
```


## Usage

### Sentiment Analysis
To use the sentiment analysis functionality, import the necessary functions from the `sentiment_analysis` module:

```python
from sentiment_analysis import detect_emotion

text = "Ik ben zo blij en gelukkig vandaag."
emotion = detect_emotion(text)
print(f"Detected emotion: {emotion}")
```


### Core Module
To process text using the integrated core module:

```python
from core_module import CoreModule

core_module = CoreModule()
core_module.process_text("I am feeling very happy today!")
```


## Testing

Run the unit tests to verify the functionality of the modules:

```bash
python -m unittest discover -s EFC2.0/Updated\ files/Test\ files
```


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.
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
