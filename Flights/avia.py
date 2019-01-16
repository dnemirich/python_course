import sys


class Flight:
    def __init__(self):
        self._from = ''
        self.to = ''
        self.departure = ''
        self.arrival = ''
        self.cost = 0

    def __rep__(self):
        return "From: {} \nTo: {} \nDeparture: {} \nArrival: {} \nCost: ${}\n".format(self._from, self.to, self.departure, self.arrival, self.cost)


class Booking_system:
    def __init__(self):
        self.flights = []

    def flights_list(self):
        with open('flights-Nemirich.av') as data_file:
            lines = data_file.read()
            for line in lines:
                if "From" in line:
                    flight = Flight()
                    flight._from = line.split(':')[1].strip()
                elif "To" in line:
                    flight.to = line.split(':')[1].strip()
                elif "Departure" in line:
                    flight.departure = line.split(':')[1].strip()
                elif "Arrival" in line:
                    flight.arrival = line.split(':')[1].strip()
                elif "Cost" in line:
                    flight.cost = int(line.split(':')[1].replace('$', '').
                                      strip())

                self.flights.append(flight)

    def add(self, flight):
        self.flights.append(flight)
        with open('flights-Nemirich.av', 'a') as data_file:
            for flight in self.flights:
                data_file.write("\nFrom: {0}\nTo: {1}\nDeparture: {2}\nArrival: {3}\nCost: ${4}\n\n".format(flight._from, flight.to, flight.departure, flight.arrival, flight.cost))

    def find(self, _from, to):
        pass

    def cheap(self, _from, to):
        pass


def main():
    flights = Booking_system()
    cmd = sys.argv[1]
    try:
        if cmd == "add":
            flight = Flight()
            flight._from = sys.argv[2]
            flight.to = sys.argv[3]
            flight.departure = sys.argv[4]
            flight.arrival = sys.argv[5]
            flight.cost = int(sys.argv[6])
            flights.add(flight)
        else:
            print("No such command '{command}'.".format(cmd=cmd))
    except ValueError:
        print("Wrong argument form.")


if __name__ == '__main__':
    main()
