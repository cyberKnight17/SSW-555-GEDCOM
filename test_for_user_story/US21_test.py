import unittest
import Project03_SourceCode
from UserStory21 import userStory21

class UserStory21Test(unittest.TestCase):
    def test_userStory21(self):
        r1 = Project03_SourceCode.parse_file('Project03-TestFile.ged')
        r2 = Project03_SourceCode.parse_file('Project01_Zhonghua_Bao.ged')
        expect1 = ['I2']
        expect2 = ['@I4@','@I5@']
        self.assertEqual(expect1,userStory21(r1))
        self.assertEqual(expect2,userStory21(r2))

if __name__ == '__main__':
    unittest.main(verbosity=2) 