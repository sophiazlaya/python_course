
class Train:
    def __init__(self, route, departure_time, arrival_time, num_cars, seats_per_car):
        self.route = route
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.num_cars = num_cars
        self.seats_per_car = seats_per_car
        self.seats_booked = []

    def book_seat(self, car_num, seat_num):
        if seat_num in self.seats_booked:
            return False
        self.seats_booked.append(seat_num)
        return Ticket(self.route, self.departure_time, car_num, seat_num)

class Passenger:
    def __init__(self, name, age, gender, passport_num):
        self.name = name
        self.age = age
        self.gender = gender
        self.passport_num = passport_num

class Ticket:
    def __init__(self, route, departure_time, car_num, seat_num):
        self.route = route
        self.departure_time = departure_time
        self.car_num = car_num
        self.seat_num = seat_num
        self.price = self.calc_price()

    def calc_price(self):
        return 100

class TicketOffice:
    def __init__(self, location, working_hours):
        self.location = location
        self.working_hours = working_hours

    def sell_ticket(self, passenger, train):
        for car_num in range(1, train.num_cars+1):
            for seat_num in range(1, train.seats_per_car+1):
                ticket = train.book_seat(car_num, seat_num)
                if ticket:
                    return ticket
        return None