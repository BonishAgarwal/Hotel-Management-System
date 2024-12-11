from payment import Payment


class PaymentStrategy(Payment):
    
    def __init__(self, guest, strategy: Payment = None):
        super().__init__(guest)
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def process(self, amount):
        self.strategy.process_payment(amount)