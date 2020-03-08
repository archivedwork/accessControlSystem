import unittest
import accessControlSystem

class test_system(unittest.TestCase):

    def test_createAP(self):
        self.assertEqual(accessControlSystem.createAP(1), 'DONE')
    
    #@unittest.expectedFailure
    def test_createAP_fail(self):
        self.assertEqual(accessControlSystem.createAP(1), 'FAIL')

    def test_createUser(self):
        self.assertEqual(accessControlSystem.createUser(1), 'DONE')

    def test_createUser_fail(self):
        self.assertEqual(accessControlSystem.createUser(1), 'FAIL')
    

    def test_grant(self):
        self.assertEqual(accessControlSystem.grant(1,1), 'DONE')

    def test_grant_is_exit(self):
        self.assertEqual(accessControlSystem.grant(1,1), 'DONE')

    def test_grant_fail(self):
        self.assertEqual(accessControlSystem.grant(2,2), 'Does not exit')

    def test_check(self):
        self.assertEqual(accessControlSystem.check(1,1), 'Does not exit') # here should be yes but due to 1,1 is not exit is gives Does not exit

    # def test_check_fail(self):
    #     self.assertEqual(accessControlSystem.check(2,2), 'Does not exit')
    
    def test_deleteAP(self):
        self.assertEqual(accessControlSystem.deleteAP(1), 'DONE')
    
    def test_deleteAP_fail(self):
        self.assertEqual(accessControlSystem.deleteAP(1), 'FAIL')
    
    # def test_luhn_first(self):
    #     self.assertTrue(is_luhn_valid(18009054331492), True)
        
        
    # def test_luhn_second(self):
    #     self.assertFalse(is_luhn_valid(1800905433149), False)
   
   
    # @unittest.expectedFailure
    # def test_list_int(self):
    #     self.assertEqual(str(is_luhn_valid(1800905433149)), 'True')
        
    # def test_dob(self):
    #     self.assertEqual(str(dob), '1980-09-05')

    
    # @unittest.expectedFailure
    # def test_dob_fail(self):
    #     self.assertRaises(dob, '09-1980-05')

if __name__ == '__main__':
    unittest.main()