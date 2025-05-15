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

    # Replace these comments with your function commenting
    def update_status(): # You may decide how to implement the arguments for this function
        print("Light =", self.traffic_light_color, "Pedestrian =", self.pedestrian, "Car =", self.car)

        print("Are any changes detected in the vision input?")
        while vision_input != "0":
            # get user input
            vision_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program:")
            if vision_input == "1":
                self.traffic_light_color = input("What change has been identified?: ")
        
        elif vision_input == "2":
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





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

