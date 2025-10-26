# hospital/__init__.py
from .patient import register_patient
from .doctor import add_doctor
from .appointment import book_appointment, get_appointments_for_doctor