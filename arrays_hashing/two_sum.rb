=begin
PROBLEM:
  - we are given an array of itegers, and a target integer
  - we have to find the indices of two integers in the array
    that add up to the target integer

Example:
nums = [2,7,11,15], target = 9
output = [0, 1]

There would be exactly one solution. Two numbers that exactly add up to the target.

AL:
- we can iterate over the array of ints
- on each iteration check compare the int with rest of the ints (another iteration)
- but only start iterating from that int and forward
- when the combo is found, return their indices

Pseudo Code:
method defition int_array target_array
int_array each_with_index current_int, index
  int_array each_with_index inside_current_int inside_index
    next if index == inside_index
    return index, inside_index if current_int + inside_current_int == target
  end inside iteration
end iteration
=end

def two_sum(nums, target)
  nums.each_with_index do |outer_int, outer_index|
    nums.each_with_index do |inner_int, inner_index|
      next if outer_index == inner_index
      return [outer_index, inner_index] if (outer_int + inner_int) == target
    end
  end
end

nums = [3,3]
target = 6

p two_sum(nums, target)

# This solution is brute force and takes a long time for bigger arrays
# need to improve upon this.

def two_sum_2(nums, target)
  nums_idx_hash = {}
  nums.each_with_index do |int, idx|
    diff = target - int
    return [nums_idx_hash[diff], idx] if nums_idx_hash.key?(diff)
    nums_idx_hash[int] = idx
  end
end

nums = [3,3]
target = 6

p two_sum_2(nums, target)