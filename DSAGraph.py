#
# -  Graph
#


from iterlinkedList import *
import numpy as np

class DSAGraph:
    '''
    This graph class implements adjacency list method
    '''
    def __init__(self):
        self.vertices = DSALinkedList()
        
    def addVertex(self,labels):
        for label in labels:
            sameLabelFound = False
            for vertices in self.vertices:
                if vertices._value.getLabel() == label:
                    sameLabelFound = True
            if not sameLabelFound:
                print("Creating New Graph Node:",label)
                vertex = DSAGraphVertex(label)
                node = DSAListNode(vertex)
                self.vertices.insertLast(node)
    
    def addEdge(self,label1,label2):
       
        self.addVertex((label1,label2))

        for vertices in self.vertices: 
                if vertices._value.getLabel() == label1:
                    vertices._value.addEdge(DSAGraphVertex(label2))
                if vertices._value.getLabel() == label2: # Bidirectional
                    vertices._value.addEdge(DSAGraphVertex(label1))
    
    def hasVertex(self,label):
        retval = False
        for vertices in self.vertices: 
                if vertices._value.getLabel() == label:
                    retval = True
        return retval
    
    def getVertexCount(self):
        retval = 0
        for vertices in self.vertices: 
                retval+=1
        return retval
    
    def getEdgeCount(self):
        retval = 0
        for vertices in self.vertices:
            retval += vertices._value.getAdjacentCount()
        return int(retval/2)
    
    def isAdjacent(self):
        pass
    
    def getAdjacent(self,label):
        retval = []
        for vertices in self.vertices: 
                if vertices._value.getLabel() == label:
                    for eachlinks in vertices._value.getAdjacent():
                        retVal.append(eachlinks)
        return retval
    
    def displayAsList(self):
        print()
        print("***********************************************************")
        print("Printing Graph As Adjacent List")
        print()
        for vertices in self.vertices:
            print(vertices._value)
        print("***********************************************************")
        
    def displayAsMatrix(self):
        pass
    
    def getAllVertices(self):
        setOfVertices = set()
        for vertices in self.vertices:
            setOfVertices = setOfVertices | {vertices._value}
        return setOfVertices
    
    def depthFirstSearch(self):
        
        newt = self.getAllVertices()
        S = DSASTACKLinked(self.getVertexCount()+1) # Stack of traversed Vertices
        T = set() # Traversal Edges
        V = newt.pop() # Current Vertex
        print("Starting from Node:",V.label)
        V.setVisited() # Mark Vertices as old
        S.push(V) # Push Vertices onto Stack
        while not S.isEmpty():
            for w in newt:
                for links in V.links:
                    if w.label == links.label and not w.getVisited():
                        newEdge = {(V,w)}
                        w.setVisited()
                        T = T | newEdge
                        S.push(w)
            V = S.pop()
        return T
    
    def breadthFirstSearch(self):
        newt = self.getAllVertices()
        Q = DSAQueueLinked(self.getVertexCount()+1) # Queue of Traversed Vertices
        T = set()
        V = newt.pop()
        print("Starting from Node:",V.label)
        V.setVisited()
        Q.queue(V)
        
        while not Q.isEmpty:
            V = Q.dequeue()
            for w in newt:
                for links in V.links:
                    if w.label == links.label and not w.getVisited():
                        newEdge = {(V,w)}
                        w.setVisited()
                        T = T | newEdge
                        Q.queue(w)
        return T



class DSAGraphVertex:
    
    def __init__(self,inLabel):
        self.label = inLabel
        self.new = True
        #self.value = inValue
        self.links = []
        self.visited = False
    
    def getLabel(self):
        return self.label
    
#     def getValue(self):
#         return self.value
    
    def getAdjacent(self):
        return self.links
    
    def getAdjacentCount(self):
        i = 0
        for link in self.links:
            i+=1
        return i
    
    def addEdge(self,vertex):
        linkExists = False
        for vertices in self.links:
            if vertex.label == vertices.label:
                linkExists = True
#                 print("Link Already Exists")
        if not linkExists:
            self.links.append(vertex)    
    
    def setVisited(self):
        self.visited = True
    
    def clearVisited(self):
        self.visited = False
        
    def getVisited(self):
        return self.visited
    
    def __str__(self):
        retstring = "Graph Node: " + str(self.label) + "\t" + "Adjacent Nodes "
        for adjacents in self.getAdjacent():
            if adjacents:
                retstring +=  str(adjacents.label) + " " 
        return retstring


#testVertex = DSAGraphVertex("A")
#print(testVertex)

#testVertex.addEdge(DSAGraphVertex("B"))
#testVertex.addEdge(DSAGraphVertex("C"))
#testVertex.addEdge(DSAGraphVertex("D"))
    
#print(testVertex.getAdjacentCount())


#print(testVertex)

#myGraph.addEdge("A","B")
#myGraph.displayAsList()
#print(myGraph.getEdgeCount())

# myGraph.addEdge("B","C")
# myGraph.displayAsList()
# print(myGraph.getEdgeCount())

# myGraph.addEdge("A","C")
# myGraph.displayAsList()
# print(myGraph.getEdgeCount())

# myGraph.addEdge("C","A")
# myGraph.displayAsList()
# print(myGraph.getEdgeCount())

# filename1 = "prac6_1.al"
# filename2  = "prac6_2.al"

# def graphFromfile(filename):
#     Edge_Vertex1 = []
#     Edge_Vertex1 = []

#     graphFromFile1  = DSAGraph()

#     def processline(line):
#         tokens = line.split(" ")
#         try:
#             inEdge_Vertex1 = tokens[0].strip()
#             inEdge_Vertex2 = tokens[1].strip()

#         except TypeError:
#             raise TypeError("File has invalid Format")
#         return inEdge_Vertex1,inEdge_Vertex2

#     try:
#         with open(filename,"r") as f:
#             for line in f.readlines():
#                 inEdge_Vertex1,inEdge_Vertex2 = processline(line)
#                 graphFromFile1.addEdge(inEdge_Vertex1,inEdge_Vertex2)
#             print("File Read Successful")
            
#     except IOError as e:
#         print("Error in File Processing:" + str(e))
#     return graphFromFile1

# graph1 = graphFromfile(filename1)
# graph1.displayAsList()
# graphFromfile(filename2).displayAsList()

# TraversalSet = graph1.depthFirstSearch()
# #print(TraversalSet)
# for paths in TraversalSet:
#    vertex1,vertex2 = paths
#    print("(",vertex1.label,",",vertex2.label,")",end=",")
# print()

# # for vertices in graph1.getAllVertices():
# #     print(vertices)

