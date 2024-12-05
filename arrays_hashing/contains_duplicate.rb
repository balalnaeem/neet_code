=begin
PROBLEM:
- We have an array of integers, and if there is any integers that appears more than once
  we return true (meaning the array does contain duplicates)

EXAMPLE:
  - [1, 2, 3, 4, 5, 5] ==> true
  - [9, 8, 7, 6, 5] ==> false
  - [1, 1] ==> true

EDGE CASES:
  if the array length is only 1 integer? its an automatic  false
    - [1] => false

AL:
- We have a given array
- we can initialize an empty array
- iterate over the given array and insert each int into the new empty array
- on each iteration check if the int already exists in the new array,
    if it does return true and stop iterating
- if we go over over all the ints in the given array without returning true,
      return false

PSEUDO CODE
define method
  initialize new array
  start iteration with each
    inside iteration 
      check if the current in already exists in the new array (return true if does)
      insert each int into the new array
    end iteration
  return false
end method definition
=end

def has_duplicate nums
  return false if nums.size <= 0
  new_nums = []
  
  nums.each do |int|
    return true if new_nums.include?(int)
    new_nums << int
  end

  false
end

puts has_duplicate [1, 2, 3, 3] # true
puts has_duplicate [1, 2, 3]    # false
puts has_duplicate [1]          # false
puts has_duplicate []           # false

