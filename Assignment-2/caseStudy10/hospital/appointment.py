# hospital/appointment.py
APPOINTMENTS = []

def book_appointment(patient_id, doctor_id, date_time):
    if not isinstance(patient_id, int) or not isinstance(doctor_id, int):
         print("Error: Invalid ID type for booking.")
         return False
         
    appointment = {
        "patient_id": patient_id, 
        "doctor_id": doctor_id, 
        "date_time": date_time
    }
    APPOINTMENTS.append(appointment)
    print("Appointment booked for P",patient_id," with D",doctor_id," on ",date_time,".")
    return True

def get_appointments_for_doctor(doctor_id):
    return [app for app in APPOINTMENTS if app['doctor_id'] == doctor_id]