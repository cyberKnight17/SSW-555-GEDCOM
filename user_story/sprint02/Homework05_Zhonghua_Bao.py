from datetime import datetime
import unittest

def periodCompare(dt1,dt2,dt3,dt4):
    """Compare two time period dt1 to dt2, dt3 to dt4 whether they have any intersection, 
       include the condition where some date is not given
    """
    result = None

    # convert string date into the date object
    if dt1 is not None:
        dt1 = datetime.strptime(dt1,'%d%b%Y')
    if dt2 is not None:
        dt2 = datetime.strptime(dt2,'%d%b%Y')
    if dt3 is not None:
        dt3 = datetime.strptime(dt3,'%d%b%Y')
    if dt4 is not None:
        dt4 = datetime.strptime(dt4,'%d%b%Y')
    
    # two points comparison
    if dt2 is not None and dt3 is not None:
        if dt2 <= dt3:
            result = True
    
    # another case of two points comparison
    if dt1 is not None and dt4 is not None:
        if dt4 <= dt1:
            result = True
    
    # compare three points, when one time period is given
    if dt1 is not None and dt2 is not None:
        if dt3 is not None:
            if dt3 > dt1 and dt3 < dt2:
                return False
        if dt4 is not None:
            if dt4 > dt1 and dt4 < dt2:
                return False

    # compare three points, when another time period is given
    if dt3 is not None and dt4 is not None:
        if dt1 is not None:
            if dt1 > dt3 and dt1 < dt4:
                return False
        if dt2 is not None:
            if dt2 > dt3 and dt2 < dt4:
                return False

    return result

class Homework05Test(unittest.TestCase):
    def test_periodCompare(self):
        self.assertTrue(periodCompare('1JAN2019','3JAN2019','1FEB2019','3FEB2019'))
        self.assertTrue(periodCompare('1FEB2019','3FEB2019','1JAN2019','3JAN2019'))
        self.assertTrue(periodCompare('18MAY1984','11NOV2011','4MAY2013',None))
        self.assertTrue(periodCompare(None,'11NOV2011','4MAY2013',None))
        self.assertTrue(periodCompare('10OCT1976',None,None,'8AUG1966'))
        self.assertTrue(periodCompare('18MAY1984','11NOV2011','11NOV2011',None))
        self.assertTrue(periodCompare('28FEB2019','28FEB2019','28FEB2019','28FEB2019'))
        self.assertFalse(periodCompare('16FEB1952','30APR1999','3JUN1969','3JAN2019'))
        self.assertFalse(periodCompare('3JUN1969','3JAN2019','16FEB1952','30APR1999'))
        self.assertFalse(periodCompare(None,'15SEP2007','1AUG2007',None))
        self.assertFalse(periodCompare('8MAY1945','11NOV1990','25APR1968',None))
        self.assertFalse(periodCompare(None,'4APR2013','12DEC2009','20JAN2017'))
        self.assertIsNone(periodCompare(None,None,None,None))
        self.assertIsNone(periodCompare('18MAY1984','11NOV2011',None,'10OCT2016'))
        self.assertIsNone(periodCompare('18MAY1984',None,'4MAY2013','10OCT2016'))
        self.assertIsNone(periodCompare('18MAY2014','11NOV2017','4MAY2013',None))
        self.assertIsNone(periodCompare(None,None,'4MAY2013','10OCT2016'))
        
        

if __name__ == '__main__':
    unittest.main(verbosity=2) 