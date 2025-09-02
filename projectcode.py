event_queue = []

def add_event(event):
    event_queue.append(event)
    print("Event '" + event + "' added to the queue..!")

def process_next_event():
    if event_queue:
        event = event_queue.pop(0)
        print("\nProcessed event: '" + event + "'")
    else:
        print("\nNo events to process.")

def display_pending_events():
    if event_queue:
        print("\nPending events:")
        for idx, event in enumerate(event_queue, 1):
            print(str(idx) + ". " + event)
    else:
        print("\nNo pending events.")

def cancel_event(event_name):
    if event_name in event_queue:
        event_queue.remove(event_name)
        print("\nEvent '" + event_name + "' has been cancelled...!")
    else:
        print("\nEvent '" + event_name + "' not found or already processed...!")

def menu():
    while True:
        print("\nMENU")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            event = input("Enter event name: ")
            add_event(event)
        elif choice == 2:
            process_next_event()
        elif choice == 3:
            display_pending_events()
        elif choice == 4:
            event_name = input("Enter event name to cancel: ")
            cancel_event(event_name)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again...!")

menu()