# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs):

# Solution #1
      """
      We are using a default dictionary because there is an edge case where the 
      first element of count[0] does not exist, so we want our dictionary to just
      add it in there. This dictionary is storing the character count of anagrams.
      """
      hashmap = defaultdict(list) 
      
      """
      Assign count to an array with 26 zeroes, for storing the alphabet.
      """
      for word in strs: # Iterate through every string in the given list.
        count = [0] * 26 # Reset to all zeroes on every loop
        
        for letter in word: # Iterate through every letter in the word 
          """
          Use the ordinal value of letter minus the ordinal value of a. This 
          means that "a" will be assigned to index zero, b to one, etc. Then 
          increase where the letter is in list count, by one every time. 
          """
          count[ord(letter) - ord("a")] += 1 #Increment by one for every letter
        hashmap[tuple(count)].append(word)
          
      list: hashmap.values()

# Solution #2
      hashmap = defaultdict(list) #Create a Default Dictionary 

      for word in strs: #Iterate through every word in the given strings
        sorted_word = sorted(word) #Sort every word so ate is aet
        """
        Hashmap with the given key of sorted_word (which is made up of 1 and 0's)
        add the individual word in there. Do this for every loop.
        """
        hashmap[tuple(sorted_word)].append(word)

      return hashmap.values() # Return the values from the Default Dictionary