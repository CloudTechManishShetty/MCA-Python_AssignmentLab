# hospital/patient.py
PATIENTS = {}
p_id_counter = 101

def register_patient(name, age, condition):
    global p_id_counter
    PATIENTS[p_id_counter] = {"name": name, "age": age, "condition": condition}
    print("Patient ",name," registered with ID P",p_id_counter,".")
    p_id_counter += 1
    return p_id_counter - 1

def get_patient_details(patient_id):
    return PATIENTS.get(patient_id)