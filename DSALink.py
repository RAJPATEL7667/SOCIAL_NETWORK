class DSAListNode():

	def __init__(self, invalue):
		self._value = invalue
		self._next = None
		self._prev = None

	def getValue(self):
		return self._value

	def setValue(self, invalue):
		self._value = invalue

	def getNext(self):
		return self._next

	def setNext(self, newNext):
		self._next = newNext

	def getPrevious(self):
		return self._prev

	def setPrevious(self, newPrevious):
		self._prev = newPrevious

class DSALinkedList():

	def __init__(self):
		self._head = None
		self._tail = None

	def __iter__(self):
		self._cur = self._head
		return self

	def __next__(self):
		curval = None
		if self._cur == None:
			raise StopIteration
		else:
			curval = self._cur._value
			self._cur = self._cur._next
		return curval

	def insertFirst(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self._head = newNd
			self._tail = newNd
		else:
			self._head.setPrevious(newNd)
			newNd._next = self._head
			self._head = newNd

	def insertLast(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self._head = newNd
			self._tail = newNd

		else:
			self._tail.setNext(newNd)
			newNd._prev = self._tail
			self._tail = newNd

	def isEmpty(self):
		empty = False
		if self._head == None:
			empty = True
		return empty

	def peekFirst(self):
		if self.isEmpty():
			raise Exception("Linklist is empty")
		else:
			nodeValue = self._head.getValue()
		return nodeValue

	def peekLast(self):	
		if self.isEmpty():
			raise Exception("Linklist is empty")
		else:
			nodeValue = self._tail.getValue()
		return nodeValue

	def removeFirst(self):
		if self.isEmpty():
			raise Exception("Linklist is empty")
		
		elif self._head == self._tail:
			nodeValue = self._head.getValue()
			self._head = None
			self._tail = None

		else:
			nodeValue = self._head.getValue()
			self._head = self._head.getNext()
			self._head.setPrevious(None)
			
		return nodeValue

	def removeLast(self):
		if isEmpty():
			raise Exception("Linklist is empty")
		elif self._head == self._tail:
			nodeValue = self._head.getValue()
			self._head = None
			self._tail = None
		else:
			nodeValue = self._tail.getValue()
			self._tail = self._tail.getPrevious()
			self._tail.setNext(None)

		return nodeValue

class DSASTACKLinked():
	"""docstring for DSASTACKLinked"""
	def __init__(self, n):
		self.array = DSALinkedList()
		self.max = n
		self.index = 0

	def push(self,item):
		if self.index<self.max:
			self.array.insertFirst(item)
			self.index += 1
		else:
			raise ValueError("Stack Full")

	def pop(self):
		retval = None
		if self.index >0:
			retval = self.array.peekFirst()
			self.array.removeFirst()
			self.index -=1
		else:
			raise ValueError("Stack Empty")
		return retval

	def __iter__(self):
		return self.array.__iter__()

	def __next__(self):
		return self.array.__next__()

	def __str__(self):
		retval = ""
		for items in self.array:
			retval+=" "+str(items)
		return retval
		
	def isEmpty(self):
		retval = False
		if self.index == 0:
			retval = True
		return retval

class DSAQueueLinked():
	"""Queue Implementation of linked List"""
	def __init__(self,n):
		self.array = DSALinkedList()
		self.max  = n
		self.index = 0
	
	def queue(self,item):
		if self.index < self.max:
			self.array.insertLast(item)
			self.index +=1
		else:
			raise ValueError("Queue Full")

	def dequeue(self):
		retval = None
		if self.index > 0:
			retval = self.array.peekLast()
			self.array.removeLast()
			self.index-=1
		else:
			raise ValueError("Queue Empty")
		return retval
	
	def __str__(self):
		retval = ""
		for items in self.array:
			retval+=" "+str(items)
		return retval
    
	def isEmpty(self):
		retval = False
		if self.index ==0:
			return retval
		return retval
 

