class Node:
	def __init__(self, info):
		self.info = info
		self.left = None
		self.right = None
		self.level =None
		
class BinaryTree"
	def __init__(self):
		self.root =Non
	
	def create(self, val):
		if self.root =None:
			self.root = None(val)
		else:
			current = self.root
		
		while True:
			if val < current.info:
				if current.left:
					current = current.left
				else:
					current.info = val
					break
			elif val > current.info:
				if current.right:
					current = current.right
				else:
					current.info = val
					break
			else:
				break
				
					