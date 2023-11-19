# Sample user database using dictionary
user_database = {
    'user1': {'username': 'user1', 'password': 'password1', 'role': 'user'},
    'user2': {'username': 'user2', 'password': 'password2', 'role': 'user'},
    'admin': {'username': 'admin', 'password': 'adminpass', 'role': 'admin'}
}
# Sample employee id's to authenticate if the user really an admin or not'
employeeid=["emp1","emp2","emp3","emp4","emp5"]
# Sample database of flights using dictionary
flights_database = {
    'F001': {'flight_id': 'F001', 'name': 'Flight 1', 'date': '2023-11-20', 'seats_available': 60},
    'F002': {'flight_id': 'F002', 'name': 'Flight 2', 'date': '2023-11-21', 'seats_available': 60},
    'F003': {'flight_id': 'F003', 'name': 'Flight 3', 'date': '2023-11-22', 'seats_available': 60}
}

booking_database = {}
# Function to user login
def login(username, password):
    if username in user_database and user_database[username]['password'] == password:
        return user_database[username]['role']
    
    return None

# Function to user signup
def signup(username, password,role):
    
    if(role=='user'):
                if username not in user_database:
                    user_database[username] = {'username': username, 'password': password, 'role': 'user'}
                    print("Signup successful! Please login.")
                else:
                    print("Username already exists. Please choose another username.")
    elif(role=='admin'):
                emp_id=input("Enter the employee id provided to you")
                if emp_id in employeeid:
                        user_database[username] = {'username': username, 'password': password, 'role': 'admin'}
                        print("Signup successful! Please login.")
    else:
            print("The employee id is incorrect")
    return None
    

# Function to search flights
def search_flights(query):
    found_flights = []
    for flight_id, flight_details in flights_database.items():
        if query in (flight_details['name'], flight_details['date'], flight_details['flight_id']):
            found_flights.append(flight_details)
    return found_flights

# Function to book a ticket
def book_ticket(username, flight_id):
    if flight_id in flights_database and flights_database[flight_id]['seats_available'] > 0:
        if username not in booking_database:
            booking_database[username] = []
        booking_database[username].append(flights_database[flight_id])
        flights_database[flight_id]['seats_available'] -= 1
        print(f"Ticket booked successfully for {username} on {flights_database[flight_id]['name']}!")
    else:
        print("Sorry, either the flight doesn't exist")
        
def view_bookings(filter_by):
    if filter_by == 'flight_id':
        filtered_bookings = sorted(booking_database.values(), key=lambda x: x[0]['flight_id'])
    elif filter_by == 'flight_name':
        filtered_bookings = sorted(booking_database.values(), key=lambda x: x[0]['flight_name'])
    elif filter_by == 'date':
        filtered_bookings = sorted(booking_database.values(), key=lambda x: x[0]['date'])
    else:
        print("Invalid filter type.")
        return

    if filtered_bookings:
        print("Filtered Bookings:")
        for bookings in filtered_bookings:
            for booking in bookings:
                print(f"Flight ID: {booking['flight_id']}, Flight Name: {booking['flight_name']}, Date: {booking['date']}")
    else:
        print("No bookings found for the specified filter.")
        
#Adding new flight
def add_flight():
        new_flight_id=input("Enter the ID of the new flight:")
        new_flight_name=input("Enter the name of the new flight:")
        new_flight_available_seats=input("Enter the seats available on the new flight:")
        if new_flight_id in flights_database:
            print("Flight ID already exists. Please use a different ID.")
            return
        new_flight = {'flight_id': new_flight_id,'flight_name': new_flight_name,'seats_available': new_flight_available_seats}
                #flights_database[new_flight_id]=new_flight        
        print("Flight added successfully!")

        
while True:
    
    print("Wecome to Flight Ticketing Booking")
    print("1.Login\n2.Signup\n3.Exit")

    choice=int(input("Enter Your Choice:"))

    if(choice==1):# Login
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")

        user_role = login(username_input, password_input)
        if user_role == 'admin':
            print("Welcome, Admin!")
        elif user_role == 'user':
            print("Welcome, User!")
        else:
            print("Invalid username or password.")
    elif(choice==2):#Signup
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        role=input("Enter your role(user/admin)")
        signup(new_username, new_password,role)
        continue
    elif(choice==3):#Exit
        break
    else:#Invalid Option
        print("Invalid Choice")
# Searching Flights
    if user_role=="user":
        search_query = input("Search for flights by name, date, or flight ID: ")
        found_flights = search_flights(search_query)
        if found_flights:
            print("Matching Flights:")
            for flight in found_flights:
                print(f"Flight ID: {flight['flight_id']}, Name: {flight['name']}, Date: {flight['date']}, Seats Available: {flight['seats_available']}")
        else:
            print("No matching flights found.")
            
    elif user_role=="admin" :
                   admin_choice=int(input("Enter the choice\n1.Add Flights\n2.View Bookings:"))
                   if admin_choice == 1:
                       add_flight()
                   elif admin_choice == 2:
                       filter_criteria = input("Select any one filter criteria to view bookings\nflight_id or flight_name or date:")
                       view_bookings(filter_criteria)
                   
# Ticket booking
    if user_role == 'user':
        selected_flight_id = input("Enter the Flight ID to book a ticket: ")
        book_ticket(username_input, selected_flight_id)
      