import unittest
import Project03_SourceCode

def userStory32(result):
    indi,fam = result['indi'],result['fam']
    anamoly = list()

    for key in fam.keys():
        tmp = set()
        if 'CHIL' in fam[key]:
            for person in fam[key]['CHIL']:
                birth = indi[person]['BIRT']
                if birth in tmp:
                    print("ANAMOLY: FAMILY: US32:",fam[key]['fam'],"has multiple birth")
                    anamoly.append(fam[key]['fam'])
                    break
                else:
                    tmp.add(birth)
    
    return anamoly

class UserStory32Test(unittest.TestCase):
    def test_userStory32(self):
        r = Project03_SourceCode.parse_file('Project03-TestFile.ged')
        expect = ['F2']
        self.assertEqual(expect,userStory32(r))



if __name__ == '__main__':
    unittest.main(verbosity=2)