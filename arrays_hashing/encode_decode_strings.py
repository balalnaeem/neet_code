"""
Problem:
- we need to design an algorithm that would 
  - take in a list of strings
  - encode that into a string
  - and then decode that into a original list again
- strings would only contain the UTF-8 characters

There would be two methods:
encode
decode

encode takes in a list
decode takes in a string

The output from one method would probably be used as input for the other method

EXAMPLES:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

examples are probably not much helpful here but the point is, we need to have a encoding algorithm
that we can decode without any unexpected results

For example, if I join the list of strings together with '-'
"neet-code-love-you"
then i can split the string at '-' and get the list
['neet', 'code', 'love', 'you']

Problem with that is if we get input like the following:
["neet-code", "love", "you"]
we are screwed


we need to have a way that will not be beaten by the ungodly input we might receive

?? we can have the index of the string in the list somehow attached to the string
"0neet1code2love3you"
I can see how that would be problematic to decode. If the string has a numeric char in it or at the end of it.

?? We can decide an opening and a closing border for each string. That way we know where a string starts and where
it finishes.
But what if the border is included in the string?
- we can have number of characters in the border, so we would know after how many char the current string ends?

Something like
"4charsneet4charscode4charslove4charsyou"
or 
"4charneet4charcode1chari4charslove4charsyou"

then when we are reading the string,
we see how many chars, each string is and extract those chars

So encode would look something like this:
ENCODE
Loop over the list
on each iteration find out the length of the string
  create the code string and add to the result
  add the current string to the result
  go to next iteration

return result


And we will get the encoded string as input for the decode method
- and now that we know, how we have encoded that string
- we need to decode it
- we will read the string letter by letter
- once we start reading we start extracting the letters
- as soon as we have the letter #
- we stop and get the length of the str
- start a loop for that many letters, extract out the string
- append it to a list res
and then go to next iteration.



"""

def encode(strs):
    coded = ''
    for str in strs:
        coded += f'{len(str)}#'
        coded += str
    
    return coded

def decode(s):
    res = []
    i = 0
    
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
        
    return res




print(encode(["neet","code","love","you"]))
print(decode("4#neet4#code4#love3#you"))