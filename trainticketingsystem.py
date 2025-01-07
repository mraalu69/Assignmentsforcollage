from datetime import datetime
import json
from typing import Dict, List, Tuple

class Station:
    def __init__(self, name: str, zone: int):
        self.name = name
        self.zone = zone

class TicketSystem:
    def __init__(self):
        # Initialize with some example stations
        self.stations = {
            "Central": Station("Central Station", 1),
            "North": Station("North Station", 2),
            "East": Station("East Station", 2),
            "South": Station("South Station", 3),
            "West": Station("West Station", 3),
            "Airport": Station("Airport Station", 4)
        }
        
        self.prices = {
            "Adult": 21.05,
            "Child": 14.10,
            "Senior": 10.25,
            "Student": 17.50
        }

    def get_zones(self) -> set:
        """Return all unique zones in the system."""
        return {station.zone for station in self.stations.values()}

    def display_stations(self) -> None:
        """Display all stations grouped by zone."""
        zones = {}
        for station in self.stations.values():
            if station.zone not in zones:
                zones[station.zone] = []
            zones[station.zone].append(station.name)
        
        print("\nStations by Zone:")
        for zone in sorted(zones.keys()):
            print(f"\nZone {zone}:")
            for station in sorted(zones[zone]):
                print(f"  - {station}")

    def calculate_zones_traveled(self, start_zone: int, end_zone: int) -> int:
        """Calculate number of zones traveled including start and end zones."""
        return abs(end_zone - start_zone) + 1

    def calculate_price(self, zones: int, travelers: Dict[str, int]) -> float:
        """Calculate total price based on zones and number of each traveler type."""
        total = 0
        for traveler_type, count in travelers.items():
            price = self.prices[traveler_type] * zones * count
            total += price
        return round(total, 2)

    def generate_ticket(self, start_station: str, end_station: str, 
                       travelers: Dict[str, int]) -> str:
        """Generate a formatted ticket with all journey details."""
        start = self.stations[start_station]
        end = self.stations[end_station]
        zones = self.calculate_zones_traveled(start.zone, end.zone)
        total_price = self.calculate_price(zones, travelers)
        
        ticket = f"""
===========================================
       CENTRALA UNDERGROUND TICKET        
===========================================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

From: {start_station} (Zone {start.zone})
To: {end_station} (Zone {end.zone})
Zones traveled: {zones}

Travelers:"""
        
        for traveler_type, count in travelers.items():
            if count > 0:
                price = self.prices[traveler_type] * zones * count
                ticket += f"\n{traveler_type}: {count} x {self.prices[traveler_type]} × {zones} = €{price:.2f}"
        
        ticket += f"\n\nTotal Price: €{total_price:.2f}"
        ticket += "\n==========================================="
        return ticket

def main():
    system = TicketSystem()
    
    guide = """
    Hello, Travellers!

    Welcome to the Centrala Underground Ticketing System.
    Please follow the guide below to select your destination:

    - Enter 'Central' for "Central Station" (Zone 1).
    - Enter 'North' for "North Station" (Zone 2).
    - Enter 'East' for "East Station" (Zone 2).
    - Enter 'South' for "South Station" (Zone 3).
    - Enter 'West' for "West Station" (Zone 3).
    - Enter 'Airport' for "Airport Station" (Zone 4).

    We hope you have a pleasant journey!
    """

    while True:
        print("\nCentrala Underground Ticketing System")
        print("1. View Stations")
        print("2. Buy Ticket")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            system.display_stations()
            
        elif choice == "2":
            # Display guide and stations
            print(guide)
            system.display_stations()
            
            # Get journey details
            start_station = input("\nEnter starting station: ")
            while start_station not in system.stations:
                print("Invalid station. Please try again.")
                start_station = input("Enter starting station: ")
                
            end_station = input("Enter destination station: ")
            while end_station not in system.stations:
                print("Invalid station. Please try again.")
                end_station = input("Enter destination station: ")
            
            # Get traveler counts
            travelers = {}
            for traveler_type in system.prices.keys():
                while True:
                    try:
                        count = int(input(f"Number of {traveler_type} travelers: "))
                        if count >= 0:
                            travelers[traveler_type] = count
                            break
                        print("Please enter a positive number.")
                    except ValueError:
                        print("Please enter a valid number.")
            
            # Generate and print ticket
            ticket = system.generate_ticket(start_station, end_station, travelers)
            print(ticket)
            
        elif choice == "3":
            print("Thank you for using Centrala Underground Ticketing System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
