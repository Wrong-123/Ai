# Simple disease symptoms and treatments
disease_symptoms = {
    "Flu": ["fever", "cough", "sore throat"],
    "Cold": ["sneezing", "runny nose"],
    "Malaria": ["fever", "chills"],
    "COVID-19": ["fever", "cough", "loss of taste"]
}

disease_treatments = {
    "Flu": "Rest and drink fluids.",
    "Cold": "Stay warm and use cold medicine.",
    "Malaria": "Visit a doctor and take antimalarial medicine.",
    "COVID-19": "Isolate and consult a doctor."
}

def check_disease(symptoms):
    possible_diseases = []
    for disease, symptoms_list in disease_symptoms.items():
        for s in symptoms:
            if s in symptoms_list:
                possible_diseases.append(disease)
                break

    if not possible_diseases:
        return "No matching disease found."

    result = "Possible diseases and treatments:\n"
    for disease in possible_diseases:
        result += f"\n{disease}: {disease_treatments[disease]}"
    return result

# Input from user
user_input = input("Enter symptoms separated by commas: ").lower()
symptom_list = [s.strip() for s in user_input.split(",")]
print(check_disease(symptom_list))




