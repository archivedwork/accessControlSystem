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
grant       = []

def createAP(access_identifier):

    if access_identifier not in accessPoint:
        accessPoint.append(access_identifier)
        x = "DONE"
        print(x)
    else:
        print("FAIL")
        return accessPoint


def createUser(user_identifier):

    if user_identifier not in user:
        user.append(user_identifier)
        x = "DONE"
        print(x)
    else:
        print("FAIL")
        return accessPoint


# Test cases for create access point
createAP(1)
# createAP(2)
# createAP(1)
# createAP(3)
# createAP(2)
# createAP(2)
# createAP(100)

# Test Cases for user 
createUser(1)
# createUser(1)
# createUser(2)

print("Access Point: ", accessPoint)
print("Users: ", user)