from math import sqrt

while True:
    try:
        # Prompt the user to enter the car's skid distance in feet
        skid_distance = float(input("Enter the car's skid distance (in feet)\n"))
        
        # If the user has entered a negative number, prompt them to enter a valid input
        if skid_distance < 0:
            print("Invalid entry, please enter zero, or a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter zero, or a number greater than zero.")

# Calculate the car's speed
speed = sqrt(24 * skid_distance)

# Display the estimated speed in miles per hour, rounded to 2 decimals
print("Estimated speed: " + str(round(speed, 2)) + " mph.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")