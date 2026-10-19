
# ============================================================
# NYC Airbnb Exploratory Data Analysis (EDA)
# Dataset: AB_NYC_2019.csv
# Libraries: NumPy, Pandas, Matplotlib, Seaborn
# ============================================================


# ------------------------- IMPORTS ---------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------- LOAD THE DATASET ----------------------

data = pd.read_csv(
    "C:\\Users\\vyomu\\OneDrive\\Desktop\\Python Language\\ML and Data Science Roadmap\\EDA PROJECTS\\AB_NYC_2019.csv"
)


# ============================================================
# PHASE 1: INITIAL DATA INSPECTION & DATA QUALITY
# ============================================================

# Preview the dataset
print("Data:")
print(data.head())

# Check dataset dimensions
print("\nRows and Columns in Data:")
print(data.shape)

# Inspect column data types and non-null values
print("\nData Type:")
print(data.info())

# Display column names
print("\nColumn Names:")
print(data.columns)

# Check missing values
print("\nNull Values:")
print(data.isnull().sum())
print(data.isnull().mean() * 100)

# Check for duplicate rows
print("\nDuplicated Values:")
print(data.duplicated().sum())

# Generate descriptive statistics
print("\nData Summary:")
print(data.describe())


# Investigate missing listing and host names
print(data["name"].isnull())
print(data["host_name"].isnull())

# Compare listings with zero reviews against missing last-review dates
a = (data["number_of_reviews"] == 0).sum()
b = data["last_review"].isnull().sum()

if a == b:
    print("Same")
else:
    print("Not Same")

# Inspect combinations of review counts and missing review dates
print(
    data.loc[
        (data["number_of_reviews"] == 0)
        & (data["last_review"].isnull())
    ]
)

print(
    data.loc[
        (data["number_of_reviews"] == 0)
        & (data["last_review"].notnull())
    ]
)

print(
    data.loc[
        (data["number_of_reviews"] != 0)
        & (data["last_review"].isnull())
    ]
)

# Compare missing values in review-related columns
a = data["last_review"].isnull().sum()
b = data["reviews_per_month"].isnull().sum()

print("Missing last_review:", a)
print("Missing reviews_per_month:", b)

if a == b:
    print("Counts are the same")
else:
    print("Counts are different")


# Investigate Airbnb listing prices
print(data["price"].min())
print(data["price"].max())
print((data["price"] == 0).sum())
print((data["price"] >= 1000).sum())


# Investigate minimum-night requirements
print("Minimum nights:", data["minimum_nights"].min())
print("Maximum nights:", data["minimum_nights"].max())
print(
    "Listings requiring more than 365 nights:",
    (data["minimum_nights"] > 365).sum()
)


# Inspect available room types
print("Unique room types:", data["room_type"].unique())
print(data["room_type"].value_counts())


# Detect price outliers using the IQR method
q1, q2, q3 = data["price"].quantile([0.25, 0.5, 0.75])

iqr = q3 - q1
upper_limit = q3 + 1.5 * iqr

print((data["price"] > upper_limit).sum())


# ============================================================
# PHASE 2: UNIVARIATE ANALYSIS
# ============================================================

# ----------------------- Room Type ---------------------------

print(data["room_type"].unique())
print(data["room_type"].value_counts())

sns.countplot(data=data, x="room_type")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.title("Room Type Distribution")
plt.tight_layout()
plt.show()


# -------------------------- Price ----------------------------

med = data["price"].median()
print("Median:", med)

avg = data["price"].mean()
print("Average:", avg)

maxi = data["price"].max()
print("Maximum:", maxi)

sns.histplot(data=data, x="price", bins=50)
plt.xlabel("Price per Night ($)")
plt.ylabel("Number of Listings")
plt.title("Distribution of Airbnb Nightly Prices in NYC")
plt.tight_layout()
plt.show()


# -------------------- Minimum Nights -------------------------

med1 = data["minimum_nights"].median()
print("Median:", med1)

avg1 = data["minimum_nights"].mean()
print("Average:", avg1)

maxi1 = data["minimum_nights"].max()
print("Maximum:", maxi1)

sns.histplot(data=data, x="minimum_nights", bins=50)
plt.xlabel("Minimum Number of Nights")
plt.ylabel("Number of Listings")
plt.title("Distribution of Minimum Night Requirements in NYC")
plt.tight_layout()
plt.show()


# -------------------- Number of Reviews ----------------------

med2 = data["number_of_reviews"].median()
print("Median:", med2)

avg2 = data["number_of_reviews"].mean()
print("Average:", avg2)

maxi2 = data["number_of_reviews"].max()
print("Maximum:", maxi2)

sns.histplot(data=data, x="number_of_reviews", bins=50)
plt.xlabel("Number of Reviews")
plt.ylabel("Number of Listings")
plt.title("Distribution of Airbnb Reviews in NYC")
plt.tight_layout()
plt.show()


# ============================================================
# PHASE 3: LOCATION-BASED ANALYSIS
# ============================================================

# -------------------- Listings by Borough --------------------

print(data["neighbourhood_group"].value_counts())


# ------------------- Average Price by Borough ---------------

grouped = data.groupby("neighbourhood_group")["price"].mean()
print(grouped.sort_values(ascending=False))

grouped.plot(kind="bar")
plt.xlabel("Borough")
plt.ylabel("Average Price ($)")
plt.title("Average Airbnb Price by NYC Borough")
plt.tight_layout()
plt.show()


# --------------- Room Types Across Boroughs -----------------

grouped1 = data.groupby("neighbourhood_group")["room_type"].value_counts()
print(grouped1)


# ---------- Average Price by Borough and Room Type ------------

grouped2 = data.groupby(
    ["neighbourhood_group", "room_type"]
)["price"].mean()

print(grouped2)


# ---------------- Median Price by Room Type ------------------

grouped3 = data.groupby("room_type")["price"].median()
print(grouped3)


# ============================================================
# PHASE 4: RELATIONSHIP ANALYSIS
# ============================================================

# ------------- Price vs. Number of Reviews ------------------

sns.scatterplot(x="price", y="number_of_reviews", data=data)
plt.xlabel("Price")
plt.ylabel("Number of Reviews")
plt.title("Price vs. Number of Reviews")
plt.tight_layout()
plt.show()


# ------------------- Correlation Analysis -------------------

correlation = data["price"].corr(data["number_of_reviews"])
print(correlation)


# ---------------- Price Distribution by Room Type ------------

sns.boxplot(x="room_type", y="price", data=data)
plt.ylim(0, 500)
plt.xlabel("Room Type")
plt.ylabel("Price")
plt.tight_layout()
plt.show()


# ============================================================
# PHASE 5: DEEPER INSIGHTS & BUSINESS QUESTIONS
# ============================================================

# -------------------- Busiest Hosts --------------------------

# Identify the hosts managing the most listings
busiest_host = data.groupby("host_id")[
    "calculated_host_listings_count"
].max()

sorted_busiest_host = busiest_host.sort_values(ascending=False)

print(sorted_busiest_host.head(10))


# -------------------- Host Concentration ---------------------

# Count hosts based on their listing counts
exactly_one = (busiest_host == 1).sum()
more_than_10 = (busiest_host > 10).sum()
more_than_50 = (busiest_host > 50).sum()

print("Hosts with exactly 1 listing:", exactly_one)
print("Hosts with more than 10 listings:", more_than_10)
print("Hosts with more than 50 listings:", more_than_50)


# ---------------- Availability vs. Price ---------------------

# Divide listings into availability groups
low = data[data["availability_365"].between(0, 100)]
medium = data[data["availability_365"].between(101, 200)]
high = data[data["availability_365"].between(201, 365)]

# Calculate median prices for each availability group
print("Low availability median price:", low["price"].median())
print("Medium availability median price:", medium["price"].median())
print("High availability median price:", high["price"].median())


# -------------- Most Expensive Neighbourhoods ----------------

expensive_neighbour = data.groupby("neighbourhood")["price"].median()

sorted_expensive_neighbour = expensive_neighbour.sort_values(
    ascending=False
)

print(sorted_expensive_neighbour.head(10))


# --------------- Reviews by Room Type ------------------------

reviews_by_room = data.groupby("room_type")["number_of_reviews"].mean()

sorted_reviews = reviews_by_room.sort_values(ascending=False)

print(sorted_reviews)


# ============================================================
# END OF NYC AIRBNB EXPLORATORY DATA ANALYSIS
# ============================================================
