import pandas as pd
from sklearn.model_selection import train_test_split

# Load your dataset
data = pd.read_csv('/Users/parmikenia/Desktop/internship codes/combined_credit1 (1).csv')

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Save the training set to a CSV file
train_data.to_csv('train_data.csv', index=False)

# Save the testing set to a CSV file
test_data.to_csv('test_data.csv', index=False)

print("Training and testing datasets have been saved to 'train_data.csv' and 'test_data.csv'.")


