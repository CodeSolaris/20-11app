import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    def __init__(self, hotel_ID):
        self.hotel_ID = hotel_ID

    @staticmethod
    def is_available(self):
        """check if hotel is available"""
        availability = df.loc[df.hotel_id == self.hotel_ID, 'available'].squeeze()
        return True if availability == 'yes' else False

    def book_hotel(self):
        """Book a hotel by changing availability to 'no'"""
        df.loc[df.hotel_id == self.hotel_ID, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_name):
        self.hotel = hotel_name
        self.name = customer_name

    def generate_ticket(self):
        pass


print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
name = input('Enter your name: ')

if hotel.is_available():
    hotel.book_hotel()
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate_ticket())
else:
    print('Sorry, the hotel is not available')
