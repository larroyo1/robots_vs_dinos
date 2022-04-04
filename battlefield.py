from robot import Robot 
from dinosaur import Dinosaur 
from weapon import Weapon
import time

class Battlefield: 
    def __init__(self): 
        self.robot = Robot('Dominus')
        self.dinosaur = Dinosaur('Jimmy the Dino', 23)


    def display_welcome(self): 
        print('Welcome to Robots vs Dinos.')

    def battle_phase(self): 
        while self.robot.health > 0 and self.dinosaur.health > 0: 
            self.robot.attack(self.dinosaur)
            print(f'The robot attacked the dino! The dino now has {self.dinosaur.health} health.')
            time.sleep(1.5)
            
            if self.dinosaur.health <= 0:
                break
            else:
                self.dinosaur.attack(self.robot)
                print(f'The dino attacked the robot! The robot now has {self.robot.health} health.')
                time.sleep(1.5)

    def display_winner(self): 
        if self.robot.health > self.dinosaur.health: 
            print('The robot has won the battle!')
        else: 
            print('The dino has won the battle!')

    def select_robot_weapon(self): 
        user_input = int(input('Choose the robots weapon! Enter 1 for axe, 2 for sword, 3 for pillow, and 4 for BAZOOKA!'))

        if user_input == 1: 
            self.robot.active_weapon = Weapon('Axe', 15)
        elif user_input == 2: 
            self.robot.active_weapon = Weapon('Sword', 25)
        elif user_input == 3: 
            self.robot.active_weapon = Weapon('Pillow', 1)
        elif user_input == 4: 
            self.robot.active_weapon = Weapon('Bazooka', 100000) 

    def run_game(self): 
        self.display_welcome()
        self.select_robot_weapon()
        self.battle_phase()
        self.display_winner()