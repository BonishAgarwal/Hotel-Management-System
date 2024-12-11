from guest import Guest
from reservation_status import ReservationStatus
from room import Room


class Reservation:
    
    def __init__(self, guest: Guest, room: Room, check_in_date: str, check_out_date: str):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = ReservationStatus.CONFIRMED
    