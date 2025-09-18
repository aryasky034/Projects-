import time

def countdown():
    """
    Simple countdown timer that takes user input for duration
    """
    try:
        # Get user input for countdown duration in seconds
        seconds = int(input("Enter countdown time in seconds: "))
        
        while seconds > 0:
            # Calculate minutes and seconds
            mins, secs = divmod(seconds, 60)
            # Format as 00:00
            timer = f"{mins:02d}:{secs:02d}"
            # Print over the same line
            print(timer, end="\r")
            # Wait one second
            time.sleep(1)
            seconds -= 1
        
        print("\nCountdown complete!")
    
    except ValueError:
        print("Please enter a valid number of seconds")

if __name__ == "__main__":
    countdown()
