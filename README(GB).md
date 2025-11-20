# Fashion Market Assortment & White-Space Analysis  
*A Multi-Retailer Fashion Analytics Project (SSENSE, Net-a-Porter, Mr Porter, Vestiaire Collective)*

## 📌 Project Overview
This project analyzes the fashion market across four major retailers — **SSENSE**, **Net-a-Porter**, **Mr Porter**, and **Vestiaire Collective** — to understand:

- Category assortment distribution  
- Price-band positioning  
- Market saturation vs. white-spaces  
- Premium vs. mass-market dynamics  

The goal is to build a clean, unified dataset and generate insights that support strategic assortment decisions for premium fashion brands.

---

## 📊 Datasets Used

| Source | Rows (approx.) | Columns |
|--------|----------------|---------|
| SSENSE | 20,000 | 4 |
| Net-a-Porter | 23,000 | 4 |
| Mr Porter | 20,000 | 4 |
| Vestiaire Collective | 900,000 | 36 |

**Final merged dataset:**  
`~964,000 rows × 9 columns`

---

## 🧹 Data Cleaning & Standardization
All datasets were standardized to the following schema:

```
retailer
brand
product_name
description
category_raw
gender
price_usd
category_main       ← engineered column
price_band          ← engineered column
```

### Cleaning Steps:
- Unified column names  
- Dropped irrelevant fields  
- Generated missing values consistently  
- Engineered `category_main` via keyword mapping  
- Engineered `price_band` using defined price thresholds  
- Combined all datasets using `pd.concat`  

---

## 🛠 Feature Engineering

### **1. Category Main**
A standardized set of categories created using keyword matching:
- `"coat"`, `"jacket"` → **Outerwear**  
- `"dress"` → **Dresses**  
- `"skirt"` → **Skirts**  
- `"knit"`, `"sweater"`, `"hoodie"` → **Knitwear & Sweats**  
- `"shoe"`, `"boot"`, `"sneaker"` → **Shoes**  
- `"bag"` → **Bags**  
- etc.

### **2. Price Band**
Prices were segmented into strategic ranges:

- `<100`  
- `100–199`  
- `200–299`  
- `300–499`  
- `500–999`  
- `1000+`

---

## 📈 Analyses Performed

### **1. Assortment Analysis (Retailer × Category)**
Comparison of category coverage across all retailers.

### **2. Price Positioning Analysis (Category × Price Band)**
Understanding price structures by product category.

### **3. White-Space Analysis**
Identifying under-served combinations of categories and price bands.

---

## 🔍 Key Insights

- **Shoes dominate** the market across all price bands, especially in the ≤199 USD range.  
- **Outerwear is premium-heavy**, with more than 50% priced above 500 USD.  
- **Accessories dominate the sub-100 USD entry price segment.**  
- **Dresses show potential in the 200–299 USD band**, a lightly populated area.  
- **Bags are extremely premium-skewed**, with a strong concentration above 1000 USD.  
- **Knitwear & Sweats align with mid-market ranges (100–499 USD)** and are ideal for mid-premium brands.

---

## 📂 Project Structure

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

## 🧪 How to Run

```bash
pip install -r requirements.txt
jupyter notebook
```

Or run the scripts:

```bash
python -m src.cleaning
python -m src.analysis
```

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Jupyter Notebook  
- VS Code  

---

## 📝 Author
Adjina Mohamed