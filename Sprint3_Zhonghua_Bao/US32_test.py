import unittest
import Project03_SourceCode
from UserStory32 import userStory32

class UserStory32Test(unittest.TestCase):
    def test_userStory32(self):
        r1 = Project03_SourceCode.parse_file('Project03-TestFile.ged')
        r2 = Project03_SourceCode.parse_file('Project01_Zhonghua_Bao.ged')
        expect1 = ['F2']
        expect2 = ['@F2@']
        self.assertEqual(expect1,userStory32(r1))
        self.assertEqual(expect2,userStory32(r2))


if __name__ == '__main__':
    unittest.main(verbosity=2) 