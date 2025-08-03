
# Output= [["hat"],["act", "cat"],["stop", "pots", "tops"]]


strs = ["act","pots","tops","cat","stop","hat"]
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        soln = defaultdict(list) # key : [takes list as value]
        for i in strs:  #think of looping then think of joining and soriting
            sorted_i = ''.join(sorted(i))
            #think of appending to the dic
            soln[sorted_i].append(i) 
            return list(soln.values)




'''from collections import defaultdict

# Input list of words
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# defaultdict automatically creates an empty list for a new key
res = defaultdict(list)

for s in strs:
    # Sort the word to get a common key for anagrams
    sortedS = ''.join(sorted(s))

    # Group the original word under the sorted key
    # If 'sortedS' doesn't exist in res, defaultdict makes an empty list
    res[sortedS].append(s)

# At this point, res looks like this:
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }

# Convert dictionary values to a list of groups
output = list(res.values())
print(output)

# ----------- Step-by-step Breakdown Below -----------

# Step 1: "eat" -> sorted = "aet"
# res = {
#   "aet": ["eat"]
# }

# Step 2: "tea" -> sorted = "aet"
# res = {
#   "aet": ["eat", "tea"]
# }

# Step 3: "tan" -> sorted = "ant"
# res = {
#   "aet": ["eat", "tea"],
#   "ant": ["tan"]
# }

# Step 4: "ate" -> sorted = "aet"
# res = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan"]
# }

# Step 5: "nat" -> sorted = "ant"
# res = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"]
# }

# Step 6: "bat" -> sorted = "abt"
# res = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }

# Final Output:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''