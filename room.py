from xmlrpc.client import Boolean
from room_type import RoomType


class Room:
    
    def __init__(self, room_number: int, price: int, floor: int, type: RoomType):
        self.room_number = room_number
        self.price = price
        self.floor = floor
        self.room_type = type
        self.is_available = True
    
    def get_room_number(self):
        return self.room_number

    def get_price(self):
        return self.price
    
    def get_floor(self):
        return self.floor

    def get_room_type(self):
        return self.room_type
    
    def is_room_available(self):
        return self.is_available == True
    
    def check_in(self):
        self.is_available = False
    
    def check_out(self):
        self.is_available = True