"""
PROBLEM:
- we are given an array of how many tickets each person wants to buy
- its like index is a person and the value is the amount of tickets they want to buy
- each ticket takes 1 second to buy
- can only buy 1 ticket at a time
- and after buying have to go to the end of queue
- we are also given a position k for the queue
- we need to find out how many seconds it would take the person at k position 
  to buy the N(value of that position) tickets

Input: tickets = [2,3,2], k = 2
Output: 6

we are checking for person at index 2
it would take them 6 seconds to buy 2 tickets
[2,3,2] = 1 sec
[3,2,1] = 1 sec
[2,1,2] = 1 sec
[1,2,1] = 1 sec
[2,1]   = 1 sec
[1,1]   = 1 sec

Input: tickets = [5,1,1,1], k = 0
Output: 8

[5,1,1,1] = 1 sec
[1,1,1,4] = 3 sec
[4]       = 4 sec



APPROACH:
- we will use deque from collection for this logic
- we will need to keep track of two things
  1. seconds elapsed
  2. a revolving index (to keep track of our tickets at k position)
  
- convert the tickets list to deque
- start a loop
- we start revolving the deque and start counting the seconds
- on each revolve, we keep track of our revolving index
- as index goes to -1 we set it equal to len(list) - 1
- we don't count the seconds for values that have gone to 0, which means all the tickets been bought

PSEUDO CODE:

DEF time_required_to_buy(tickets, k):
SET seconds elapsed to 0
CONVERT the lis to deque

START THE LOOP:
if k < 0:
    SET k to len(tickets) - 1
if the first element at deque is > 0:
    -= 1 that element
    += the seconds elapsed
    if k at this iteratin is zero
        return seconds elapsed.
then pop the first from deque and append to the last
update the k -=1

"""
from collections import deque

def time_required_to_buy(tickets, k):
    seconds_elapsed = 0
    tickets = deque(tickets)
    last_index = len(tickets) - 1
    
    while True:
        if k < 0:
            k = last_index
        if tickets[0] > 0:
            tickets[0] -= 1
            seconds_elapsed += 1
            if k == 0 and tickets[0] == 0:
                return seconds_elapsed
        tickets.append(tickets.popleft())
        k -= 1

print(time_required_to_buy([5, 1, 1, 1], 0))