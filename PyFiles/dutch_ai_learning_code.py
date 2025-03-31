
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load a Dutch language model, such as "mBART" or another multilingual model
tokenizer = AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# Example sentences in Dutch
nederlands_tekst = "Hallo, hoe gaat het met jou vandaag?"

# Tokenize the Dutch text
inputs = tokenizer(nederlands_tekst, return_tensors="pt")

# Generate predictions or translations
outputs = model.generate(**inputs)
resultaat = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(resultaat)
