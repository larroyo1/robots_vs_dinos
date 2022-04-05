import unittest 
from weapon import Weapon

class TestWeapon(unittest.TestCase): 

    def test_instance(self): 
        weapon = Weapon('Axe', 10)
        
        self.assertIsInstance(weapon, Weapon)
        self.assertEqual(weapon.name, 'Axe')
        self.assertEqual(weapon.attack_power, 10)

if __name__ == '__main__': 
    unittest.main()
