from abc import ABC, abstractmethod

from guest import Guest

class Payment(ABC):
    
    def __init__(self, guest: Guest):
        self.guest = guest
    
    @abstractmethod
    def process_payment(self, amount: float):
        pass

    def get_guest(self):
        return self.guest        