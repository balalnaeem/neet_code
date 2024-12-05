=begin
PROBLEM:
- What is an Anagram?
  A word that is formed by re arranging the characters of another word
  So if I can spell 'cried' from the characters of the word 'cider'
  then 'cried' is an anagram of the word 'cider'

  Few more examples of anagrams:
  peach <==> cheap
  night <==> thing
  study <==> dusty

No letter should be reused.

We are given two strings. We have to find out if one string is an anagram of another.

AL:
- We will have to start with some sort of iteration over one string
  while trying to make the other given string. If not possible, return false.

- Or we can iterate over string_1 and inside this iteration we can start iterating over the the string_2
  and then we need to find out if each letter of string_1 exists in string_2 and the exists the same number of times
  So we can count the iteration of each letter in the string_1 and then count it in string_2 ??
  That can work too.

  This can actually be used using hashes as well.
  We can create a hash for each string with letters as keys and count of those letters as values
  We can then iterate over the hash_1 and check value of each key is same in both hashes.

  Or we can uniq the string_1
  iterate over the uniq string
  count the existence of each letter
  and make sure its the same number of times in both strings

PSEUDO CODE

method definition str_1 str_2
    string_1 uniq each do
      number of times each letter exists in str_1 == number of times each letter exists in str_2
      at any point above expression is false, return false
    end each

    return true
method definition end
=end

require 'pry'

def is_anagram(s, t)
  return false if s.size != t.size

  s.split('').uniq.each do |char|
    return false unless s.count(char) == t.count(char)
  end
    
  true
end

puts is_anagram("peach", "cheap")     #true
puts is_anagram("anagram", "nagaram") #true
puts is_anagram("fnagram", "nagaram") #false
puts is_anagram("cat", "rat")         #false