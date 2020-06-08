#Setup for unit tests
import unittest
import datamunger
import os


this_dir = os.path.dirname(__file__)

class MainUnitTest(unittest.TestCase):
    #TEST 1: Missing Value - single case
    def test1(self):
        testCSV = [",1,1,1,1,1,1,1,1"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertTrue(result, msg = "ERROR: Missing value - single case")

    #TEST 2: Incorrect Adding
    def test2(self):
        testCSV = ["1,1,1,1,1,1,1,1,1"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertNotEqual(warning_total, [], msg = "ERROR: Incorrect adding")

    #TEST 3: Correct Adding
    def test3(self):
        testCSV = ["36,1,2,3,4,5,6,7,8,X"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertEqual(warning_total, [], msg = "ERROR: Correct adding")

    #TEST 4: Correct monotonic: EQUAL values
    def test4(self):
        testCSV = ["36,1,2,3,4,5,6,7,8,X", "36,1,2,3,4,5,6,7,8,X", "360,10,20,30,40,50,60,70,80,X"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertEqual(warning_mono, [], msg = "ERROR: Correct equal monotonic")

    #TEST 5: Correct monotonic: different values
    def test5(self):
        testCSV = ["36,1,2,3,4,5,6,7,8,X", "360,10,20,30,40,50,60,70,80,X","3600,100,200,300,400,500,600,700,800,X"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertEqual(warning_mono, [], msg = "ERROR: Correct different monotonic")

    #TEST 6: Incorrect monotonic
    def test6(self):
        testCSV = ["36,1,2,3,4,5,6,7,8,X", "30,1,2,3,4,5,6,7,8,X", "360,10,20,30,40,50,60,70,80,X"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertNotEqual(warning_mono, [], msg = "ERROR: Incorrect monotonic")

    #TEST 7: Missing Value - multiple cases
    def test7(self):
        testCSV = [",1,1,1,1,1,1,1,1",",1,1,1,1,1,1,1,1","1,1,1,1,1,1,1,1,1",",1,1,1,1,1,1,1,1",",1,1,1,1,1,1,1,1",",1,1,1,1,1,1,1,1"]
        warning_total = []
        warning_mono = []
        result = datamunger.datamungerMain(testCSV, warning_total, warning_mono)
        self.assertEqual(result, 5, msg = "ERROR: Missing value - multiple cases")

if __name__ == '__main__':
    unittest.main()
