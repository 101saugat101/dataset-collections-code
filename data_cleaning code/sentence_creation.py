import pandas as pd
import random

# Load CSV files
names_df = pd.read_csv('names.csv')
surnames_df = pd.read_csv('surnames_en.csv')
provinces_df = pd.read_csv('provience_names_and_headquarters.csv')
vdc_df = pd.read_csv('vdc_municipality.csv')
zones_df = pd.read_csv('zones.csv')

# Convert surnames and zones to lists for easier access
surnames = surnames_df['Surnames'].dropna().str.strip().tolist()
zones = zones_df['zones'].dropna().str.strip().tolist()

# Initialize a list to store unique sentences
sentences = []

# Generate unique sentences
for i, person1 in names_df.iterrows():
    for j, person2 in names_df.iterrows():
        if i != j:  # Ensure person1 and person2 are different
            name1 = person1['name']
            name2 = person2['name']
            gender1 = person1['gender']
            gender2 = person2['gender']
            
            surname1 = random.choice(surnames)
            surname2 = random.choice(surnames)
            
            province1 = provinces_df.sample().iloc[0]
            province2 = provinces_df.sample().iloc[0]
            
            vdc = vdc_df.sample().iloc[0]
            zone = random.choice(zones)
            
            # Construct the sentence
            sentence = (
                f"{name1} {surname1} lives in {province1['headquarter']} which is the headquarter of {province1['name']}. "
                f"His friend {name2} {surname2} lives in {province2['headquarter']} which is the headquarter of {province2['name']} province. "
                f"Their home is in {vdc['name']}, {vdc['status']}, {vdc['district']}. Their family is from the {zone} zone."
            )
            
            sentences.append(sentence)

# Save sentences to a text file
with open('unique_sentences.txt', 'w') as f:
    for sentence in sentences:
        f.write(sentence + '\n')

print("Unique sentences have been generated and saved to 'unique_sentences.txt'.")
