# Fashion Marktanalyse & White-Space-Identifikation  
*Analyse über SSENSE, Net-a-Porter, Mr Porter und Vestiaire Collective*

## 📌 Projektübersicht
Dieses Projekt untersucht den Modemarkt über vier führende Retailer, um:

- Sortimentsverteilung  
- Preisband-Positionierung  
- Marktüberfüllung vs. White-Spaces  
- Premium- und Mid-Market-Dynamiken  

zu analysieren und strategische Handlungsempfehlungen abzuleiten.

---

## 📊 Verwendete Datensätze

| Quelle | Zeilen (ca.) | Spalten |
|--------|--------------|---------|
| SSENSE | 20.000 | 4 |
| Net-a-Porter | 23.000 | 4 |
| Mr Porter | 20.000 | 4 |
| Vestiaire Collective | 900.000 | 36 |

**Finaler Datensatz:**  
`~964.000 Zeilen × 9 Spalten`

---

## 🧹 Datenbereinigung & Standardisierung

Alle Datensätze wurden auf folgendes einheitliches Schema gebracht:

```
retailer
brand
product_name
description
category_raw
gender
price_usd
category_main
price_band
```

### Schritte:
- Vereinheitlichung der Spalten  
- Entfernen irrelevanter Felder  
- Generierung fehlender Werte  
- Erstellung der Hauptkategorie via Keyword-Matching  
- Einteilung in Preisbänder  
- Zusammenführung aller Datensätze mittels `pd.concat`  

---

## 🛠 Feature Engineering

### **1. Category Main (Hauptkategorie)**
Basierend auf Keyword-Erkennung:
- „coat“, „jacket“ → **Outerwear**
- „dress“ → **Dresses**
- „skirt“ → **Skirts**
- „knit“, „sweater“ → **Knitwear & Sweats**
- „shoe“, „boot“, „sneaker“ → **Shoes**
- „bag“ → **Bags**
- usw.

### **2. Preisbänder**
Preiskategorien:
- `<100`  
- `100–199`  
- `200–299`  
- `300–499`  
- `500–999`  
- `1000+`

---

## 📈 Durchgeführte Analysen

### **1. Sortimentsanalyse (Retailer × Kategorie)**
Vergleich der Kategorieabdeckung zwischen den Retailern.

### **2. Preispositionierung (Kategorie × Preisband)**
Analyse der Preisstruktur nach Kategorien.

### **3. White-Space-Analyse**
Identifikation unterbesetzter Segmente.

---

## 🔍 Wichtigste Erkenntnisse

- **Schuhe dominieren** mengenmäßig alle Preisbänder, besonders ≤199 USD.  
- **Outerwear ist stark Premium-getrieben**, mit hohem Anteil >500 USD.  
- **Accessoires dominieren den Einstiegsbereich (<100 USD).**  
- **Dresses bieten Potenzial im Bereich 200–299 USD.**  
- **Bags sind deutlich im Luxusbereich konzentriert**, besonders >1000 USD.  
- **Knitwear & Sweats** liegen überwiegend im Mid-Market (100–499 USD).

---

## 📂 Projektstruktur

```
├─ data/ 
│ ├─ raw/ 
│ │ ├─ ssense_dataset.csv 
│ │ ├─ mr-porter.csv 
│ │ ├─ net-a-porter.csv 
│ │ ├─ vestiaire.csv 
│ ├─ processed/  
├─ notebooks/ 
│ ├─ 01_eda_and_schema.ipynb 
│ ├─ 02_assortment_white_space.ipynb 
├─ src/ 
│ ├─ __init__.py 
│ ├─ data_prep.py 
│ ├─ plotting.py 
├─ outputs/ 
│ ├─ figures/  
│ ├─ tables/ 
├─ README.md
```

---

## 🧪 Ausführung

```bash
pip install -r requirements.txt
jupyter notebook
```

Oder via Script:

```bash
python -m src.cleaning
python -m src.analysis
```

---

## 🛠 Tech-Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Jupyter Notebook  
- VS Code  

---

## 📝 Autor
Adjina Mohamed