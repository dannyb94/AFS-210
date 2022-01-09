# Write the code to perform a binary search on a sorted list.  The function should accept a sorted list and the value to search for as inputs.
# The function should return either True or False depending if the provided value was found in the sorted list.

# Sample Input:
# [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] find 31
# [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] find 77
# ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]find "Delta"

def bnrySearch(list, search):
	listLen = len(list)
	for i in range(listLen): # instead of for loop use while loop
		if search == list[i]:
			return True
	return False

l1 = ["Jeans", 22, 86, 310, "Flour", 48, "Lotto", 163, 7271]
l2 = [47, 120, 246, 3, 400, 52, 25, 99, 153, 81]
l3 = ["Hay", "Forage Food", "Wipes", "Lettuce", "Parsley", "Water", "Vitamins"]

print(bnrySearch(l1, 310)) # True
print(bnrySearch(l2, 80)) # False
print(bnrySearch(l3, "Lettuce")) # True
