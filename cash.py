from payment import Payment

class Cash(Payment):
    
    def __init__(self, guest):
        super().__init__(guest)
    
    def process_payment(self, amount):
        return "The amount is being processed through Cash..."