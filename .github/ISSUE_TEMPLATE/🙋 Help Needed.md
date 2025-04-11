title: "[Help] 
description: Ben vooral opzoek naar creative, innovative denkers en experten die een verschil willen maken, en helpen bouwen aan iets wat voor velen een hulp middel kan worden inplaats zomaar een tool.
labels: ["help wanted", "good first issue"]
assignees: ""

body:
  - type: markdown
    attributes:
      value: |
        Dankjewel dat je een bijdrage overweegt! Laat ons weten waar je hulp bij nodig hebt, of waarmee je wilt bijdragen.

  - type: textarea
    id: description
    attributes:
      label: Beschrijving
      description: Leg kort uit wat het probleem of de hulpvraag is.
      placeholder: Bijvoorbeeld: "Ik zoek iemand die de documentatie kan verbeteren voor de HEX-module."
      required: true

  - type: checkboxes
    id: areas
    attributes:
      label: Relevante onderdelen
      description: Op welke gebieden wil je bijdragen?
      options:
        - label: 📘 Documentatie
        - label: 🧠 AI-logica / prompt engineering
        - label: 💡 UX/UI of visueel design
        - label: 🔧 Debugging / testing
        - label: 🌐 Website / integratie
        - label: Anders (beschrijf in het tekstvak hieronder)

  - type: textarea
    id: other
    attributes:
      label: Extra toelichting of voorstel
      description: Heb je een concreet idee of een andere skill die kan helpen? Zet het hier.
