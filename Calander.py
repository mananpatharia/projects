import calendar

def main():
    while True:
        print("\n=== Calendar App ===")
        print("1. View Calendar")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_calendar()
        elif choice == "2":
            print("Exiting the Calendar App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def view_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    
    print("\nCalendar for {}-{}".format(year, month))
    
    cal = calendar.month(year, month)
    print(cal)

if __name__ == "__main__":
    main()
