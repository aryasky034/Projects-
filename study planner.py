class StudyPlanner:
    def __init__(self):
        self.schedule = {}

    def add_subject(self, subject, time):
        self.schedule[subject] = time
        print(f"Added {subject} with study time of {time} hours.")

    def view_schedule(self):
        if not self.schedule:
            print("No subjects in the study planner.")
            return
        print("Your Study Schedule:")
        for subject, time in self.schedule.items():
            print(f"{subject}: {time} hours")

def main():
    planner = StudyPlanner()
    
    while True:
        print("\nStudy Planner Menu:")
        print("1. Add Subject")
        print("2. View Schedule")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            subject = input("Enter the subject name: ")
            time = input("Enter the study time in hours: ")
            planner.add_subject(subject, time)
        elif choice == '2':
            planner.view_schedule()
        elif choice == '3':
            print("Exiting the study planner. Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
