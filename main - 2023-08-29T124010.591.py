import pandas as pd

# Load property data from a CSV file (modify this part according to your data source)
data = pd.read_csv("property_data.csv")

# Define constants
ANNUAL_DEBT_SERVICE = 120000  # Example annual debt service amount

# Calculate Debt Coverage Service (DCS) ratio for each property
data["DCS Ratio"] = data["Net Operating Income"] / ANNUAL_DEBT_SERVICE

# Filter properties with DCS ratio below a certain threshold
threshold = 1.2  # Example threshold for a good DCS ratio
good_dcs_properties = data[data["DCS Ratio"] >= threshold]

# Display properties with good DCS ratio
print("Properties with Good DCS Ratio:")
print(good_dcs_properties[["MLS Number", "DCS Ratio"]])

# Save updated data with DCS ratio to a new CSV file
data.to_csv("property_data_with_dcs.csv", index=False)
