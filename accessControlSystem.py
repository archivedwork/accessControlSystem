### Task 1 ##
## - choose one of three problems
## - code the selected problem and make three version as below:
## - version 1 : use structured code base (try to apply some design pattern style)
## - version 2 : make half structured and half unstructured code
## - version 3 : make unstructured code base (code that is hard to read and follow)

# version 1
import driver
import data

a = []
a.append(driver.createAP(data.ACCESS_POINT_1))


if a[0] == data.ACCESS_POINT_1:
    print "DONE"

a.append(driver.createAP(data.ACCESS_POINT_1))
if a[1] == data.ACCESS_POINT_1:
    print "FAIL"

print(a)
