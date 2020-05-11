
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

# defining the hash map
class HashMap:
  
  # takes input for array size and puts None in the whole array
  def __init__(self, size):
  	self.array_size = size
  	self.array = [LinkedList() for i in range(size)]


  # defining a hash function which calculates a hash code value for the string
  def hash(self, key):
  	key_bytes = key.encode()
  	hash_code = sum(key_bytes)
  	return hash_code

  # compression function that reduces the number into array index
  def compress(self, hash_code):
  	return hash_code % self.array_size

  # Assigning the key value pairs for the array with index
  def assign(self, key, value):
  	array_index = self.compress(self.hash(key))
  	payload = Node([key, value])

  	# Assigning a list at the index temporarily to list_at_array
  	list_at_array = self.array[array_index]

  	#searching for the item, if found assigning value and returning else inserting
  	for item in list_at_array:
  		if item[0] == key:
  			item[1] = value
  			return

  	list_at_array.insert(payload)

  # Retrieving the value given the key
  def retrieve(self, key):
  	array_index = self.compress(self.hash(key))
  	list_at_index = self.array[array_index]
  	# Iterating over the list
  	for item in list_at_index:
  		if item[0] == key:
  			return item[1]
  
  		return None
  	payload = self.array[array_index]

  	if payload != None:
  		if payload[0] == key:
  			return payload[1]
  		elif payload[0] != key:
  			return None
  	elif payload == None:
  		return None

  
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
	blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))



