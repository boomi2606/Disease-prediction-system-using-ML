import pandas as pd
import random

# Symptoms List
symptoms = [
    "Fever",
    "Cough",
    "Cold",
    "Headache",
    "Vomiting",
    "Nausea",
    "Fatigue",
    "Body_Pain",
    "Chest_Pain",
    "Shortness_of_Breath",
    "Loss_of_Taste",
    "Loss_of_Smell",
    "Diarrhea",
    "Constipation",
    "Skin_Rash",
    "Dizziness",
    "Back_Pain",
    "Joint_Pain",
    "Sore_Throat",
    "Runny_Nose",
    "Sweating",
    "Chills",
    "Abdominal_Pain",
    "Weight_Loss",
    "Blurred_Vision",
    "Frequent_Urination",
    "High_BP",
    "Low_BP",
    "Anxiety",
    "Depression",
    "Insomnia",
    "Memory_Loss",
    "Ear_Pain",
    "Eye_Redness",
    "Tooth_Pain",
    "Swelling",
    "Itching",
    "Heartburn",
    "Weakness",
    "Dehydration"
]

# Disease Symptom Mapping
disease_map = {
    "Flu": ["Fever", "Cough", "Headache", "Fatigue", "Body_Pain"],
    "Common_Cold": ["Cold", "Runny_Nose", "Cough", "Sore_Throat"],
    "COVID19": ["Fever", "Cough", "Loss_of_Taste", "Loss_of_Smell", "Fatigue"],
    "Dengue": ["Fever", "Headache", "Body_Pain", "Joint_Pain", "Chills"],
    "Malaria": ["Fever", "Sweating", "Chills", "Headache"],
    "Typhoid": ["Fever", "Weakness", "Abdominal_Pain", "Headache"],
    "Migraine": ["Headache", "Nausea", "Blurred_Vision"],
    "Pneumonia": ["Fever", "Chest_Pain", "Cough", "Shortness_of_Breath"],
    "Asthma": ["Shortness_of_Breath", "Chest_Pain", "Cough"],
    "Bronchitis": ["Cough", "Chest_Pain", "Fatigue"],
    "Hypertension": ["High_BP", "Headache", "Dizziness"],
    "Diabetes": ["Frequent_Urination", "Weight_Loss", "Fatigue"],
    "Anemia": ["Weakness", "Fatigue", "Dizziness"],
    "Food_Poisoning": ["Vomiting", "Nausea", "Diarrhea"],
    "Gastritis": ["Heartburn", "Nausea", "Abdominal_Pain"],
    "Arthritis": ["Joint_Pain", "Swelling", "Body_Pain"],
    "Depression": ["Depression", "Fatigue", "Insomnia"],
    "Anxiety_Disorder": ["Anxiety", "Insomnia", "Sweating"],
    "Insomnia": ["Insomnia", "Fatigue"],
    "Conjunctivitis": ["Eye_Redness", "Itching"],
    "Ear_Infection": ["Ear_Pain", "Fever"],
    "Kidney_Stone": ["Back_Pain", "Vomiting", "Abdominal_Pain"],
    "UTI": ["Frequent_Urination", "Fever", "Abdominal_Pain"],
    "Skin_Allergy": ["Skin_Rash", "Itching"],
    "Heart_Disease": ["Chest_Pain", "Shortness_of_Breath", "Sweating"]
}

records = []

for disease, disease_symptoms in disease_map.items():

    for _ in range(200):  # 25 diseases x 200 = 5000 records

        row = {symptom: 0 for symptom in symptoms}

        # Main symptoms
        for symptom in disease_symptoms:
            row[symptom] = 1

        # Random noise symptoms
        noise = random.sample(symptoms, random.randint(1, 4))

        for symptom in noise:
            row[symptom] = 1

        row["Disease"] = disease

        records.append(row)

df = pd.DataFrame(records)

df.to_csv("disease_dataset.csv", index=False)

print("Dataset Generated Successfully")
print("Shape:", df.shape)