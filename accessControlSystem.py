from datetimerange import DateTimeRange
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
        
        # return('DONE')
        print ('DONE')    #bug injected
    else:
        #print("FAIL")
        return 'FAIL'

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
        #user.pop()     
        user.pull()     #bug inject
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
        return 'FAIL'


def check(accessIdentifier, userIdentifier):
    if grant(accessIdentifier, userIdentifier) == "DONE":
        return "YES"
    if grant(accessIdentifier, userIdentifier) == "FAIL":
        return "NO"
    
    if grant(accessIdentifier, userIdentifier) == "Does not exit":
        return "Does not exit"


def revoke(accessIdentifier, userIdentifier):
    if userIdentifier in user and accessIdentifier in accessPoint:
        user.pop()
        accessPoint.pop()
        return "DONE"
    else:
        return "FAIL"


output = [createAP(-3), createAP(1), createUser(1), createUser(1), grant(1,1), grant(1,1), grant(2,2), check(1,1), revoke(1,1), revoke(1,1), revoke(2,2), check(1,1), check(2,2), deleteAP(1), deleteAP(1), deleteUser(1), deleteUser(1)]
print(output)
print("Access Point: ", accessPoint)
print("Users: ", user)
# print("Grant: ", grnt)


# ----------------------- Extended Edition ---------------------
# The management of the Administration Building has decided to install an access control system to improve security conditions at the building.
# The access control system allows these  access privileges :
# add a new username to the list
# the door can be opened if the user is in the list if not the door will not open
# Time of Day: the system can allow the card to work at all day 24 hours per days for half year then the administartion must update manually and  periodically each half year
#

listOfUsers = ["mo"]

def newUser(new):
    if new not in listOfUsers:
        listOfUsers.append(new);
        return "Username " + new + " are added to system";
    else:
        return "username exits!";


def dooropener(username):
    if username not in listOfUsers:
        print("User is not found, not granted")
    else:
        print("USER GRANTED!, DOOR OPENED")
        userEntranceTime = "2020-06-23T10:00:00";
        return userEntranceTime

time_range = DateTimeRange("2020-01-01T00:00:00", "2020-06-30T00:00:00")

print("---------------------------- Extended version -------------------------")
print("2015-03-23T00:00:00" in time_range)
print(dooropener("m"))
print(newUser("md"))
print(dooropener("md"))
print(listOfUsers)

print(dooropener("mo") in time_range)
print(time_range)