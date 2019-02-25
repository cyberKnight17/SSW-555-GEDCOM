from datetime import datetime
import unittest

def dateVerify(checkdate):
    """implement user story 01, dates (birth, marriage, divorce, death) should not be after the current date,
       verify the date checked validity, return none if date is invalid, and then compare with current date,
       if it is not later than current date, return true, else return false
    """
    if type(checkdate) is not str:
        return None

    try:
        date = datetime.strptime(checkdate,'%d%b%Y')
    except ValueError:
        print("The date you check is invalid, please try again.")
    else:
        current = datetime.today()
        delta = current - date # compare and get the gap bewteen the two dates
        if delta.days >= 0:
            return True
        else:
            return False
    
def dateCompare(checkdate,comparedate):
    if type(checkdate) is not str:
        return None

    try:   
        compare = datetime.strptime(comparedate,'%d%b%Y')
        check = datetime.strptime(checkdate,'%d%b%Y')
    except ValueError:
        print("The date you check is invalid, please try again.")
    else:
        delta = compare - check # compare and get the gap bewteen the two dates
        if delta.days >= 0:
            return False
        else:
            return True


class Homework04Test(unittest.TestCase):
    def test_dateVerify(self):
        self.assertIsNone(dateVerify(123))
        self.assertIsNone(dateVerify('123'))
        self.assertIsNone(dateVerify('48OCT2019'))
        self.assertIsNone(dateVerify('31FEB2019'))
        self.assertIsNone(dateVerify('10FEB2019.2'))
        self.assertTrue(dateVerify('01JAN2019'))
        self.assertTrue(dateVerify('24FEB2019'))
        self.assertFalse(dateVerify('1MAR2020'))
        self.assertIsNone(dateVerify('29FEB2100'))
    
    def test_dateCompare(self):
        self.assertTrue(dateCompare('25FEB2019','24FEB2019'))
        self.assertFalse(dateCompare('19FEB2019','24FEB2019'))
        self.assertFalse(dateCompare('24FEB2019','24FEB2019'))
        self.assertIsNone(dateCompare('29FEB2019','24FEB2019'))
        self.assertIsNone(dateCompare(123,'24FEB2019'))
        self.assertIsNone(dateCompare('123','24FEB2019'))
        

if __name__ == '__main__':
    unittest.main(verbosity=2)  
