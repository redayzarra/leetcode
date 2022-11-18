str = ["ate", "rat", "tea", "car", "tar", "art"]

# for word in str: #Iterate through every word listed in the list str
#   count = [0] * 26 #Creates and resets the value of count back to an array of 26 zeroes

#   for letter in word:
#     count[ord(letter) - ord("a")] += 1
print(str[3])

count = [0] * 26

for i in range(5):
  count[0] += 1

print(count)