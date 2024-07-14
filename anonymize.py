import dask.dataframe as dd
from hashlib import sha256

# Define anonymization function
def anonymize_text(text):
    return sha256(text.encode('utf-8')).hexdigest()

# Read CSV file
df = dd.read_csv('data.csv')

# Anonymize columns
df['first_name'] = df['first_name'].apply(anonymize_text, meta=('first_name', 'object'))
df['last_name'] = df['last_name'].apply(anonymize_text, meta=('last_name', 'object'))
df['address'] = df['address'].apply(anonymize_text, meta=('address', 'object'))

# Write to a new CSV file in a different directory
output_path = 'C:/Users/Amit Yadav/Documents/anonymized_data.csv'
df.repartition(npartitions=1).to_csv(output_path, single_file=True)

# Compute the Dask graph
df.compute()
