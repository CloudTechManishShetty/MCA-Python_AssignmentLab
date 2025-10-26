# main.py - Simulates Hospital Operations by importing the package
import hospital
print("--- Hospital Management System Simulation ---")

p_id_jane = hospital.register_patient("Jane Doe", 35, "Fever")
p_id_john = hospital.register_patient("John Smith", 60, "Routine Checkup")

print("-" * 20)

d_id_dr_sam = hospital.add_doctor("Dr. Sam Wilson", "Cardiology")
d_id_dr_lily = hospital.add_doctor("Dr. Lily Chen", "General Practice")

print("-" * 20)

hospital.book_appointment(p_id_jane, d_id_dr_lily, "2025-10-25 10:00")
hospital.book_appointment(p_id_john, d_id_dr_sam, "2025-10-25 11:30")
hospital.book_appointment(p_id_jane, d_id_dr_lily, "2025-10-26 09:00") # Jane's second appointment

print("-" * 20)

dr_lily_schedule = hospital.get_appointments_for_doctor(d_id_dr_lily)
print("Dr. Lily Chen's Appointments (",len(dr_lily_schedule),"):")
for app in dr_lily_schedule:
    print("  - Patient P",app['patient_id']," at ",app['date_time'])