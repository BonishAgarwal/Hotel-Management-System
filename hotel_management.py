from threading import Lock
from typing import List
from guest import Guest
from payment import Payment
from payment_strategy import PaymentStrategy
from reservation import Reservation
from reservation_status import ReservationStatus
from room import Room


class HotelManagement:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HotelManagement, cls).__new__(cls)
        
        return cls._instance

    def __init__(self):
        self.lock = Lock()
        self.rooms: List[Room] = []
        self.reservations: List[Reservation] = []
        
    def add_rooms(self, room: Room):
        self.rooms.append(room)
    
    def book_room(self, guest: Guest, room: Room, check_in, check_out):
        with self.lock:
            if room.is_room_available():
                # reserve the room for the guest
                reservation = Reservation(guest, room, check_in, check_out)
                
                # this can help me how many reservations have we done
                self.reservations.append(reservation)
            return reservation
                
    
    def check_in(self, reservation: Reservation):
        with self.lock: # to ensure that the code is executed for one thread at one single time
            if reservation and reservation.status == ReservationStatus.CONFIRMED:
                reservation.room.check_in()
    
    def check_out(self, reservation):
        with self.lock:
            reservation.room.check_out()
    
    def get_all_reservations(self):
        with self.lock:
            return self.reservations
        
        