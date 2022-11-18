# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums, k):

#My Solution (wrong)

      count = defaultdict(list)
      uniques = sorted(set(nums))
      answer = []

      for i, type in enumerate(nums):
        for number in nums:
          if number == type:
            (count[i]) += 1

      answer.append(count[:k])

#Solution #2 - Use bucket sort that is able to solve in linear time
"""
We are going to sort and count our values in a hashmap that stores the i (count)
and the values so if 1 occurs three times then value at count 3 would be a 1. We 
will also limit this list to 6 counts because the array given is only 6 elements.
We will then scan the list backwards K times to find the most frequent elements.
"""
def topKFrequent(self, nums, k):

      hashmap = {} #Create a hashmap to count occurences of each value
      frequency = [[] for i in range(len(nums) + 1)] #Index is going to be the frequency of an element

      for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)

      for n, c in hashmap.items():
        frequency[c].append(n)

      result = []
      for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
          result.append(n)
          if len(result) == k:
            return result

#Solution #3 - Use the counter function to count the elements
def topKFrequent(self, nums, k):
      from collections import counter
      count = counter(nums)
      return [c[0] for c in count.most_common(k)]

#Solution #4 - Use a max heap
def topKFrequent(self, nums, k):

      from collections import counter
      count = counter(nums)
      heap = []
      ans = []

      for i in count:
        heappush(heap, (-count[i], i))

      while k:
        ans.append(heappop(heap)[1])
        k -= 1

      return ans

#Solution #5 - The one liner
def topKFrequent(self, nums, k):
  from collections import counter
  return list(map(lambda x:x[0], counter(nums).most_common(k)))