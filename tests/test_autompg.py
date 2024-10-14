import os
import unittest
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# Gives you access to all functions, methods, etc. of these classes
from src.autompg import AutoMPG, AutoMPGData

# Checks that import works & that it imports correct file/thing
# a1 = AutoMPGData()

# Way to print objects from AutoMPGData.
# for car in a1:
#     print(car)

print("This is test_autompg:", __name__)


class TestAutoMPG(unittest.TestCase):
    """
    This class inherits from unittest.TestCase and tests the autompg.py file

    Methods:
    -----------------------------------------------
    setUpClass: instantiates an object of the AutoMPGData class
    tearDownClass: deletes clean data file and object
    setUp: prints a string
    tearDown: prints a string
    test_str: Checks format of string from __str__ method
    test_eq: Checks __eq__ method works as intended
    test_lt: Checks __lt__ method works as intended
    test_hash: Checks has method works properly
    """

    @classmethod
    def setUpClass(cls):
        """
        instantiate an object of AutoMPGData class
        that will be used for testing the code. Executed
        before any of the tests are run.
        """
        print("Executing setUpClass")

        # My Notes:
        # Creates attribute called a1. Attribute is of TestAutoMPG
        # class, it is accessible to all methods within this class!
        # (ex: Can access self.data list from AutoMPGData init).
        # Creates an object/instance of AutoMPGData class that is
        # now a part of this TestAutoMPG class, but has its own
        # properties/functions defined in autompg.py.
        cls.a1 = AutoMPGData()
        return

    @classmethod
    def tearDownClass(cls):
        """Runs after all tests in the class are run"""
        os.remove('data/auto-mpg.clean.txt')
        del cls.a1
        print('Executing tearDownClass')
        return

    def setUp(self):
        """Runs before each test in the class and prints a string"""
        print("setUp")
        return

    def tearDown(self):
        """Runs after each test in the class and prints a string"""
        print("tearDown")
        return

    def test_str(self):
        """
        Tests str method in AutoMPGData corresponds to format
        AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)
        """
        # print(self.a1.data[238])
        print("Executing test_str")
        car238 = self.a1.data[238]  # AutoMPG(subaru, dl, 1977, 30.0)
        
        self.assertEqual(self.a1.data[0], AutoMPG(make="chevrolet",
                                                  model="chevelle malibu", year=1970, mpg=18.0))
        
        self.assertEqual(self.a1.data[1], AutoMPG(make="buick",
                                                  model="skylark 320", year=1970, mpg=15.0))
        
        self.assertEqual(car238, AutoMPG(make="subaru", model="dl", year=1977, mpg=30.0))
        return

    def test_eq(self):
        """
        Checks that the __eq__ method uses all 4 attributes to compare
        and is working as intended. Makes sure the objects pulled from
        AutoMPGData are of the AutoMPG class. Does not raise TypeError
        because __eq__ from default python class is called to assess
        equality of different object types.
        """
        print("Executing test_eq")
        # print(self.a1.data[0])

        # Objects from AutoMPGData
        car0 = self.a1.data[0]  # AutoMPG(chevrolet, chevelle malibu, 1970, 18.0)
        car1 = self.a1.data[1]  # AutoMPG(buick, skylark 320, 1970, 15.0)
        car6 = self.a1.data[6]  # AutoMPG(chevrolet, impala, 1970, 14.0)

        # Equal tests actually evaluate even though obj is different type. Equal
        # calls python default parent method and gives Assertion error
        # unlike lt method that gives type error.
        # This is why we don't need to assertRaise(TypeError) for __eq__.
        self.assertFalse(car0 == 3)

        # asserIsInstance tests whether obj is an instance of cls
        self.assertIsInstance(car0, AutoMPG)
        self.assertIsInstance(car1, AutoMPG)
        self.assertIsInstance(car6, AutoMPG)

        # An easier way to change one variable on second car object for each comparison
        # car0 = self.a1.data[0]
        # car_y = AutoMPG(make, model, year, mpg)
        # self.assertEqual(car0, other_vehicle)
        # self.assertNotEqual(car0, AutoMPG('a', car_y.model, car_y.year, car_y.mpg))

        # Both perfectly equal
        self.assertEqual(car0, AutoMPG(make="chevrolet", model="chevelle malibu", year=1970, mpg=18.0))

        # All attributes equal except make
        self.assertNotEqual(car6, AutoMPG(make="bmw", model="impala", year=1970, mpg=14.0))

        # All attributes equal except model
        self.assertNotEqual(car6, AutoMPG(make="chevrolet", model="chevelle", year=1970, mpg=14.0))

        # All attributes equal except year
        self.assertNotEqual(car1, AutoMPG(make="buick", model="skylark 320", year=1975, mpg=15.0))

        # All attributes equal except mpg
        self.assertNotEqual(car1, AutoMPG(make="buick", model="skylark 320", year=1970, mpg=500.0))
        return

    def test_lt(self):
        """
        Checks that the __lt__ method uses all 4 attributes to compare
        and is working as intended. Raises a TypeError if objects being
        compared are not both AutoMPG objects.
        """
        print("Executing test_lt")

        # Objects from AutoMPGData
        car9 = self.a1.data[9]  # AutoMPG(amc, ambassador dpl, 1970, 15.0)
        car30 = self.a1.data[30]  # AutoMPG(chevrolet, vega 2300, 1971, 28.0)

        # self.assertRaises(TypeError, car0.__lt__, 10)  # Another way
        with self.assertRaises(TypeError):
            car9 < 10

        with self.assertRaises(TypeError):
            car30 < "hello"

        # asserIsInstance tests whether obj is an instance of cls
        self.assertIsInstance(car9, AutoMPG)
        self.assertIsInstance(car30, AutoMPG)

        # Both perfectly equal
        self.assertEqual(car9, AutoMPG(make="amc", model="ambassador dpl", year=1970, mpg=15.0))
        self.assertFalse(car9 < AutoMPG(make="amc", model="ambassador dpl", year=1970, mpg=15.0))

        # Testing one less than if all others are equal
        # All attributes equal except make <
        self.assertTrue(car30 < AutoMPG(make="zhevrolet", model="vega 2300", year=1971, mpg=28.0))

        # All attributes equal except model <
        self.assertTrue(car30 < AutoMPG(make="chevrolet", model="zega 2300", year=1971, mpg=28.0))

        # All attributes equal except year <
        self.assertTrue(car30 < AutoMPG(make="chevrolet", model="vega 2300", year=1975, mpg=28.0))

        # All attributes equal except mpg <
        self.assertTrue(car30 < AutoMPG(make="chevrolet", model="vega 2300", year=1971, mpg=30.0))

        # Testing one greater than if all others are less than
        # All attributes less than except make >
        self.assertFalse(car30 < AutoMPG(make="ahevrolet", model="zega 2300", year=1975, mpg=30.0))

        # All attributes less than except model >
        self.assertFalse(car30 < AutoMPG(make="dhevrolet", model="uega 2300", year=1975, mpg=30.0))

        # All attributes less than except year >
        self.assertFalse(car30 < AutoMPG(make="dhevrolet", model="zega 2300", year=1900, mpg=30.0))

        # All attributes less than except mpg >
        self.assertFalse(car30 < AutoMPG(make="dhevrolet", model="zega 2300", year=1975, mpg=25.0))
        return

    def test_hash(self):
        """
        Checks that the hash method is working properly.
        """
        print("Executing test_hash")
        test = AutoMPG('bmw', 'x3', 2013, 7.8)
        test2 = AutoMPG('chevy', 'truck', 2010, 10.8)
        test3 = AutoMPG('chevy', 'truck', 2010, 10.8)
        test4 = AutoMPG('audi', 'a4', 2009, 9.8)
        test_hash = {test, test2, test3, test4}

        # if test_hash deals with duplicate, this is equal. If not, there are 4 objects.
        # makes sure obj is hashable
        self.assertEqual(len(test_hash), 3)

        # test if 2 of the same objects have the same hash
        self.assertEqual(hash(test2), hash(test3))
        return

        # # My Notes:
        # for car in self.a1:
        #     print(car)
        # print(self.a1.data[9])

    # # My Notes:
    # def test_test(self):
    #     # Test that this test runs with print
    #     print("Hello")
    #
    #     # Outputs the memory location bc AutoMPGData doesn't have a str method
    #     print(self.a1)
    #
    #     # Output are the actual AutoMPGData objects
    #     for car in self.a1:
    #         print(car)


if __name__ == '__main__':
    unittest.main()
