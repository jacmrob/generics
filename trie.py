# Author Jacqueline Roberti

class Trie:
	"""
	Trie data structure.
	Insert in O(key_len), search in O(key_len)
	Memory usage:  O(ALPHABET_SIZE * key_len * n)
	"""
	def __init__(self):
		self.trie = {}

	def insert(self, string):
		# inserts string into trie 
		trie_level = self.trie 
		m = len(string)
		for i, c in enumerate(string): 
			if c in trie_level.keys():
				if i == m:
					raise StandardError("Key is already in trie!")
				else:
					trie_level = trie_level[c]
			else:
				trie_level[c] = self._nest_remaining_chars(string, i+1, trie_level)
				break 

	def _nest_remaining_chars(self, string, i, d):
		d = {}
		current_level = d 
		for x, c in enumerate(string[i:]):
			current_level[c] = {}
			current_level = current_level[c]
		return d 


	def search(self, string):
		# returns true if the string is present, else false 
		trie_level = self.trie 
		for i, c in enumerate(string):
			if i == len(string) - 1:
				return True 
			if trie_level.get(c):
				trie_level = trie_level[c]
			else:
				return False 
