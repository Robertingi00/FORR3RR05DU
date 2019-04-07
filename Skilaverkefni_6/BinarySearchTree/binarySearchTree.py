class Node:

	def __init__(this, tala):
		this.tala = tala;
		this.left = None;
		this.right = None;

	def insert(this, tala):
		if(tala < this.tala):
			if(this.left):
				return this.left.insert(tala)
			else:
				this.left = Node(tala)
				return this.left
		elif(tala > this.tala):
			if(this.right):
				return this.right.insert(tala)
			else:
				this.right = Node(tala)

	def preOrderPrint(this):
		print(this.tala)
		if(this.left):
			this.left.preOrderPrint()
		if(this.right):
			this.right.preOrderPrint()

	def postOrderPrint(this):
		if (this.left):
			this.left.postOrderPrint()
		if (this.right):
			this.right.postOrderPrint()
		print(this.tala)

	def lastNodeLeft(this, last=None):
		if(this.left):
			return this.left.lastNodeLeft(this)
		else:
			last.left = None
			return this.tala

	def lastNodeRight(this, last=None):
		if(this.right):
			return this.right.lastNodeRight(this)
		else:
			print(last.right)
			last.right = None
			return this.tala

	def delete(this, n, upp):
		if(n == this.tala):
			if(upp):
				this.tala = this.lastNodeLeft(this)
			else:
				this.tala = this.lastNodeRight(this)
		elif(n > this.tala):
			if(this.right):
				this.right.delete(n, upp)
			else:
				return -1
		elif(n < this.tala):
			if(this.left):
				this.left.delete(n, upp)
			else:
				return -1


class Tree:
	def __init__(this):
		this.head = None

	def insert(this, tala):
		if(this.head):
			this.head.insert(tala)
		else:
			this.head = Node(tala)

	def print(this):
		if(this.head):
			this.head.print()
		else:
			print("Ekkert í tré")

	def preOrderPrint(this):
		if(this.head):
			this.head.preOrderPrint();
		else:
			print("Ekkert í Tré")

	def postOrderPrint(this):
		if(this.head):
			this.head.preOrderPrint();
		else:
			print("Ekkert í Tré")

	def delete(this, n):
		if(this.head.tala == n):
			if(this.head.right and this.head.left):
				this.head.tala = this.head.right.lastNodeLeft()
			elif(this.head.right):
				this.head = this.head.right
			elif(this.head.left):
				this.head = this.head.left
			else:
				this.head = None
		else:
			if(n < this.head.tala):
				this.head.delete(n, False)
			elif(n > head.tala):
				this.head.delete(n, True)

	def deleteTree(this):
			this.head = None



tree = Tree()

tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.insert(9)
tree.insert(20)
tree.insert(15)

tree.postOrderPrint()
print("-------------")
tree.delete(10)
tree.postOrderPrint()
