import random   # to generate random temperature
import time     # to add 2 second delay

# take input of temperature limits from user
min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))

# Run continuously 
while True:
    
    # Generate random temperature between 0 and 100
    temperature = random.randint(0, 100)
    
    print("Current Temperature:", temperature)
    
    # Compare temperature with limits
    if temperature > max_limit:
        print("Alert: Temperature is too high\n")
        
    elif temperature < min_limit:
        print("Alert: Temperature is too low\n")
        
    else:
        print("Temperature is within acceptable limit\n")

    
    time.sleep(2)  # Wait for 2 seconds
