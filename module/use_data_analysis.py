# Using the data analysis module
from data_analysis import DataAnalyzer, calculate_mean, calculate_median

# Using the DataAnalyzer class
data = [12, 45, 33, 27, 89, 45, 18, 62, 39, 51]
analyzer = DataAnalyzer(data)

# Data summary statistics
summary = analyzer.get_summary()
print("Data Summary:")
for key, value in summary.items():
    print(f"- {key}: {value}")

# Using individual functions
print(f"\nMean: {calculate_mean(data)}")
print(f"Median: {calculate_median(data)}")

# Data filtering
filtered_data = analyzer.filter_data(lambda x: x > 40)
print(f"\nValues greater than 40: {filtered_data}")
print(f"Mean of filtered data: {calculate_mean(filtered_data)}")