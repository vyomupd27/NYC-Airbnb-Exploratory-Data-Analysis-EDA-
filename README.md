# NYC Airbnb Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project explores the **New York City Airbnb Open Data (2019)** dataset using Python. The goal is to understand Airbnb listing patterns, pricing trends, room-type preferences, host activity, and the relationship between prices and customer reviews.

Through Exploratory Data Analysis (EDA), the project identifies useful patterns and insights that can help explain the NYC Airbnb rental market.

## 🎯 Objectives

- Understand the structure and quality of the dataset.
- Analyze Airbnb prices, minimum nights, and review distributions.
- Compare listings and prices across NYC boroughs.
- Explore relationships between price, room type, and number of reviews.
- Identify hosts with multiple listings.
- Investigate the relationship between listing availability and median prices.
- Find neighbourhoods with the highest median listing prices.

## 🛠️ Technologies Used

- **Python** — Data analysis
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization

## 📂 Dataset

**Dataset:** AB_NYC_2019.csv

The dataset contains Airbnb listings in New York City, including information about:

- Listing and host IDs
- Neighbourhoods and boroughs
- Latitude and longitude
- Room types
- Nightly prices
- Minimum nights
- Number of reviews
- Reviews per month
- Host listing counts
- Availability throughout the year

**Dataset source:** [New York City Airbnb Open Data — Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

## 🔍 Analysis Performed

### Phase 1: Data Understanding and Quality Checks

- Examined dataset dimensions, columns, and data types.
- Checked missing values and duplicate records.
- Investigated missing review information.
- Explored price ranges, zero-priced listings, and expensive listings.
- Examined minimum-night requirements.
- Identified potential price outliers using the Interquartile Range (IQR) method.

### Phase 2: Univariate Analysis

- Analyzed the distribution of Airbnb room types.
- Calculated mean, median, and maximum prices.
- Visualized nightly prices using histograms.
- Investigated minimum-night requirements.
- Analyzed the distribution of listing reviews.

### Phase 3: Location Analysis

- Compared listing counts across NYC boroughs.
- Analyzed average prices by borough.
- Examined room-type preferences across boroughs.
- Compared prices by borough and room type.

### Phase 4: Relationship Analysis

- Visualized the relationship between price and number of reviews.
- Calculated the correlation between price and reviews.
- Compared median prices across room types.
- Used box plots to examine price distributions and variability.

### Phase 5: Deeper Insights and Business Questions

- Identified hosts with the largest listing portfolios.
- Counted hosts with exactly one listing and hosts with more than 10 or 50 listings.
- Compared median prices across availability groups.
- Ranked neighbourhoods by median listing price.
- Compared average review counts across room types.

## 📊 Key Findings

- **Manhattan has the highest number of listings** in the dataset, followed by Brooklyn.
- Entire homes/apartments generally have higher prices than private rooms.
- Manhattan has particularly high average prices for entire homes/apartments.
- Price and number of reviews have a very weak negative linear correlation of approximately **−0.048**.
- The median prices across the availability groups increase from $100 for low availability to $120 for high availability.
- Most hosts have a single listing, while a relatively small number manage many listings.

*Note: These findings describe patterns in the dataset. They do not establish causation, and prices may also be influenced by location, room type, and other factors.*

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Add the dataset

Download `AB_NYC_2019.csv` from the dataset source and place it in your project directory, or update the CSV file path in the Python script.

### 4. Run the script

```bash
python nyc_airbnb_eda.py
```

**Important:** In the current script, most exploratory analysis sections are commented out. Uncomment the relevant sections to execute those analyses. The neighbourhood-price ranking and average reviews by room type run by default.

## 📁 Suggested Repository Structure

```text
NYC-Airbnb-EDA/
│
├── nyc_airbnb_eda.py
├── README.md
├── requirements.txt
└── data/
    └── AB_NYC_2019.csv
```

The dataset is listed here as a suggested local folder structure; add it to the repository only if its licensing and file size permit. Alternatively, include instructions for downloading it.

## 📚 What I Learned

- Performing structured exploratory data analysis.
- Inspecting and understanding real-world datasets.
- Handling and investigating missing data.
- Using Pandas `groupby()`, aggregation, filtering, and sorting.
- Creating visualizations with Matplotlib and Seaborn.
- Interpreting distributions, outliers, and correlation.
- Translating data analysis into meaningful business observations.

## 🔮 Future Improvements

- Organize the analysis into a cleaner, reusable workflow.
- Add a dedicated visualizations folder or notebook.
- Improve neighbourhood comparisons by considering the number of listings in each neighbourhood.
- Explore additional relationships between availability, location, room type, and price.
- Build an interactive dashboard to present the findings.

## 👨‍💻 Author

**Vyom Upadhyay**

B.Tech Computer Science and Engineering | Aspiring Machine Learning Engineer and Data Scientist

---

⭐ If you find this project useful, feel free to explore the analysis and share suggestions for improvement.
