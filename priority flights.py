from queue import PriorityQueue
import heapq

patients = PriorityQueue()
temp = 'Y'
name = "000"
pri = int(0)
while temp != 'N':
    print("Press 1 to enter the flight information\nPress 2 to dequeue flights information\npress 3 to display")
    print("Press N to terminate")
    temp = input("Enter your choice\t:")
    if temp == '1':
        name = input("Enter the name of the flight\t")
        pri = input("Enter the priority of flight(1 if it is emergency)\t")
        patients.put((pri, name))
    elif temp == '2':
        if patients.empty():
            print("Your queue is empty")
        else:
            print(patients.get())
    elif temp == '3':
        if patients.empty():
            print("Your queue is empty")
        else:
            print(patients.queue)
    else:
        print("Enter the valid choice")
