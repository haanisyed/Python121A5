"""
   Python-121 2023W
   Name: Haani Syed
   Date: 2023-03-30
"""

from datetime import date
from hotel_classes import HotelRoom, Suite
from hotel_classes import StandardRoom, TaylorSuite
from hotel_classes import Guest #imports Guest
#the above imports necessary classes from hotel_classes python file
#

def menu():
    """
    -------------------------------------------------------
    Allows the users to book a room and interact with their bookings through the various possible commands.
    Use:
    - Call 'menu' function to start the bookings at Taylor Hotel process
    - Enter the type of room you would like to book, your name, preferred dates of stay
    - Once booking is confirmed, you can use these commands/methods:
       - guest_check_in : checks user into the room
       - add_service: adds services to user's bill
       - guest_bill: informs user of their current bill at any time
    - Entering yes lets the user continue to using the commands and entering no will make the user exit the program.
    -------------------------------------------------------
    Returns:
    None
    -------------------------------------------------------
    """
    #Displays a welcome message to the user
    print('Welcome to the Taylor Hotel based in Kingston, Ontario!')
    #lines below prompt user to enter preferences in: room type, room number, their name, and dates of stay/leave
    type_of_room = input('Enter the type of room you are booking (Suite, Standard Room, Taylor Suite): ')
    room_number = input('Enter the room number which you are interested in,121 rooms in total, (There are 19 suites, 89 standard rooms, and 13 Taylor Suites) the first 19 rooms are suites, next 89 are standard, and the final 13 are Taylor Suites: ')
    name = input('Respected guest please enter your name: ')
    available_date = input('Enter the available date you would like (YYYY-MM-DD): ')
    date_of_leaving = input('Enter the date of leaving AKA check out date (YYYY-MM-DD) : ')
    guest = Guest(name, date_of_leaving, type_of_room) #creates guest object with data inputted by user
    #lines below assign a room object based on user input
    if type_of_room == 'Suite' and int(room_number) in range(1, 20): #Suites are the first 19 rooms
        room = Suite(room_number, available_date)
    elif type_of_room == 'Standard Room' and int(room_number) in range(20,109): #Standard Rooms are room20-108
        room = StandardRoom(room_number, available_date)
    elif type_of_room == 'Taylor Suite' and int(room_number) in range(21, 120):#Taylor Suites are rooms21-119
        room = TaylorSuite(room_number, available_date)
    else:
        print('Improper and Invalid room type was entered!')
        return #return
    #takes user inputs and booking system provides user with appropriate functionalities
    user_entry = None
    user_response = input('Would you like to enter a command and learn more (yes/no)? :')
    while user_entry != 4:
        while user_entry not in [1,2,3,4]:
            while user_response == 'yes':
                user_entry = int(input('Enter an integer from numbers (1-3) which call the following commands respectively(guest_check_in, add_service, send_bill): '))
                if user_entry == 1:
                    #Guest-Check In
                    room.guest_check_in(guest)
                    user_response = input('Would you like to enter a command and learn more about the offers (yes/no)? :')

                elif user_entry == 2:
                    #Adding Services
                    print('The following are the services currently offered at the hotel and their associated costs. Please note breakfast and wifi are free and complementary! - room service:$50, Movies: $40, Dinner: $45, Lunch: $45, Breakfast: $0, Laundry: $20')
                    service_name = input('Enter the name of the service you would like to use from the ones stated above: ')
                    service_cost = int(input('Enter the respective cost of the service you are using from the info stated above: '))
                    guest.add_service(service_name, service_cost)
                    add_another = None
                    while add_another not in ['yes', 'no']:
                        add_another = input('Would you like to add another service (yes/no): ')
                        if add_another == 'yes':
                            print('The following are the services currently offered at the hotel and their associated costs. Please note breakfast and wifi are free and complementary! - Room service:$50, Movies: $40, Dinner: $45, Lunch: $45, Breakfast: $0, Laundry: $20')
                            service_name = input('Enter the name of the service you would like to use from the ones stated above: ')
                            service_cost = int(input('Enter the respective cost of the service you are using from the info stated above: '))
                            guest.add_service(service_name, service_cost)
                    print('You have now added all of your services. Would you like to view your bill?')
                    view_bill = input('Enter yes to be able to view your bill. Or press any other key to exit: ')
                    if view_bill == 'yes':
                        guest.send_bill()
                elif user_entry == 3:
                    #viewing bill
                    guest.send_bill()
                    user_response = input('Would you like to enter a command and learn more about the offers (yes/no)? :')
            if user_response == 'no':
                print('Was pleasure doing business with you. We hope you have a great day!')
    else:
        print('An INVALID command was entered! ') #prints invalid command entered (not 1-3)



def main():
    """
    -------------------------------------------------------
    The main function that runs the menu for bookings at the Taylor Hotel and interacting with the booking system through various commands
    Use: Call the 'main' function to run the bookings system and to be able to interact with the booking system through commands.
    -------------------------------------------------------
    Returns: None
    -------------------------------------------------------
    """
    menu() #call to menu function


main() #call to main function
