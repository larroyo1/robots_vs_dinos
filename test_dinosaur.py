import unittest 
from dinosaur import Dinosaur 
from robot import Robot 

class TestWeapon(unittest.TestCase): 

    def test_instance(self): 
        dino = Dinosaur('Jimmy', 15)

        self.assertIsInstance(dino, Dinosaur)
        self.assertEqual(dino.name, 'Jimmy')
        self.assertEqual(dino.attack_power, 15)

    def test_attack(self): 
        dino = Dinosaur('Jimmy', 15)
        robot = Robot('Dominus')

        self.assertEqual(robot.health, 100)
        dino.attack(robot)
        self.assertEqual(robot.health, 85)

if __name__ == '__main__': 
    unittest.main()