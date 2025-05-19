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

    # Constructor to initialize the sensor object
    def __init__(self):
        self.traffic_light_color = "green"  # Default value
        self.pedestrian = "no"  # Default value
        self.vehicle = "no"
        pass

    # Function to update the status of the sensor
    def update_status(self, menu_input, status_input):
       """
       Update the status of the sensor based on user selection
       of the menu item (0, 1, 2, 3) and status (green, yes, no, etc.)
       """
       if menu_input == '1' and (status_input in ["green", "yellow", "red)"]):
            self.traffic_light_color = status_input
       elif menu_input == '2' and (status_input in ["yes", "no"]):
            self.pedestrian = status_input
       elif menu_input == '3' and (status_input in ["yes", "no"]):
            self.vehicle = status_input
       else:
            print("Invalid vision change.")      
            
    # Function to print the message based on the sensor status
    def print_message(self):
        """
        Print the message based on the sensor status
        """
        # Check the status of the traffic light, pedestrian, and vehicle
        if self.traffic_light_color == "red" or self.pedestrian == "yes" or self.vehicle == "yes":
            print("\nSTOP\n")
        elif self.traffic_light_color == "yellow":
            print("\nCaution\n")
        elif self.traffic_light_color == "green":
            print("\nProceed\n")

        print("Light = " + self.traffic_light_color + ", Pedestrian = " + self.pedestrian + ", Vehicle = " + self.vehicle + "\n")

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Create a sensor object
    sensor = Sensor()
    # Loop until the user chooses to end the program
    while True:
        # use try-except to handle invalid input
        try:
            # Call the update_status method to get user input
            print("Are any changes detected in the vision input? ")
            # Get user input for menu option
            menu_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
            # validate that the user has inputted a proper value, if not, restart loop
            if menu_input in ['1', '2', '3']:
                status_input = input('What change has been identified?: ')
                Sensor.update_status(sensor, menu_input, status_input)
                Sensor.print_message(sensor)
            elif menu_input in ['0']:
                break
            else:         
                print(("You must select either 1, 2, 3, or 0.\n"))

        except ValueError:
            print(("You must select either 1, 2, 3, or 0.\n"))

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()


