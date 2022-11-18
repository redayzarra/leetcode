#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
  
#My Solution - Check to see if t and s are the same number of letters. Go through the letters of s and remove them if they exist in t, if t is zero then the same number of letters exist in both t and s.
      if len(s) == len(t): #Checks to see if the length of the two words are the same

        for letter in s: #Iterate through every letter in s
          if letter in t: #Check if it exists in t
            t = t.replace(letter, "", 1) #If it does, then remove the letter and assign it back to t
        return len(t) == 0 #Check to see if all the letters have been used, return True if all letters are used. If not, then unique letters exist so return False

      return False #If the length of s and t is not the same then they aren't anagrams to begin with


#Solution #2 - Check to see if s and t are the same length, return False immediately if they aren't.
      if len(s) != len(t): #Checks to see if they aren't the same! Faster this way.
          return False #Returns False if they aren't, or continues if they are
        
      for letter in s: #
          if letter in t:
              t = t.replace(letter, "", 1)
      return len(t) == 0

#Solution #3 - Sort the strings and check if they are equal after they have been sorted in alphabetical order.
      return sorted(s) == sorted(t)