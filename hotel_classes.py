"""
   CISC-121 2023W
   Name: Haani Syed
   Date: 2023-03-30
"""


from datetime import date, timedelta #imports

class Service:
    def __init__(self, name, cost):
     """
    -------------------------------------------------------
    Initializes a new service object with the provided cost and name.
    Use: service = Service(name, cost)
    -------------------------------------------------------
    Args:
    - name: str representing the service name
    - cost: number representing the service cost
    -------------------------------------------------------
    Atrributes:
    - name: str representing the service name
    - cost: numeric value representing the service cost
    -------------------------------------------------------
     """
     #creates object with 2 attributes
     self.name = name
     self.cost = cost



class HotelRoom:
    def __init__(self, room_number, available_date): #method
        """
        -------------------------------------------------------
        Initializing a HotelRoom object with the given room number and available date.
        Args:
        - room_number(int): hotel room's number
        - available_date(str): str representing the date on which room's available (Format: YYYY-MM-DD)
        -------------------------------------------------------
        Atrributes:
        - room_number(int): hotel room's number
        - available_date(datetime.date): str representing the date on which room's available (Format: YYYY-MM-DD)
        -------------------------------------------------------
        Calls following method:
        - setting_availability(): sets the availability status of the room
        -------------------------------------------------------
        Returns:
        None
         -------------------------------------------------------
        """
        self.room_number = room_number
        self.available_date = date.fromisoformat(available_date) #convert available date string into date object
        self.setting_availability(date.today() - timedelta(days=1)) #sets availability of room using method

    def setting_availability(self, date_of_leaving):
        """
        -------------------------------------------------------
        This method sets the availability status of the room based on the user's date of leaving.
        -------------------------------------------------------
        Args:
        - date_of_leaving(datetime.date): user's check out date/date of leaving hotel
        -------------------------------------------------------
        Return:
        None
        -------------------------------------------------------
        """
        if self.available_date <= date_of_leaving: #if available date is greater than or equal to check out date (date of leaving)
            self.available = True #showing room is now available
            self.available_date = date_of_leaving + timedelta(days=1)
        else:
            self.available = False
            #self.available_date = date_of_leaving + timedelta(days=1)

    def guest_check_in(self, some_guest):

        """
        -------------------------------------------------------
        Checks a guest into a room and updates availability

        -------------------------------------------------------
        Parameters:
        Some_guest – the guest checking in (guest object)
        Returns:
        None
        -------------------------------------------------------
        """
        if self.available:
            available_date = input('Please Re-Enter the available date you would like (YYYY-MM-DD) to confirm: ')
            date_of_leaving_input = input('Please Re-Enter date of leaving (YYYY-MM-DD) to confirm: ')
            date_of_leaving = date.fromisoformat(date_of_leaving_input)
            self.setting_availability(date_of_leaving)
            self.some_guest = some_guest
            self.available = False
            type_of_room = input('Please Re-Enter the type of room you are booking (Suite, Standard Room, Taylor Suite) to confirm: ')
            #informs user of how many days it take to clean the room after check out and before another user can book that room
            if some_guest.type_of_room == 'Suite':
                cleaning_time = '1 day'
            elif some_guest.type_of_room == 'Taylor Suite':
                cleaning_time = '2 days'
            elif some_guest.type_of_room == 'Standard Room':
                cleaning_time = '0 days'
            #print(f"Respected {some_guest.name} has been checked into the Room Number {self.room_number} from this day, {available_date}, until {some_guest.date_of_leaving} ")
            print(f"Respected {some_guest.name}, you have been checked into a {type_of_room} room at room number {self.room_number}. Your room will be clean and available on {available_date} after the previous guest checks out")
            print(f"You may enjoy your stay until {some_guest.date_of_leaving}. This room will be available again for individuals to book after {cleaning_time}")
        else:
            print(f'Respected {some_guest.name} has NOT been checked into the Room Number {self.room_number} unfortunately! ')




class Suite(HotelRoom):
    def __init__(self, room_number, available_date):
        """
        -------------------------------------------------------
        This initializes a suite object (subclass of HotelRoom) with the given room number and available date.
        The available date for a suite room is set to one day after given available date.
        -------------------------------------------------------
        Args:
        - room_number(int): hotel room's number.
        - available_date(str): the date when room becomes available (Format: YYYY-MM-DD).
        -------------------------------------------------------
        Attributes:
        - room_number(int): hotel room's number.
        - available_date(str): the date when room becomes available (Format: YYYY-MM-DD).
        By calling super(), we are initializing the attributes inherited from the base class.
        -------------------------------------------------------
        """
        super().__init__(room_number, available_date)
        self.available_date = self.available_date + timedelta(days=1) #updating available date for suite room by adding 1 (day required for it to clean before new user can book).

class StandardRoom(HotelRoom):
    def __init__(self, room_number, available_date):
        """
        -------------------------------------------------------
        Initializes a StandardRoom object (subclass of HotelRoom) with the room number and available date.
        -------------------------------------------------------
        Args:
        - room_number(int): hotel room's number.
        - available_date(str): the date when room becomes available (Format: YYYY-MM-DD).
        -------------------------------------------------------
        Attributes:
        - room_number(int): hotel room's number.
        - available_date(str): the date when room becomes available (Format: YYYY-MM-DD).
        By calling super(), we are initializing the attributes inherited from the base class.
        -------------------------------------------------------
        """
        super().__init__(room_number, available_date) #updating available date for suite room.

class TaylorSuite(HotelRoom):
    def __init__(self, room_number, available_date):
        """
        -------------------------------------------------------
        Initializing new Taylor Suite object (subclass of HotelRoom) with room number and available date.
        Available date set automatically to 2 days after provided date.
        Args:
        - room_number(int): hotel room's number.
        - available_date(str): the date when room becomes available (Format: YYYY-MM-DD).
        By calling super(), we are initializing the attributes inherited from the base class.
        -------------------------------------------------------
        """
        super().__init__(room_number, available_date) #calling constructor of parent class
        self.available_date = self.available_date + timedelta(days=2) #adds 2 days to existing available date


class Guest:
    def __init__(self, name, date_of_leaving, type_of_room):
        """
        -------------------------------------------------------
        Creates a new guest object.
        Args:
        - name(str): name of guest
        - date_of_leaving(str): the date when guest is checking out/leaving hotel, format (YYYY-MM-DD)
        - type_of_room(str): type of room guest is staying in (Standard Room, Suite, Taylor Suite)
        -------------------------------------------------------
        Attributes:
        - name(str): the name of the guest.
        - date_of_leaving(str): the date when the guest is leaving the hotel (Format: YYYY-MM-DD)
        - type_of_room(str): type of room guest is staying in (Standard Room, Suite, Taylor Suite)
        - service_name(list): a list of the services the user had used during their time at the hotel
        - service_cost(int): total cost of the services guest had during their stay.
        -------------------------------------------------------
        """
        self.name = name #assigns name argument to instance variable self.name
        self.date_of_leaving = date_of_leaving #assigns date of leaving argument to instance self.date_of_leaving
        self.type_of_room = type_of_room #assigns type_of_room to instance self.type_of_room
        self.service_name = [] #initalizes empty list
        self.service_cost = 0 #initalizes to zero

    def add_service(self, service_name, service_cost):
        """
        -------------------------------------------------------
        Adds a service to the bill of a guest
        -------------------------------------------------------
        Parameters:
        Service name – name of service (str)
        Service_cost - cost of the service (int)
        Returns: None
        -------------------------------------------------------
        """
        service = Service(service_name, service_cost) #creates new instance of Service class and assigns to variable service
        self.service_name.append(service) #appends service object to list in self.service_name
        self.service_cost = self.service_cost + service_cost #updates instance variable by adding cost of new service to existing costs

    def send_bill(self):
        """
        -------------------------------------------------------
        Based on the total services and bill total provides a
        Printed statement of all services with the total cost
        -------------------------------------------------------
        Parameters: None
        Returns: None
        -------------------------------------------------------
        """
        if self.service_name: #if statement
            print(f'Respected {self.name}, the following is your bill: ') #prints respected users bill
            for service in self.service_name: #for loop
                print(f' - {service.name}: ${service.cost}') #prints out all services and associated costs requested by user
            print(f'The total bill is: ${self.service_cost}') #prints total bill
        else:
            print('There were no services ordered unfortunately!') #if no services purchased by user.
