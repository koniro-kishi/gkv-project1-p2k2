import pandas as pd

# Load the first CSV dataset
df1 = pd.read_csv(r'C:\Users\M. Syafiq Romadhon\my-plots\honeymap\honeyproduction_1998-2021.csv')  # Replace with the path to your first CSV file

# Load the second CSV dataset
df2 = pd.read_csv(r'C:\Users\M. Syafiq Romadhon\my-plots\honeymap\states.csv')  # Replace with the path to your second CSV file

# Merge the datasets on the 'state' column
merged_df = pd.merge(df1, df2, on='state', how='left')  # Use 'left' join to keep all rows from df1

# Save the merged dataset to a new CSV file
merged_df.to_csv('merged_dataset.csv', index=False)

print("Merged dataset saved to 'merged_dataset.csv'")