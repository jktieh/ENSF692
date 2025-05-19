# input_processing.py
# Jason Tieh, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light_color = "green"  # Default value
        self.pedestrian = "no"  # Default value
        self.car = "no"
        pass

    # Function to update the status of the sensor
    def update_status():
        print("Are any changes detected in the vision input?")
        # Get user input for menu option
        # 1 for light, 2 for pedestrian, 3 for vehicle
        menu_option = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program:")
        if menu_option == "1":
            # Get user input for light color
            self.traffic_light_color = input("What change has been identified?: ")
        elif menu_option == "2":
            # Get user input for pedestrian status
            self.pedestrian = input("What change has been identified?: ")
        elif menu_option == "3":
            # Get user input for vehicle status
            self.car = input("What change has been identified?: ")
        elif menu_option == "0":
            # End the program
            return
        else:
            # Invalid input

        

          # Show current status
        print("Light =", self.traffic_light_color, "Pedestrian =", self.pedestrian, "Car =", self.car)
        pass



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    #error message 1
    if sensor.traffic_light_color == "red" or sensor.pedestrian == "yes" or sensor.car == "yes":
        print("STOP")
    elif sensor.traffic_light_color == "yellow"
        print("Caution")
    elif sensor.traffic_light_color == "green"
        print("Proceed")
    else:
        print("Invalid vision input")
    pass




# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Create a sensor object
    sensor = Sensor()
    # Loop until the user chooses to end the program
    while True:
        # Call the update_status method to get user input
        sensor.update_status()
        # Check if the user wants to end the program
        if sensor.menu_option == "0":
            break
        else
            # Call the print_message function to display the action message
             print_message(sensor)






# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

