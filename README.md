# event-processing-system
A simple Python program to manage events using a queue system. Users can add, process, view, and cancel events through a menu-driven interface.


## Features
- Add events to the queue  
- Process the next event  
- Display pending events  
- Cancel an event

## What I Learned
While working on this project, I learned:
- How to implement a queue using Python lists  
- Handling user input with validation  
- Creating a menu-driven program  
- Basic queue operations like add, remove, and process




## Sample Output
```text
MENU
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 1
Enter event name: Meeting
Event 'Meeting' added to the queue.

MENU
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 3
Pending events:
1. Meeting

MENU
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 2
Processed event: 'Meeting
