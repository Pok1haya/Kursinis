
#inventorius
#sudaryt ability  ir equipment list'as, jiems priskirt aprasyma ir atributus
#invetoriaus daiktam ir abilities priskirt kodus, kurie bus kazkam lygus, pvz #123 = sword

#cmd puslapis
#https://medium.com/@noransaber685/simple-guide-to-creating-a-command-line-interface-cli-in-python-c2de7b8f5e05

import cmd
import random

class SheetEditor:
    
    @staticmethod
    def import_sheet(importedSheetName):
        print(f"Importing: {importedSheetName}\n")
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
        print("Let's put in some data\n")
        name = input("Enter Name: ")
        class_name = input("Enter Class: ")

        while True:
            stats = input("Enter Statistics (STR DEX CON INT WIS CHA, separated by space): ").split()
            
            if len(stats) != 6:
                print("Error: Please enter exactly 6 statistics.")
            else:
                if all(stat.strip().isdigit() for stat in stats):
                    break
                else:
                    print("Error: Statistics should be numeric.")
    
        while True:
            health = input("Enter Health: ")
            if health.isdigit():
                break
            else:
                print("Error: Health should be a number.")
    
        with open(newSheetName, 'w') as file:
            file.write(name + "\n")
            file.write(class_name + "\n")
            file.write(' '.join(stats) + "\n")
            file.write(health + "\n")
            file.write(input("Enter Inventory content: ") + "\n")
            file.write(input("Enter Abilities: ") + "\n")
            file.write(input("Enter History: ") + "\n")
            print("Sheet created")


    def edit_sheet(sheetName):
        print(f"Editing {sheetName}")
        try:
            with open(sheetName, 'r') as file:
                data = file.readlines()
                print("Current data:")
                print("1. Name:", data[0].strip())
                print("2. Class:", data[1].strip())
                print("3. Statistics:", data[2].strip())
                print("4. Health:", data[3].strip())
                print("5. Inventory content:", data[4].strip())
                print("6. Abilities:", data[5].strip())
                print("7. History:", data[6].strip())
            
            while True:
                choice = input("Enter the number corresponding to what you want to edit or 'quit' to exit: ")
                if choice.lower() == 'quit':
                    print("Exiting editor.")
                    break
                
                line_num = int(choice)
                if line_num < 1 or line_num > 7:
                    print("Error: Invalid option number.")
                    continue
                
                if line_num == 1:
                    new_value = input("Enter new Name: ")
                elif line_num == 2:
                    new_value = input("Enter new Class: ")
                elif line_num == 3:
                    while True:
                        new_value = input("Enter new Statistics (STR DEX CON INT WIS CHA, separated by space): ")
                        stats = new_value.split()
                        
                        if len(stats) != 6:
                            print("Error: Please enter exactly 6 statistics.")
                        else:
                            if all(stat.strip().isdigit() for stat in stats):
                                new_value = ' '.join(stats)
                                break
                            else:
                                print("Error: Statistics should be numeric.")
                elif line_num == 4:
                    new_value = input("Enter new Health: ")
                    while not new_value.isdigit():
                        print("Error: Health should be a number.")
                        new_value = input("Enter new Health: ")
                elif line_num == 5:
                    new_value = input("Enter new Inventory content: ")
                elif line_num == 6:
                    new_value = input("Enter new Abilities: ")
                elif line_num == 7:
                    new_value = input("Enter new History: ")
                else:
                    print("Error: Invalid option number.")
                    continue
            
                data[line_num - 1] = new_value + "\n"
                
                with open(sheetName, 'w') as file:
                    file.writelines(data)
                
                print("Sheet updated successfully.")
            
        except FileNotFoundError:
            print("Sheet not found.")

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