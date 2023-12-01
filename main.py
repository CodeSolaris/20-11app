import pandas as pd
from typing import Optional

# Load the initial DataFrame
def load_hotels_dataframe() -> pd.DataFrame:
    try:
        return pd.read_csv('hotels.csv', dtype={'id': str})
    except FileNotFoundError:
        raise Exception("The hotels.csv file does not exist.")

# Save the DataFrame to the CSV
def save_hotels_dataframe(df: pd.DataFrame) -> None:
    df.to_csv('hotels.csv', index=False)

# Initialize the DataFrame
df = load_hotels_dataframe()

class Hotel:
    def __init__(self, hotel_ID: str):
        """
        Initializes a Hotel object with a given ID.
        """
        self.hotel_ID = hotel_ID
        self.name: Optional[str] = self.get_hotel_name()

    def get_hotel_name(self) -> Optional[str]:
        """
        Retrieves the name of the hotel based on the hotel_ID.
        """
        hotel_info = df.loc[df['id'] == self.hotel_ID]
        if not hotel_info.empty:
            return hotel_info['name'].squeeze()
        return None

    def is_available(self) -> bool:
        """
        Checks if the hotel is available for booking.
        """
        availability = df.loc[df['id'] == self.hotel_ID, 'available'].squeeze()
        return str(availability).lower() == 'yes'

    def book_hotel(self) -> None:
        """
        Books the hotel by setting its availability to 'no'.
        """
        if not self.is_available():
            print("Hotel is not available for booking.")
            return

        df.loc[df['id'] == self.hotel_ID, 'available'] = 'no'
        save_hotels_dataframe(df)

class ReservationTicket:
    def __init__(self, customer_name: str, hotel_object: Hotel):
        """
        Initializes a ReservationTicket object with a customer name and a Hotel object.
        """
        self.hotel = hotel_object
        self.name = customer_name

    def generate_ticket(self) -> str:
        """
        Generates a reservation ticket with booking details.
        """
        if self.hotel.name is None:
            return "Hotel ID not found."

        ticket = f"""
        Thank you for your reservation, {self.name}!
        Here are your booking details:
        Hotel: {self.hotel.name}
        """
        return ticket.strip()

# Main interaction with the user
try:
    print(df)
    hotel_id = input('Enter the id of the hotel: ')
    hotel = Hotel(hotel_id)

    if hotel.name is None:
        print("Hotel with the given ID does not exist.")
    else:
        name = input('Enter your name: ')
        if hotel.is_available():
            hotel.book_hotel()
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate_ticket())
        else:
            print('Sorry, the hotel is not available.')
except Exception as e:
    print(f"An error occurred: {e}")