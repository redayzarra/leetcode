#Enter the code below to return True if there is a duplicate in the list.
class Solution:
    def containsDuplicate(self, nums) -> bool:

#Solution #1 - Create a hashset then store values in it one at a time, while checking if it is already in there. A hashet is a type of data structure that doesn't contain duplicates.
        hash = set() #Create an empty hashset
        for number in nums: #Use a for loop to iterate through every element 
          if number in hash: #Checks if the number is already stored in set
            return True #If it is then return True and end the code
          hash.add(number) #If not then store that number to our hashet
        return False #If the for loop fails then return False

#Solution #2 - Check to see if the length of a hashset of the list is the same as the original. If it is, then all elements are unique. If not then there are duplicates.
    def containsDuplicate(self, nums) -> bool:

      return len(nums) != len(set(nums)) #If there are duplicates, then the list and set are not the same. Return True if there are duplicates. 