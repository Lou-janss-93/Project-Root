import pandas as pd

# Creëer een document met eenvoudige datasets en oefeningen
content = {
    "Datasets": [
        {
            "Description": "Een dataset voor huisprijzen op basis van oppervlakte.",
            "Data": pd.DataFrame({
                "Oppervlakte (m²)": [50, 75, 100, 125, 150, 175, 200],
                "Prijs (x1000 €)": [100, 150, 200, 250, 300, 350, 400]
            })
        },
        {
            "Description": "Een dataset voor verkoopcijfers gebaseerd op advertentiebudget.",
            "Data": pd.DataFrame({
                "Advertentiebudget (€)": [500, 1000, 1500, 2000, 2500, 3000],
                "Verkoop (aantal)": [10, 20, 30, 40, 50, 60]
            })
        },
        {
            "Description": "Een dataset om het cijfer van leerlingen te voorspellen op basis van studietijd.",
            "Data": pd.DataFrame({
                "Studietijd (uren)": [1, 2, 3, 4, 5, 6, 7],
                "Cijfer": [50, 55, 60, 65, 70, 75, 80]
            })
        }
    ],
    "Exercises": [
        {
            "Description": "Voorspel de prijs van een huis van 160 m² met behulp van de eerste dataset."
        },
        {
            "Description": "Voorspel de verkoop bij een advertentiebudget van €3500 met behulp van de tweede dataset."
        },
        {
            "Description": "Voorspel het cijfer van een leerling die 8 uur heeft gestudeerd met behulp van de derde dataset."
        },
        {
            "Description": "Experimenteer met het toevoegen van ruis aan de datasets en kijk hoe dit de voorspellingen beïnvloedt."
        }
    ]
}

# Schrijf de content naar een Excel-bestand
with pd.ExcelWriter("/mnt/data/ML_Exercises_and_Datasets.xlsx") as writer:
    # Schrijf datasets en oefeningen naar aparte tabbladen
    for idx, dataset in enumerate(content["Datasets"], 1):
        dataset["Data"].to_excel(writer, sheet_name=f"Dataset {idx}", index=False)
    
    # Maak een samenvatting van de oefeningen in een apart tabblad
    exercises_df = pd.DataFrame([{"Oefening": ex["Description"]} for ex in content["Exercises"]])
    exercises_df.to_excel(writer, sheet_name="Oefeningen", index=False)

"/mnt/data/ML_Exercises_and_Datasets.xlsx"
