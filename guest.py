from typing import Dict
from room import Room

class Guest:
    
    def __init__(self, name: str, email: str, contact: str):
        self.name = name
        self.email = email
        self.contact = contact
    
    def get_user(self):
        return f"Username: {self.user} | Email: {self.email} | Contact: {self.contact}"