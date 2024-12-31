import pandas as pd
import random

# Load your CSV files
names_df = pd.read_csv('names.csv')
surnames_df = pd.read_csv('surnames_en.csv')
provinces_df = pd.read_csv('provience_names_and_headquarters.csv')
vdc_df = pd.read_csv('vdc_municipality.csv')
zones_df = pd.read_csv('zones.csv')
districts_df = pd.read_csv('district_names_and_headquarters.csv')

# Convert necessary columns to lists for easier access
surnames = surnames_df['Surnames'].dropna().str.strip().tolist()
zones = zones_df['zones'].dropna().str.strip().tolist()

# Define sentence structures
sentence_structures = [
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"{n1} {s1} lives in {p1['headquarter']}, the headquarter of {p1['name']} province. "
        f"{'She' if g1 == 'girl' else 'He'} often visits {v['name']} ({v['status']}) in {v['district']} district. "
        f"{'Her' if g1 == 'girl' else 'His'} friend {n2} {s2} resides in {d['headquarters']}, the district headquarter of {d['names']} in the {z} zone."
    ),
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"In the {z} zone, {n1} {s1} and {'her' if g1 == 'girl' else 'his'} friend {n2} {s2} "
        f"often meet in {d['headquarters']}, located in the {d['names']} district. "
        f"{'She' if g1 == 'girl' else 'He'} lives near {p1['headquarter']}, the capital of {p1['name']} province."
    ),
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"The headquarter of {p1['name']} province is {p1['headquarter']}, where {n1} {s1} resides. "
        f"{'Her' if g1 == 'girl' else 'His'} friend, {n2} {s2}, lives in {v['name']} ({v['status']}) in {v['district']} district in the {z} zone."
    ),
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"{n1} {s1} and {n2} {s2} grew up in the {z} zone. Now, {n1} lives in {p1['headquarter']}, "
        f"the headquarter of {p1['name']} province, while {'her' if g2 == 'girl' else 'his'} friend resides in {d['headquarters']}."
    ),
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"{n2} {s2} lives in {v['name']} in the {z} zone. {'She' if g2 == 'girl' else 'He'} often visits {p1['headquarter']}, "
        f"the capital of {p1['name']} province, to meet {n1} {s1}."
    ),
    lambda n1, s1, g1, n2, s2, g2, p1, d, v, z: (
        f"{n1} {s1} lives near {v['name']} ({v['status']}) in {v['district']} district. "
        f"{'Her' if g1 == 'girl' else 'His'} best friend, {n2} {s2}, stays in {d['headquarters']}, the district headquarter of {d['names']} in {z} zone."
    ),
]

# Generate sentences in a loop
sentences = []
for _ in range(10000):  # Adjust the number of sentences
    # Randomly sample data
    person1 = names_df.sample().iloc[0]
    person2 = names_df.sample().iloc[0]
    while person1['name'] == person2['name']:  # Ensure unique names
        person2 = names_df.sample().iloc[0]

    surname1 = random.choice(surnames)
    surname2 = random.choice(surnames)
    province = provinces_df.sample().iloc[0]
    district = districts_df.sample().iloc[0]
    vdc = vdc_df.sample().iloc[0]
    zone = random.choice(zones)

    # Choose a random sentence structure
    structure = random.choice(sentence_structures)
    sentence = structure(
        person1['name'], surname1, person1['gender'],
        person2['name'], surname2, person2['gender'],
        province, district, vdc, zone
    )
    sentences.append({'Sentence': sentence})

# Save the sentences to a CSV file
sentences_df = pd.DataFrame(sentences)
sentences_df.to_csv('diverse_sentences.csv', index=False)

print("Generated sentences have been saved to 'diverse_sentences.csv'.")
