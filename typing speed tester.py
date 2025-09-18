import time

def typing_speed_meter():
    # The sentence to type
    sentence = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence as fast as you can:")
    print(sentence)
    
    # Start the timer
    start_time = time.time()
    
    # Get user input
    user_input = input("Your input: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate the time taken in minutes
    time_taken = (end_time - start_time) / 60  # convert to minutes
    
    # Calculate the number of words typed
    words_typed = len(user_input.split())
    
    # Calculate typing speed in WPM
    typing_speed = words_typed / time_taken if time_taken > 0 else 0
    
    print(f"Your typing speed is: {typing_speed:.2f} words per minute.")

# Run the typing speed meter
typing_speed_meter()
