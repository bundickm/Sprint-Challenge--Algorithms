'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# The pythonic way to do it would be to simply call `word.count('th')`
def count_th(word):
  if len(word) < 2: # Less than 2 char means it can't be 'th', bounce
    return 0
  elif word[:2] == 'th': # Check the first two letters
    return 1 + count_th(word[1:]) # Increment the count 1, remove the first letter
  else:
    return count_th(word[1:]) # No match, just remove the first letter