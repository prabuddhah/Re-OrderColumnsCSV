#import the pandas library
import pandas as pd

# Replace 'Merged_Logs.csv' with the actual filename of your CSV file
input_file = 'Merged_Logs.csv'
output_file = 'Merged_ColumnArranged.csv'

# Define the desired column order
desired_columns = [
    'devname', 'srcintf', 'srcip', 'dstintf', 'dstip',
    'proto', 'dstport', 'service', 'app', 'policyname'
]

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Rearrange the columns based on the desired order
df = df[desired_columns]

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Columns rearranged and saved to {output_file}.")
