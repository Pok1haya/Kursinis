#komandu list'as "/help" +
#importuot egzistuojanti sheeta + 
#sukurt nauja sheet'a
#sheeta editint
#pakeist health skaiciu
#inventorius
#ability list
#edit statistics
#dice roller +

#cmd puslapis
#https://medium.com/@noransaber685/simple-guide-to-creating-a-command-line-interface-cli-in-python-c2de7b8f5e05

import cmd
import random

class SheetEditor:
    
    @staticmethod
    def import_sheet(importedSheetName):
        print(f"Importing:, {importedSheetName}\n")
        try:
            with open(importedSheetName, 'r') as file:
                for line in file:
                    print(line.strip())
                
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)
    
    def create_sheet(newSheetName):
        print(f"Creating: {newSheetName}\n")
        with open(newSheetName, 'w') as file:
            print("Let's put in some data\n")
            file.write(input("Enter Name: \n") + "\n")
            file.write(input("Enter Class: \n") + "\n")
            file.write(input("Enter Statistics (STR, DEX, CON, INT, WIS, CHA): \n") + "\n")
            file.write(input("Enter Health: \n") + "\n")
            file.write(input("Enter Inventory content: \n") + "\n")
            file.write(input("Enter Abilities: \n") + "\n")
            file.write(input("Enter History: \n") + "\n")
            print("Sheet created")

    def edit_sheet(sheetName):
        print(f"Editing {sheetName}")
        
class DiceRoller:
    def __init__(self):
        self.dice_types = {
            'd4': 4,
            'd6': 6,
            'd8': 8,
            'd10': 10,
            'd12': 12,
            'd20': 20,
            'd100': 10
        }

    def roll_dice(self, dice_type):
        if dice_type.lower() in self.dice_types:
            max_value = self.dice_types[dice_type.lower()]
            if dice_type.lower() == 'd100':
                result = random.randint(0, 10) * 10 
            else:
                result = random.randint(1, max_value)
            print(f"Rolling {dice_type}: {result}\n")
        else:
            print("Invalid dice type. Choose from d4, d6, d8, d10, d12, d20, or d100.\n")
    
  
    
class CommandInterface(cmd.Cmd):
    prompt = '> '
    intro = 'Welcome to DND helper. Type "help" for available commands.'
    
    def __init__(self):
        super().__init__()
        self.sheetName = ''
        
    def do_SheetExplain(self, line):
        """Explains sheets text file lines"""
        print("1. Name\n2. Class\n3. Stats\n4. Health\n5. inventory\n6. Abilities\n7. History")
    
    def do_CreateSheet(self, line):
        """Creates a new sheet"""
        newSheetName = input("Enter file name: ")
        SheetEditor.create_sheet(newSheetName)
        self.sheetName = newSheetName
        
    def do_ImportSheet(self, line):
        """Imports an existing sheet"""
        importedSheetName = input("Enter file name: ")
        SheetEditor.import_sheet(importedSheetName)
        self.sheetName = importedSheetName
    
    def do_EditSheet(self, line):
        """Edit an imported/created sheet"""
        if self.sheetName == '':
            print("No imported/created sheet. Create a sheet with command 'CreateSheet' or import one using 'ImportSheet'")
        else:
            SheetEditor.edit_sheet(self.sheetName)


    def do_SheetName(self, line):
        """Displays sheet name"""
        if self.sheetName == '':
            print("No imported/created sheet. Create a sheet with command 'CreateSheet' or import one using 'ImportSheet'")
        else: print(self.sheetName)
    
    def do_RollDice(self, line):
        """Roll a dice of your choice"""
        roller = DiceRoller()
        while True:
            dice_input = input("Enter the type of dice to roll (e.g., d6, d20, d100), or 'exit' to exit: ")
            if dice_input.lower() == 'exit':
                break
            roller.roll_dice(dice_input)
    
    def do_Quit(self, line):
        """Exits DND helper"""
        return True
    
    def postcmd(self, stop, line):
        print()  
        return stop
    
if __name__ == '__main__':
    CommandInterface().cmdloop()