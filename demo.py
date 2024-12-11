from guest import Guest
from hotel_management import HotelManagement
from room import Room
from room_type import RoomType


def main():
    
    hm_service = HotelManagement()
    
    room1 = Room(101, 1000, 1, RoomType.DELUXE)
    room2 = Room(102, 2000, 1, RoomType.DOUBLE)
    room3 = Room(103, 3000, 1, RoomType.SINGLE)
    room4 = Room(104, 1000, 1, RoomType.DELUXE)
    
    hm_service.add_rooms(room1)
    hm_service.add_rooms(room2)
    hm_service.add_rooms(room3)
    hm_service.add_rooms(room4)
    
    guest = Guest("Bonish", "email@gmail.com", "123456")
    
    reservation = hm_service.book_room(guest, room1, "11/24", "12/24")
    
    hm_service.check_in(reservation)
    
    print(hm_service.get_all_reservations())
    
    
    
    



if __name__ == "__main__":
    main()