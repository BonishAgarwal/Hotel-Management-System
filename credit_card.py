from payment import Payment

class CreditCard(Payment):
    
    def __init__(self, guest):
        super().__init__(guest)
    
    def process_payment(self, amount):
        return "The amount is being processed through Credit Card..."