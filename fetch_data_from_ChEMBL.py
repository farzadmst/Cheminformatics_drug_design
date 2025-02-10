from chembl_webresource_client.new_client import new_client
import pandas as pd

# Connect to ChEMBL
target = new_client.target
activity = new_client.activity

# Fetch kinase data (it could be used for all other targets too)
kinase_target = target.search('kinase')  # Search for 'kinase' targets
kinase_id = kinase_target[0]['target_chembl_id']

# Fetch bioactivity data for the first kinase target
bioactivity_data = activity.filter(target_chembl_id=kinase_id)

# Store data in a pandas dataframe
df = pd.DataFrame(bioactivity_data)

# Save the data to CSV
df.to_csv('kinase_inhibitors.csv', index=False)

print("Data saved to kinase_inhibitors.csv")