=begin
PROBLEM:
Check if a string is a palindrome and return true or false accordingly.

What is a palindrome?
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, 
it reads the same forward and backward. 

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

AL:
We are given a string in input.
1. We need to remove all non-alphanumeric characters from the string.
2. We need to lowercase the string.
3. We need to reverse the string and see if it's still the same

Pseudo Code:
To remove non all non-alphanumeric chars from the string, we can use regex
String has a 'sub' method that can substitute a letter with something else
We can substitute non-alphanumeric letters with ''
lower case the string and check if its the same when we reverse it

=end

def is_palindrome(s)
  slim_s = s.downcase.gsub(/[^a-zA-Z0-9]/, '')
  slim_s == slim_s.reverse
end


puts is_palindrome('A man, a plan, a canal: Panama')
puts is_palindrome('race a car')
puts is_palindrome('')


# Apparently `delete` method is better/faster here than `gsub` 