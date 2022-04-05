import unittest 
from robot import Robot 
from dinosaur import Dinosaur

class TestRobot(unittest.TestCase): 
    
    def test_instance(self): 
        robot = Robot('Dominus')

        self.assertIsInstance(robot, Robot)
        self.assertEqual(robot.name, 'Dominus')
        self.assertEqual(robot.health, 100)

    def test_attack(self): 
        robot = Robot('Dominus')
        dino = Dinosaur('Jimmy', 20) 

        self.assertEqual(dino.health, 100)
        robot.attack(dino)
        self.assertEqual(dino.health, 75)

        


if __name__ == '__main__': 
    unittest.main()