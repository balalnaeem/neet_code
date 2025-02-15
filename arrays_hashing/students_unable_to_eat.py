"""
PROBLEM:
- cafe has two types of sandwiches, that are placed in a stack like structure
- top sandwich has to be consumed first
- sandwiches are denoted by 0's and 1's
- students either prefer the 0 sandwich or 1 sandwich
- if the student does not want the sandwich at the top of the stack, they go to end of the queue
- we are given two integer arrays
  - student preferences
  - sandwich shapes in a stack
  - zero index is at the top of stack and -1 index is at the bottom of the stack

- students going to the end of the queue goes on until all the sandwiches are eaten
- or the students are not able to eat the sandwiches left
- because all the students that are left, do not prefer to eat the top sandwich

students and sandwiches have the same length
Only 0's or 1's in both arrays
no empty arrays

APPROACH:
- we need to have a pointer that would point to the next sandwich in the stack
- then we iterate over the students
  - if the student at 0 index is not okay with the sandwich,
    - he goes to end of the queue
    - and here we check whether the students that are left, do any of them want the sandwich
      on top. Because if not, we need to break out of the loop and return num of left students
    - and the next student becomes the student at 0 index and loop starts again
  - if the student at 0 index is happy with the sandwich
    - sandwich pointer gets updated
    - student get's dropped from the arr

- return the len of the students that are left

PSEUDO CODE:
DEF method(students, sandwiches):
SET next_sandwich_index = 0

LOOP over the students:
    IF student != next_sandwich
        check if the all the students prefer the next_sandwich:
        if next_sandwich not in students:
            return len(students)
        students.append(students.pop(0))
    else: (student happy with the sandwich)
        next_sandwich_pointer += 1
        students.pop(0)
    if len(students) == 0:
      return 0

return len(students)

"""

def count_students(students, sandwiches):
    cur_sandwich_idx = 0
    while True:
        if students[0] != sandwiches[cur_sandwich_idx]:
            if sandwiches[cur_sandwich_idx] not in students:
                return len(students)
            students.append(students.pop(0))
        else:
            students.pop(0)
            cur_sandwich_idx +=1
        if len(students) == 0:
            return 0


print(count_students([1,1,0,0], [0,1,0,1]))