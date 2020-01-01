import random
import sys
from DSALink import *

class Post:

    def __init__(self):
        self.post = DSALinkedList()

    def _createPost(self, createdby):
        pass
        

class NodeFunc:
    
    def __init__(self):
        self.profiles = DSALinkedList()
        self.posts = DSALinkedList()
        
    def CheckAccExist(self,labels):
        "Creating Social Network's Profile"
        for labels in labels:
            sameLabelFound = False
            for profiles in self.profiles:
                if profiles._value.getAccount() == labels:
                    sameLabelFound = True
            if not sameLabelFound:
                print("CREATED ACCOUNT FOR:\t "+ str(labels) + "\n")
                profile = EdgeFunc(labels)
                node = DSAListNode(profile)
                self.profiles.insertLast(node)

    def AddAccounts(self,labels):
        "Creating Social Network's Profile"
        sameLabelFound = False
        for profiles in self.profiles:
            if profiles._value.getAccount() == labels:
                sameLabelFound = True
        if not sameLabelFound:
            print("CREATED ACCOUNT FOR:\t "+ str(labels) + "\n")
            profile = EdgeFunc(labels)
            node = DSAListNode(profile)
            self.profiles.insertLast(node)

    def AddLinks(self,name1,name2):

        self.CheckAccExist((name1,name2))

        for profiles in self.profiles: 
            if profiles._value.getAccount() == name1:
                profiles._value.AddLinks(EdgeFunc(name2))
            if profiles._value.getAccount() == name2: # Bidirectional
                profiles._value.AddLinks(EdgeFunc(name1))

    # def createPost(self,label,text):
    #     for profiles in self.profiles: 
    #         if profiles._value.getAccount() == label:
    #             profiles._value.createPost(Post(text))
    #         if profiles._value.getAccount() == name2: # Bidirectional
    #             profiles._value.createPost(Post(name1))    

    def getProfilesCount(self):
        value = 0
        for profiles in self.profiles: 
                value+=1
        return value


    def getTotalConnections(self):
        value = 0
        for profiles in self.profiles:
            value += profiles._value.getTotalLink()
        return int(value/2)
    
    
    def getLinks(self,label):
        value = []
        for profiles in self.profiles: 
                if profiles._value.getAccount() == label:
                    for eachlinks in profiles._value.getLinks():
                        value.append(eachlinks)
        return value

    
    
    def displayNetwork(self):
        print()
        print("***********************************************************")
        print("RUNNING TIMESTEPS BASE ON THE NETWORK FILE")
        print()
        for profiles in self.profiles:
            print(profiles._value)
        print("***********************************************************")
        
    def displayAsMatrix(self):
        pass
    
    def getAllProfiles(self):
        setOfProfiles = set()
        for profiles in self.profiles:
            setOfProfiles = setOfProfiles | {profiles._value}
        return setOfProfiles
    
    def DFS(self):
        
        newt = self.getAllProfiles()
        S = DSASTACKLinked(self.getVertexCount()+1) 
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
    

    def justpost(self, a, b):
        print(a + "\t >>POSTED\t"  + ">>" +b +"\n" )

    def remove(self,label):
        print("ACCOUNT" +"\t"+ label +"\t"+ "WAS REMOVED"+"\n" )
    
        

##############################  TRIED TO MAKE A FUNCTION THAT CAN CREATE POST AND LIKE IT ##### FAILED ##########################33
    # def addPost(self,labels):
    #     "Adding post"
    #     for label in labels:
    #         sameLabelFound = False
    #         for posts in self.posts:
    #             if posts._value.getAccount() == label:
    #                 sameLabelFound = True
    #         if not sameLabelFound:
    #             print("Creating New Graph Node:",label)
    #             post = EdgeFunc(label)
    #             node = DSAListNode(post)
    #             self.vertices.insertLast(node)

    # def like(self,name1,name2):
    #     "Like a post"
    #     self.addPost((name1,name2))

    #     for posts in self.posts: 
    #         if posts._value.getAccount() == name1:
    #             posts._value.like(EdgeFunc(name2))
    #         if posts._value.getAccount() == name2: # Bidirectional
    #             posts._value.like(EdgeFunc(name1))

    # def getPostCount(self):
    #     value = 0
    #     for posts in self.posts: 
    #             value+=1
    #     return value

    # def getLikes(self,label):
    #     value = []
    #     for posts in self.posts: 
    #             if posts._value.getAccount() == label:
    #                 for eachlinks in posts._value.getLikes():
    #                     value.append(eachlinks)
    #     return value
    
    # def getTotallikes(self):
    #     value = 0
    #     for posts in self.posts:
    #         value += posts._value.getLikesCount()
    #     return int(value/2)
   ############################################################################################################################ 


   


class EdgeFunc:
    
    def __init__(self,inLabel):
        self.label = inLabel
        self.connections = []
        self.visited = False
    
    def getAccount(self):
        return self.label
    
    
    def getLinks(self):
        return self.connections

    def getTotalLink(self):
        i = 0
        for link in self.connections:
            i+=1
        return i

    def AddLinks(self,profile):
        linkExists = False
        for profiles in self.connections:
            if profile.label == profiles.label:
                linkExists = True
        if not linkExists:
            self.connections.append(profile)        
    
    def setVisited(self):
        self.visited = True
    
    def clearVisited(self):
        self.visited = False
        
    def getVisited(self):
        return self.visited
    
    def __str__(self):
        retstring = "Profile: " + str(self.label) + "\t\t" + "Follows: "
        for adjacents in self.getLinks():
            if adjacents:
                retstring +=  str(adjacents.label) + " " 
        return retstring




class CreateNetwork:

    def graphFromfile(filename):
        CallFunc= NodeFunc()
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    tokens = line.split(":")
                    if len(tokens) == 1:
                        CallFunc.AddAccounts(tokens[0].strip())
                    elif len(tokens) == 2:
                        CallFunc.AddLinks(tokens[0].strip(),tokens[1].strip())
                print("File Read Successful")
        except IOError as e:
          print("Error in File Processing:" + str(e))
        return CallFunc




class Events:

    def graphFromfile(filename):
        CallFunc= NodeFunc()
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    tokens = line.split(":")
                    if tokens[0] == "F":
                        CallFunc.AddLinks(tokens[1].strip(),tokens[2].strip() )
                        print(tokens[1] +"\t" +">> STARTED FOLLOWING>>"+"\t" +tokens[2]+"\n")
                    elif tokens[0] == "P":
                        CallFunc.justpost(tokens[1].strip(),tokens[2].strip())
                    elif tokens[0] == "A":
                        CallFunc.AddAccounts(tokens[2].strip())
                    elif tokens[0] == "R":
                        CallFunc.remove(tokens[1].strip())
                print("File Read Successful")
        except IOError as e:
          print("Error in File Processing:" + str(e))
        return CallFunc


choose = input('\nSet run mode: (D)efault, (-I)nteractive, (-S)imulation or (E)xit\n')

if choose.upper() == '-S':
    if (len(sys.argv) < 3):
        print("\nArgvs too short, four arguments are requiered. Using default values: \n-Networkfile: 'network1.txt'\n-Eventfile: 'events1.txt'\n-Probability of like: 0.5\n-Probability of follow: 0.2\n")                     
        NetworkData = 'network1.txt'                
        eventsData = 'events1.txt'
        # iprob_like = 0.5
        # iprob_fol = 0.2
    else:        
        NetworkData =  open(sys.argv[2], 'r')              
        eventsData = open(sys.argv[3], 'r')          
        # iprob_like = float(sys.argv[4])             
        # iprob_fol = float(sys.argv[5])

    call = CreateNetwork.graphFromfile(NetworkData)
    call.displayNetwork()

elif choose.upper() == 'D':
    NetworkData = 'network1.txt'                
    eventsData = 'events1.txt'
    # iprob_like = 0.5
    # iprob_fol = 0.2
    call = CreateNetwork.graphFromfile(NetworkData)  
    call.displayNetwork()

elif choose.upper() == '-I':
    choose = int(input("PLEASE CHOOSE A OPTION: \n(1) LOAD NETWORK \n(2) SET PROBABILITY \n(3) NODE OPERATIONS  (INSERT, REMOVE, FIND) \n(4) EDGE OPERATION (LIKE/FOLLOW - ADD, REMOVE) \n(5) NEW POST \n(6) DISPLAY THE NETWORK \n(7) DISPLAY STATS \n(8) UPDATE- RUN A TIMESTEP\n(9) SAVE NETWORK \n(0)EXIT\n"))
    
    while choose != 0:
        if choose == 1:
            NetworkData = input('Upload a valid network file: ')
            eventsData = input('Upload a valid events file: ')

            network1 = CreateNetwork.graphFromfile(NetworkData)
            network1.displayNetwork()
            print("################################################################################"+"\n")
            print("RUNNNG >>>> TIMESTEPS BASED ON EVENTS <<<<<<<<<\n")
            print("################################################################################"+"\n")
            events1 = Events.graphFromfile(eventsData)
        elif choose == 2:
            iprob_like = input('Input probability of like: ')            
            iprob_fol = input('Input probability of follow: ')   
        elif choose == 3:
            print("<><><><><><><><><>TO USE THIS FUNCTION MAKE SURE TO LOAD A NETWORK FIRST<><><><><><><><><><><><>")
            choose1 = int(input("Enter selection: \n(1) Insert \n(2) Delete \n(3) Find\n"))
            if choose1 == 1:
                name = input('Name of Profile: ')
                #network1 = NodeFunc()
                network1.AddAccounts(name)
            elif choose1 == 2:
                name = input('\nChoose a name to remove :')
                print(name+"\twas removed")
            elif choose1 == 3:
                name = input('\nChoose a name to see its friends :')
                for profiles in network1.getLinks(name):
                    print(profiles)
        elif choose == 4:
            choose2 = int(input("Enter selection: \n(1) Follow \n(2) Like\n"))
            if choose2 == 1:
                sel1 = input('Enter a Connection from: ')
                sel2 = input('Enter a Connection to: ')
                network1.AddLinks(sel1, sel2)
                print("LINK CREATED BETWEEN\t"+sel1+"\tAND\t"+sel2+"\n")
            elif choose2 == 2:
                sel1 = input('Enter a profile for liking : ')
                sel2 = input('Enter a Connection to: ')
                print("PROFILE\t"+sel1+"\tLIKE\t"+sel2+"\n")            
        elif choose == 5:
            pass
        elif choose == 6:
            print('\nNetwork\n')
            network1.displayNetwork()
            print('\nEvents\n')
            events1.displayNetwork()
        elif choose == 7:
            pass
        elif choose == 8:
            eventsData = input('Upload a valid events file: ')
            events1 = Events.graphFromfile(eventsData)
        elif choose == 9:
            # network1= NodeFunc()
            # network1 = "network1.txt".displayNetwork()
            # network1= NodeFunc()
            with open('SAVED_NETWORK.txt', 'w') as f:
                f.writelines("NEW LIST AFTER UPDATION" +"\n")
                f.writelines(str(network1.getAllProfiles()))
                f.writelines(str(network1.displayNetwork()))
                print("\nNETWORK FILE SAVED TO THE FOLDER\n")
            
        else:
            print('!!!INVALID CHOICE!!!!.')
        print("\n")
        print("*******************************************************************************************************")
        
        choose = int(input("PLEASE CHOOSE A OPTION: \n(1) LOAD NETWORK \n(2) SET PROBABILITY \n(3) NODE OPERATIONS (INSERT, REMOVE, FIND) \n(4) EDGE OPERATION (LIKE/FOLLOW - ADD, REMOVE) \n(5) NEW POST \n(6) DISPLAY THE NETWORK \n(7) DISPLAY STATS \n(8) UPDATE- RUN A TIMESTEP\n(9) SAVE NETWORK \n(0)EXIT\n"))
        print("\n########################################################################################################")
elif choose.upper() == 0:
    print('Thanks')

else:
    print('THANK YOU!!!.')


