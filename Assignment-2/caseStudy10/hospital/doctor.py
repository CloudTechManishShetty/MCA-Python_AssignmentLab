# hospital/doctor.py
DOCTORS = {}
d_id_counter = 201

def add_doctor(name, specialty):
    global d_id_counter
    DOCTORS[d_id_counter] = {"name": name, "specialty": specialty}
    print("Doctor ",name," (",specialty,") added with ID D",d_id_counter,".")
    d_id_counter += 1
    return d_id_counter - 1

def get_doctor_details(doctor_id):
    return DOCTORS.get(doctor_id)