# define functions to calcucate holiday cost

def hotel_cost(num_nights, cost_per_night=25):
    '''
    This function takes in number of nights spend in a hotel as an argument
    and returns a total cost for the hotel stay
    '''
    try:
        total = num_nights * cost_per_night
        return total
    except Exception as e:
        return f"The following error occured: {e}"


def plane_cost(city_flight):
    '''
    This function takes in the city destination as an argument for the user flight
    and returns the cost of the flight. Plane cost depends on the destination selected 
    by the user. There are four available destination with different price option:
    New York: £450 
    Roma: £80 
    Barcelona: £120 
    Melbourne: £780
    '''

    if city_flight == 'New York':
        return 450
    elif city_flight == 'Roma':
        return 80
    elif city_flight == 'Barcelona':
        return 120
    elif city_flight == 'Melbourne':
        return 780
    else:
        return "Invalid Destination. Try again!"



def car_rental(rental_days):
    '''
    This function takes in number of car rental days as an argument and 
    returns the total cost of the car rental. Daily rental cost is a flat rate of £29.99
    '''
    try:
        total = rental_days * 29.99
        return total
    except ValueError as e:
        return e


def holiday_cost(num_nights, city_flight, rental_days):
    '''
    This function takes in three arguments:
    num_nights, city_flight and rental_days and calculates
    the total amount of the holiday. To calculate the cost it uses three functions
    hotel_cost, plane_cost and car_rental
    Therefore, the following arguments need to be passed in:
    num_nights: number of nights spent in the hotel for the hotel_cost function
    city_flight: city to which the user is flying for the plane_cost function
    rental_days: number of car rental days for the car_rental function
    These three arguments are then passed in to calculate the total cost of the holiday
    '''
    try:
        hotel = hotel_cost(num_nights)
        plane = plane_cost(city_flight)
        car = car_rental(rental_days)
        total = hotel + plane + car
        return total
    except ValueError as e:
        return e


# run the program for the user to get the information for the holiday cost calculation
while True:
    try:
        destinations = ['New York', 'Roma', 'Barcelona', 'Melbourne']
        print('Choose from one of the following destinations: New York, Roma, Barcelona, Melbourne')
        city_flight = input("Please select your destination: ")
        # check for a correct city selected
        if city_flight not in destinations:
            print("Incorrect destination. Please try again!")
            continue

        num_nights = int(input('Please select number of nights: '))
        rental_days = int(
            input("Please select number of days to rent a car: "))

        # Calculating total cost of the holiday using user inputs
        total_cost = holiday_cost(num_nights, city_flight, rental_days)

        # print the result for the user
        print(
            f"Total cost of your holiday in {city_flight} for {num_nights} nights, renting a car for {rental_days} days is: £{total_cost}")
        break
    except Exception as e:
        print(f"Wrong Input. Let's try again! Error: {e}")
