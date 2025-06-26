# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)
sns.set(style="whitegrid")

# 1. Load the dataset
file_path =(" C:\Users\HP ELITEBOOK 830 G5\OneDrive\Desktop\ecommerce-data\eda.py") # Replace with your dataset filename
df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Use 'utf-8' if needed

# 2. Basic info
print("Dataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))

# 3. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Drop or fill missing values (example: dropping rows with null in 'CustomerID')
df_cleaned = df.dropna(subset=['CustomerID'])

# Convert 'InvoiceDate' to datetime
df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'])

# Add new columns
df_cleaned['TotalAmount'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']
df_cleaned['InvoiceYearMonth'] = df_cleaned['InvoiceDate'].dt.to_period('M')

# 5. Top Countries by Revenue
country_revenue = df_cleaned.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
country_revenue.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Revenue')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Monthly Revenue
monthly_revenue = df_cleaned.groupby('InvoiceYearMonth')['TotalAmount'].sum()
plt.figure(figsize=(12, 6))
monthly_revenue.plot(marker='o')
plt.title('Monthly Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Most Sold Products
top_products = df_cleaned.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar', color='orange')
plt.title('Top 10 Most Sold Products')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Revenue by Product
top_revenue_products = df_cleaned.groupby('Description')['TotalAmount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_revenue_products.plot(kind='bar', color='green')
plt.title('Top 10 Products by Revenue')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Heatmap of Missing Values (Optional)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.tight_layout()
plt.show()
