import random


class MyNode:

    def __init__(self, n):
        self.name = str(n)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.weight_up = 0
        self.weight_down = 0
        self.weight_left = 0
        self.weight_right = 0

    def print(self):
        print("----- " + self.name + " -----")
        print("Up: " + str(self.up) + " - " + str(self.weight_up))
        print("Down: " + str(self.down) + " - " + str(self.weight_down))
        print("Left: " + str(self.left) + " - " + str(self.weight_left))
        print("Right: " + str(self.right) + " - " + str(self.weight_right))

    def remove_edge(self):

        if (self.up == False and self.down == False
                and self.left == False and self.right == False):
            return -1

        while True:
            choice = random.randrange(1, 5)

            if choice == 1 and self.up != False:
                self.up = False
                self.weight_up = 0
                return 1
            elif choice == 2 and self.down != False:
                self.down = False
                self.weight_down = 0
                return 1
            elif choice == 3 and self.left != False:
                self.left = False
                self.weight_left = 0
                return 1
            elif choice == 4 and self.right != False:
                self.right = False
                self.weight_right = 0
                return 1

