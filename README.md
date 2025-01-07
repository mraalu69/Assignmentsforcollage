

# Centrala Underground Ticketing System

## Overview

The Centrala Underground Ticketing System is a Python-based application that allows users to view stations, select travel routes, and generate tickets based on their journey details. The system supports multiple traveler types and calculates ticket prices based on the zones traveled.

## Features

- View available stations by zone.
- Select starting and destination stations.
- Specify the number of travelers for each traveler type (Adult, Child, Senior, Student).
- Calculate the fare based on the number of zones traveled.
- Generate a formatted ticket with the journey details.

## Requirements

To run the Centrala Underground Ticketing System, you need Python 3.x installed.

## Installation

1. Clone or download the repository.
2. Navigate to the project directory in your terminal.
3. Ensure you have Python 3.x installed. You can check this by running:
   ```
   python --version
   ```
4. If needed, create a virtual environment:
   ```
   python -m venv venv
   ```
5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
6. No additional dependencies are required, as the system uses Python’s built-in libraries.

## Usage

1. Run the system using:
   ```
   python ticket_system.py
   ```
2. The system will present the following options:
   - **1**: View available stations, grouped by zone.
   - **2**: Buy a ticket by selecting a starting station, destination, and the number of travelers for each type (Adult, Child, Senior, Student).
   - **3**: Exit the system.

### Example Flow:
- The system will guide you through selecting your journey, including starting and destination stations.
- You will then specify the number of travelers for each type.
- Finally, a ticket will be generated and displayed, showing the journey details and the total price.

## Ticket Generation

Once a ticket is generated, the system outputs a formatted ticket with the following details:
- Date and time of ticket generation
- Starting and destination stations with zone information
- Number of zones traveled
- Breakdown of ticket prices for each traveler type
- Total price of the journey

## Code Structure

- **Station Class**: Represents a train station, storing its name and zone.
- **TicketSystem Class**: Contains methods to manage stations, calculate fares, and generate tickets.
- **Main Program**: Provides a user interface through the command line to interact with the system.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.
