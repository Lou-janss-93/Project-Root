# Sentiment Analysis Project

This project implements a lexicon-based sentiment analysis approach. It provides functionality to detect emotions and calculate sentiment scores from input text using a predefined lexicon.

## Project Structure

```
sentiment-analysis-project
├── src
│   ├── sentiment_analysis.py  # Main logic for sentiment analysis
│   └── __init__.py            # Marks the directory as a Python package
├── requirements.txt            # Lists project dependencies
└── README.md                   # Project documentation
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