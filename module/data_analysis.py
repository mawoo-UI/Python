"""Data analysis utility module"""

def calculate_mean(numbers):
    """Calculate the average of a list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median value of a list."""
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def calculate_variance(numbers):
    """Calculate the variance of a list."""
    if not numbers or len(numbers) < 2:
        return None
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std_deviation(numbers):
    """Calculate the standard deviation of a list."""
    variance = calculate_variance(numbers)
    if variance is None:
        return None
    return variance ** 0.5

class DataAnalyzer:
    """Class for data analysis"""
    
    def __init__(self, data=None):
        self.data = data or []
    
    def load_data(self, data):
        """Load data."""
        self.data = data
    
    def get_summary(self):
        """Return summary statistics of the data."""
        if not self.data:
            return "No data available."
        
        return {
            "count": len(self.data),
            "sum": sum(self.data),
            "mean": calculate_mean(self.data),
            "median": calculate_median(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "std_dev": calculate_std_deviation(self.data)
        }
    
    def filter_data(self, condition_func):
        """Filter data based on a condition function."""
        return [item for item in self.data if condition_func(item)]