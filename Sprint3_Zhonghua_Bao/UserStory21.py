import unittest
import Project03_SourceCode

def userStory21(result):
    indi,fam = result['indi'],result['fam']
    anamoly = list()

    for key in fam.keys():
        check_husb = fam[key]['HUSB']
        check_wife = fam[key]['WIFE']
        
        if indi[check_husb]['sex'] == 'F':
            if check_husb in anamoly:
                continue
            else:
                anamoly.append(check_husb)
                print("ERROR: INDIVIDUAL: US21:", check_husb, "should be a male.")
        
        if indi[check_wife]['sex'] == 'M':
            if check_wife in anamoly:
                continue
            else:
                anamoly.append(check_wife)
                print("ERROR: INDIVIDUAL: US21:", check_wife, "should be a female.")
    
    return anamoly

class UserStory21Test(unittest.TestCase):
    def test_userStory21(self):
        r = Project03_SourceCode.parse_file('Project03-TestFile.ged')
        expect = ['I2']
        self.assertEqual(expect,userStory21(r))



if __name__ == '__main__':
    unittest.main(verbosity=2) 