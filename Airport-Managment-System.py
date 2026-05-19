"""
Airport Management System
Built with Object-Oriented Programming (OOP) in Python
"""

class Flight:
    def __init__(self, flight_no, destination):
        self.flight_no = flight_no
        self.destination = destination

    def display(self):
        print(f"  Flight No: {self.flight_no} | Destination: {self.destination}")


class Passenger:
    def __init__(self, name, flight_no):
        self.name = name
        self.flight_no = flight_no

    def display(self):
        print(f"  Name: {self.name} | Flight No: {self.flight_no}")


class AirportSystem:
    def __init__(self):
        self.flights = []
        self.passengers = []

    def add_flight(self):
        flight_no = input("\nEnter Flight No: ")
        destination = input("Enter Destination: ")
        flight = Flight(flight_no, destination)
        self.flights.append(flight)
        print("\n Flight added successfully!")

    def view_flights(self):
        if not self.flights:
            print("\nNo flights available.")
        else:
            print("\n------ Flight List ------")
            for flight in self.flights:
                flight.display()

    def book_ticket(self):
        name = input("\nEnter Passenger Name: ")
        flight_no = input("Enter Flight No: ")
        for flight in self.flights:
            if flight.flight_no == flight_no:
                passenger = Passenger(name, flight_no)
                self.passengers.append(passenger)
                print("\n Ticket booked successfully!")
                return
        print("\n Flight not found.")

    def view_passengers(self):
        if not self.passengers:
            print("\nNo passengers found.")
        else:
            print("\n------ Passenger List ------")
            for p in self.passengers:
                p.display()

    def run(self):
        print("-" * 40)
        print("\n Welcome to National Airport System of Pakistan \n")
        print("-" * 40)

        while True:
            print("\n1. Add Flight")
            print("2. View Flights")
            print("3. Book Ticket")
            print("4. View Passengers")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.add_flight()
            elif choice == '2':
                self.view_flights()
            elif choice == '3':
                self.book_ticket()
            elif choice == '4':
                self.view_passengers()
            elif choice == '5':
                print("\nExiting System. Thanks for visiting!\n")
                break
            else:
                print("\n Invalid choice. Try again.")


airport = AirportSystem()
airport.run()