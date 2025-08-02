# 📈 Time Series Visualizer

This project is part of the **freeCodeCamp Data Analysis with Python** certification. It analyzes time series data of daily page views for the freeCodeCamp forum between May 2016 and December 2019, and creates three insightful visualizations:

---

## 📊 Visual Outputs

1. **Line Plot** (`line_plot.png`)  
   - Shows overall trend of page views over time  
   - Highlights seasonal dips and growth

2. **Bar Plot** (`bar_plot.png`)  
   - Displays average monthly page views for each year  
   - Helps compare activity across years

3. **Box Plot** (`box_plot.png`)  
   - Includes both year-wise and month-wise distributions  
   - Reveals variability and outliers in the data

---

## 🧰 Tools & Libraries Used

- Python 3.13  
- `matplotlib` & `seaborn` for plotting  
- `pandas` for data manipulation  
- `unittest` for test validation (`test_module.py`)

---

## ✅ Project Requirements

- Cleaned data to remove outliers beyond 2.5% to 97.5% range  
- Each plot includes proper axis labels and titles  
- Visuals exported as `.png` files for easy reference

---

## 🚀 Run Locally

To generate the plots:
```bash
python main.py
