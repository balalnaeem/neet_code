"""
PROBLEM:
given an integer (row_index), return the row_index-th row of the pascals triangle.

EXAMPLES:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]

If we list the rows of pascal's triangle, we can see there is a pattern
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

- each new row is constructed from the previous array.
- apart from the first and last elements which are 1 anyway, each element's value is gained by adding last two elements
of the previous array
[1, 2, 1] ==> next ==> [1, 3, 3, 1]

We can build the triangle so and then return the row when get the required index

APPROACH:
- we build each row from the previous row
- And at the end of each row building we add a 1 to finish the row
- if index is 0 which means there is no previous row, we just add the 1 and return that row
- for each each row we start iterating on the previous array, add the first element as is
- for each next element, we add the previous two elements
- at the end add the closing 1 and return that row
- once we have built the required rows, we return latest row
"""

def get_row(rowIndex):
    triangle = []
    
    for i in range(rowIndex + 1):
        current_row = []
        if i > 0:
            previous_row = triangle[i - 1]
            for j in range(len(previous_row)):
                if j == 0:
                    current_row.append(previous_row[j])
                else:
                    current_row.append(previous_row[j] + previous_row[j - 1])
        current_row.append(1)
        triangle.append(current_row)
    return triangle[-1]

print(get_row(1))
            
