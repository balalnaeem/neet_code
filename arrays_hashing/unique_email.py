"""
Problem:
email
- local name (balal)
- @ symbol
- domain name (gmail.com)
- email may contain '.' or '+'

- '.' in local names don't matter. In domains, of course they do
- everything after the '+' in local name will be ignored (not domain of course)

Given the list of emails, return the number of tryly unique emails. Meaning how many different email
addresses will receive the email.

Ex:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2

we don't have to do anything to the domain name.
but we do need to perform some modification to the local name (before @) to see if the email is truly
unique

Approach:
- we need to ofcourse iterate over the array
- on each iteration we need to do some text manipulation based on the rules provided
- turn each email into truly unique and add it to a set.
- return len of the set

- text manipulation
  - separate the local name from the domain
  - remove the dots from local name
  - remove + and everything after it
  - add local name back with the domain with @

"""

def num_unique_emails(emails):
    res = set()
    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = local_name.replace('.', '').split('+')[0]
        res.add(local_name + 'a' + domain_name)
    return len(res)