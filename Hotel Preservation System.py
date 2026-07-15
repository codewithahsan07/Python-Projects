import json


class Room:
    def __init__(self, room_no, room_type, price, booked=False):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.booked = booked

    def to_dict(self):
        return {
            "room_no": self.room_no,
            "room_type": self.room_type,
            "price": self.price,
            "booked": self.booked
        }


class Hotel:

    def __init__(self):
        self.rooms = [
            Room(101, "Single", 2000),
            Room(102, "Double", 3500),
            Room(103, "Luxury", 5000)
        ]
        self.load_data()


    def show_rooms(self):
        for room in self.rooms:
            status = "Booked" if room.booked else "Available"

            print("----------------")
            print("Room:", room.room_no)
            print("Type:", room.room_type)
            print("Price:", room.price)
            print("Status:", status)


    def book_room(self):
        room_no = int(input("Enter room number: "))

        for room in self.rooms:
            if room.room_no == room_no:

                if room.booked:
                    print("Room already booked")
                    return

                room.booked = True
                self.save_data()

                print("Room booked successfully!")
                return

        print("Room not found")


    def checkout(self):
        room_no = int(input("Enter room number: "))

        for room in self.rooms:
            if room.room_no == room_no:

                if not room.booked:
                    print("Room is already empty")
                    return

                room.booked = False
                self.save_data()

                print("Checkout successful!")
                print("Bill:", room.price)

                return

        print("Room not found")


    def save_data(self):
        data = [room.to_dict() for room in self.rooms]

        with open("rooms.json", "w") as file:
            json.dump(data, file)


    def load_data(self):
        try:
            with open("rooms.json", "r") as file:
                data = json.load(file)

                self.rooms = []

                for room in data:
                    self.rooms.append(
                        Room(
                            room["room_no"],
                            room["room_type"],
                            room["price"],
                            room["booked"]
                        )
                    )

        except FileNotFoundError:
            pass



hotel = Hotel()


while True:

    print("""
===== Hotel Reservation System =====

1. View Rooms
2. Book Room
3. Checkout
4. Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        hotel.show_rooms()

    elif choice == "2":
        hotel.book_room()

    elif choice == "3":
        hotel.checkout()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        

    