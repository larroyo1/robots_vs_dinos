import unittest 
from battlefield import Battlefield 
from dinosaur import Dinosaur
from robot import Robot 

class TestBattlefield(unittest.TestCase): 

    def test_instance(self): 
        battlefield = Battlefield()

        self.assertIsInstance(battlefield, Battlefield)
        self.assertIsInstance(battlefield.robot, Robot)
        self.assertIsInstance(battlefield.dinosaur, Dinosaur)

if __name__ == '__main__': 
    unittest.main()