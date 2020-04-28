import unittest
import accessControlSystem

class test_system(unittest.TestCase):

    # def test_createAP(self):
    #     self.assertEqual(accessControlSystem.createAP(1), 'DONE')
    
    # #@unittest.expectedFailure
    # def test_createAP_fail(self):
    #     self.assertEqual(accessControlSystem.createAP(1), 'FAIL')

    # def test_createUser(self):
    #     self.assertEqual(accessControlSystem.createUser(1), 'DONE')

    # def test_createUser_fail(self):
    #     self.assertEqual(accessControlSystem.createUser(1), 'FAIL')
    

    # def test_grant(self):
    #     self.assertEqual(accessControlSystem.grant(1,1), 'DONE')

    # def test_grant_is_exit(self):
    #     self.assertEqual(accessControlSystem.grant(1,1), 'DONE')

    # def test_grant_fail(self):
    #     self.assertEqual(accessControlSystem.grant(2,2), 'Does not exit')

    # def test_check(self):
    #     self.assertEqual(accessControlSystem.check(1,1), 'Does not exit') # here should be yes but due to 1,1 is not exit is gives Does not exit

    # # def test_check_fail(self):
    # #     self.assertEqual(accessControlSystem.check(2,2), 'Does not exit')
    
    # def test_deleteAP(self):
    #     self.assertEqual(accessControlSystem.deleteAP(1), 'DONE')
    
    # def test_deleteAP_fail(self):
    #     self.assertEqual(accessControlSystem.deleteAP(1), 'FAIL')

# --------------------------------------------------------------------------------------------
# --------------------------------- Extended Version -----------------------------------------
# --------------------------------------------------------------------------------------------
    def test_newuser_pass(self):
        self.assertEqual(accessControlSystem.newUser("moo"),'Username moo are added to system')


    def test_newuser_fail(self):
        self.assertEqual(accessControlSystem.newUser("mo"), 'username exits!')


    def test_dooropener_pass(self):
        self.assertEqual(accessControlSystem.dooropener("mo"), '2020-06-23T10:00:00')


    def test_dooropener_fail(self):
        self.assertEqual(accessControlSystem.dooropener("mmo"), 'User is not found, not granted')
    
if __name__ == '__main__':
    unittest.main()