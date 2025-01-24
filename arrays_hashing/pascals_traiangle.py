"""
PROBLEM:
- we given an integer n
- return the first n rows of pascal's traiangle

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]

n will be between 1 and 30

Approach:
There is a pattern that we can observe from the examples:
Each next row(arr) is derived from the previous array
- on each iteration unless its the first element, we get the sum of the current element
and previous element
- when it comes to the last element, we add it on its own as well.

"""

def generate(num_rows):
  res = []
  for i in range(num_rows):
      new_row = []
      if i == 0:
          new_row.append(1)
      else:
          prev_row = res[i - 1]
          for j in range(len(prev_row)):
              if j == 0:
                  new_row.append(prev_row[j])
              else:
                  new_row.append(prev_row[j] + prev_row[j -1])
              if j == len(prev_row) - 1:
                  new_row.append(prev_row[-1])

      res.append(new_row)
  return res

print(generate(5))
             