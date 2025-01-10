# Generate a test CSV using pandas
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create date range for one year of daily data
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Create sample data
data = {
    'Date': dates,
    'Sales': np.random.normal(1000, 200, len(dates)),  # Daily sales with normal distribution
    'Units': np.random.randint(50, 150, len(dates)),   # Units sold
    'Price': np.random.uniform(20, 30, len(dates)),    # Price per unit
    'Customer_Satisfaction': np.random.uniform(3.5, 5, len(dates)),  # Customer satisfaction scores
    'Marketing_Spend': np.random.normal(500, 100, len(dates)),  # Daily marketing spend
    'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))  # Regions
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Profit
df['Profit'] = df['Sales'] - df['Marketing_Spend']

# Round numeric columns to 2 decimal places
numeric_columns = ['Sales', 'Price', 'Customer_Satisfaction', 'Marketing_Spend', 'Profit']
df[numeric_columns] = df[numeric_columns].round(2)

# Save to CSV
df.to_csv('sample_sales_data.csv', index=False)

print("Sample of the generated data:")
print(df.head())