"""
We are given two integer arrays.
  - one arrays lists the  size of cookies each kid will be satisfied with
  - second array lists the cookies sizes that we have
we need to output, how many kids we can satisfy

EXAMPLES:
in: [1, 2, 3], s = [1, 1]
out: 1
we can only satisfy one kids with the cookie sizes that we have

in: [1, 2], s = [1, 2, 3]
out: 2
we can satisfy both kids with the cookie sizes that we have

BREAKDOWN:
- we are given two arrays of integers
- we need to find out how many integers in one array are 
  greater than or equal to the integers in the other array
- maximum possible greater than integers

A brute force solution would be easy but not very efficient.
- we could sort both arrays
- then use the pointer in one array
- and start iteration over the other array
- as soon as we are faced with the integer of same value or more,
  pointer moves forward before we go to the next iteration

We need to use two pointer approach:
- we would still need to sort two arrays
- we iterate over the sizes array
- on each iteration we check if it is greater than or equal to the greed that we are currently pointing to
- if it is, we start pointing to the next greed
- if it is not, we of course go to the next iteration
- that way we can go through all sizes
- while checking the greed ascending size
- and idx will be the number of satisfied kids
- we just need to make sure that we don't go out of reach index wise when checking greeds

"""

def find_content_children(g, s):
    g.sort()
    s.sort()
    idx = 0

    for size in s:
        if idx < len(g) and size >= g[idx]:
            idx += 1

    return idx

print(find_content_children([10,9,8,7], [5,6,7,8]))


