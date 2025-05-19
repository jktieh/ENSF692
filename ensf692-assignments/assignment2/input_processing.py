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
        self.vehicle = "no"
        pass

    # Function to update the status of the sensor
    def update_status(self, menu_input, status_input):
       if menu_input == '1' and (status_input in ["green", "yellow", "red)"]):
            self.traffic_light_color = status_input
       elif menu_input == '2' and (status_input in ["yes", "no"]):
            self.pedestrian = status_input
       elif menu_input == '3' and (status_input in ["yes", "no"]):
            self.vehicle = status_input
       else:
            print("Invalid vision change.")      
            
# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
    def print_message(self):
        #error message 1
        if self.traffic_light_color == "red" or self.pedestrian == "yes" or self.vehicle == "yes":
            print("\nSTOP\n")
        elif self.traffic_light_color == "yellow":
            print("\nCaution\n")
        elif self.traffic_light_color == "green":
            print("\nProceed\n")

        print("Light = " + self.traffic_light_color + ', Pedestrian = ' + self.pedestrian + ', Vehicle = ' + self.vehicle)

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Create a sensor object
    sensor = Sensor()
    # Loop until the user chooses to end the program
    while True:
        # Call the update_status method to get user input
        print("Are any changes detected in the vision input?: ")
        # Get user input for menu option
        menu_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        # validate that the user has inputted a proper value, if not, restart loop
        if menu_input in ['1', '2', '3']:
            status_input = input('What change has been identified?: ')
            Sensor.update_status(sensor, menu_input, status_input)
        elif menu_input in ['0']:
            break
        else:         
            print(("You must select either 1, 2, 3, or 0.\n"))

        Sensor.print_message(sensor)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()


