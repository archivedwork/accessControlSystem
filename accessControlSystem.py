### Task 1 ##
## - choose one of three problems
## - code the selected problem and make three version as below:
## - version 1 : use structured code base (try to apply some design pattern style)
## - version 2 : make half structured and half unstructured code
## - version 3 : make unstructured code base (code that is hard to read and follow)

# Test Cases
## accessPoint          User           Grant             check
#     1                  1             DONE               Yes
#     1                  1             FAIL               NO
#     1                  2             DONE               Yes


accessPoint = []
user        = []
grnt       = []

def createAP(access_identifier):

    if access_identifier not in accessPoint:
        accessPoint.append(access_identifier)
        
        return "DONE"
    else:
        #print("FAIL")
        return "FAIL"

def deleteAP(access_identifier):

    if access_identifier in accessPoint:
        accessPoint.pop()
        return "DONE"
    else:
        #print("FAIL")
        return "FAIL"

    # if access_identifier not in accessPoint:
    #     return "Does not exit"


def createUser(user_identifier):

    if user_identifier not in user:
        user.append(user_identifier)
        return "DONE"
    else:
        return "FAIL"

def deleteUser(user_identifier):

    if user_identifier in user:
        user.pop()
        return "DONE"
    else:
        return "FAIL"

def grant(accessIdentifier, userIdentifier):
    if accessIdentifier in accessPoint:
        if userIdentifier in user:
            return "DONE"
        else:
            return "FAIL"
    else:
        return "Does not exit"


def check(accessIdentifier, userIdentifier):
    if grant(accessIdentifier, userIdentifier) == "DONE":
        return "YES"
    if grant(accessIdentifier, userIdentifier) == "FAIL":
        return "NO"
    
    if grant(accessIdentifier, userIdentifier) == "Does not exit":
        return "Does not exit"

def revoke(accessIdentifier, userIdentifier):
   if grant(accessIdentifier, userIdentifier) == "DONE":
       #grant(accessIdentifier, userIdentifier) == "FAIL"
       return "FAIL"
    
   if grant(accessIdentifier, userIdentifier) == "FAIL":
        return "Does not exit"

# Test cases for create access point
#createAP(1)
# createAP(2)
# createAP(1)
# createAP(3)
# createAP(2)
# createAP(2)
# createAP(100)

# Test Cases for user 
#createUser(1)
#createUser(3)
# createUser(2)


#check(1,1)
#grant(1,3)
#createUser(1)
#deleteUser(1)

output = [createAP(1), createAP(1), createUser(1), createUser(1), grant(1,1), grant(1,1), grant(2,2), check(1,1), check(2,2), revoke(1,1), revoke(2,2)]
print(output)
print("Access Point: ", accessPoint)
print("Users: ", user)
print("Grant: ", grnt)