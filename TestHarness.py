
#********************************************************************
from SocialSim import *

numPassed = 0
numTests = 0

ll = None 
sTestString = ""
nodeValue = None

#Test 1 - Constructor
print("\n\nTesting Normal Conditions - Constructor")
print("=======================================")
try:
    numTests += 1
    ll = DSALinkedList()
    print("Testing creation of DSALinkedList (isEmpty()):")
    if (not ll.isEmpty()):
        raise ListError("Head must be None.")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

     
#Test 2 - Insert First
print("\nTest insert first and remove first - stack behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertFirst():")
    ll.insertFirst("abc")
    ll.insertFirst("jkl")
    ll.insertFirst("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 3 - Peek First
try:
    numTests += 1
    print("Testing peek.First():")
    testString = ll.peekFirst()
    if testString != "xyz":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 4 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.removeFirst()
    if testString != "xyz":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "abc":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")


#Test 5 - Insert Last 
print("\nTest insert last and remove first - queue behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertLast():")
    ll.insertLast("abc")
    ll.insertLast("jkl")
    ll.insertLast("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 6 - Peek Last
try:
    numTests += 1
    print("Testing peekFirst():")
    testString = ll.peekFirst()
    if testString != "abc":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 7 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.removeFirst()
    if testString != "abc":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.removeFirst()
    if testString != "xyz":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 8 - Is Empty 2
try:
    numTests += 1
    print("Testing isEmpty when empty")
    testString = ll.removeFirst()
    raise ListError("Remove first when empty failed")
    print("Failed")
except:
    numPassed += 1
    print("Passed")

#Test 9 - Constructor
print("\n\nTesting Normal Conditions - Constructor")
print("=======================================")
try:
    numTests += 1
    nn = NodeFunc()
    print("Testing creation of nodeOperations (isEmpty()):")
    if (not ll.isEmpty()):
        raise ListError("Profiles must be None.")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 10 - AddAccounts 
print("\nTest create Profile")
print("=======================================")
try:
    numTests += 1
    print("Testing AddAccounts():")
    nn.AddAccounts("abc")
    nn.AddAccounts("jkl")
    nn.AddAccounts("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 11 - AddFirend
print("\nTest Add Friend")
print("=======================================")
try:
    numTests += 1
    print("Testing AddLinks():")
    nn.AddLinks("abc", "mns")
    nn.AddLinks("jkl", "abc")
    nn.AddLinks("xyz", "mns")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 12 - getProfilesCount
try:
    numTests += 1
    print("Testing getProfilesCount():")
    testString = nn.getProfilesCount()
    if testString != 4:
        raise ListError("Get ptofiles count failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 13 - getTotalConnections
try:
    numTests += 1
    print("Testing getTotalConnections():")
    testString = nn.getTotalConnections()
    if testString != 3:
        raise ListError("Get connections failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")
