=begin
PROBLEM:
- given a string containing only parentheses i.e. (){}[]
- determine if the input string is valid

conditions for validity:
1. open brackets must be closed and by the same bracket type
2. open brackets must be closed in the correct order
3. every close bracket has a corresponding open bracket.

open bracket should come before the closed bracket

AL:
So I learned a bit about stack
We will maintain a stack
Each time we encounter an opening bracket, we will add it to the top of the stack
Each time we encounter a closing bracket
  we will check if the top of the stack matches the the closing bracket, if it does we would remove the opening half
  from the stack, sort of like completing a bracket close
  If the top of the stack doesn't match the closing bracket, we return false
  If the stack is empty we return false

And if we get to the end of the string iteration and stack is empty we return true, which means each bracket was closed
in order

But if there is something still left in the stack we return false
We can use a hash to store opening and closing brackets, which will make it easier
for us to check the top of the stack for matching opening half of the bracket

=end

def is_valid(str)
  stack = []
  pairs = { ')' => '(', '}' => '{', ']' => '['}

  str.each_char do |char|
    if pairs.values.include?(char)
      stack << char
    else
      return false if stack.empty? || stack.pop != pairs[char]
    end
  end

  stack.empty?
end

