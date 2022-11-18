#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):

#My solution (wrong) - For every element in list nums, find the difference between target and the element and store that in a list. Check to see if the element exists in the stored list and then return their indices by assigning them to variables
      store = [] #Create an empty list called store
      for element in nums: #Iterate through every element of nums
        stored = target - element #Assign variable stored to the difference of target and element
        store.append(stored) #Add the variable stored to the empty list store

        if element in store: #Check to see if the element of nums exists in list store
          element_index = store.index(element) #If it does, assign the variable to find the index of where the element value is in the list store
          stored_index = len(store) - 1 #WRONG - assigns the last index of the list store to the variable


      output = [element_index, stored_index] #Stores the element index in store and the last index of store
      print(output) #Prints the output

#Solution #2 - Use the enumerate function to assign an index to an element while you're looping through it. This will allow you to cleanly achieve the index of the element and the element's value in the hashmap.
      hashmap = {} #Create an empty dictionary named hashmap
      
      for index, number in enumerate(nums): #Use enumerate to create a tuple that maps index to element value. Use unpacking to assign indices to index and element values to number
          difference = target - number #Assign the variable difference to the value of target - number
          if difference in hashmap: #Check to see if the difference is in hashmap
              return [hashmap[difference], index] #If it is, then return the indices of the difference index and the current index
          hashmap[number] = index #If not, then update the hashmap and add the element value in the correct index order to the hashmap
      return #Return