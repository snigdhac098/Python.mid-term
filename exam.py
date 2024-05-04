class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        inf = (id, movie_name, time)
        self._show_list.append(inf)

        self._seats[id] = []
        for i in range(self._rows):
            row_seats = []
            for i in range(self._cols):
                row_seats.append(0)
            self._seats[id].append(row_seats)

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        for seat in seats_to_book:
            row, col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat: {row}, {col}")
                continue

            if self._seats[id][row][col] == 1:
                print(f"Seat {row}, {col} is already booked.")
            else:
                self._seats[id][row][col] = 1
                print(f"Seat {row}, {col} booked successfully.")

    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for show {id} in Hall {self._hall_no}:")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col] == 0:
                    print("0", end=" ")
                else:
                    print("1", end=" ")
            print()

    def book_tickets(self, id):
        if id not in self._seats:
            print("Invalid")
            return

        row = int(input("Enter row : "))
        col = int(input("Enter col : "))

        if not (0 <= row < self._rows and 0 <= col < self._cols):
            print(f"Invalid seat: {row}, {col}")
            return

        if self._seats[id][row][col] == 1:
            print(f"Seat {row}, {col} already booked.")
        else:
            self._seats[id][row][col] = 1
            print(f"Seat {row}, {col} booked successfully.")


hall1 = Hall(rows=8, cols=8, hall_no=1)
hall1.entry_show(id="234", movie_name="Ms Dhoni", time="2:00 PM")

hall2 = Hall(rows=8, cols=8, hall_no=2)
hall2.entry_show(id="255", movie_name="Robot", time="5:00 PM")

while True:
    print("\nWelcome to Star Cinema:")
    print("1: View all Shows")
    print("2: View Available seats")
    print("3: Book Tickets")
    print("4: Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        hall1.view_show_list()
        hall2.view_show_list()
    elif ch == "2":
        show_id = input("Enter the show ID: ")
        if show_id in hall1._seats:
            hall1.view_available_seats(show_id)
        elif show_id in hall2._seats:
            hall2.view_available_seats(show_id)
        else:
            print("Invalid show ID.")
    elif ch == "3":
        show_id = input("Enter the show ID: ")
        hall1.book_tickets(show_id) if show_id in hall1._seats else hall2.book_tickets(show_id) if show_id in hall2._seats else print("Invalid show ID.")
    elif ch == "4":
        print("Thank you for visiting Star Cinema. Goodbye!")
        break
    else:
        print("Invalid choice.")