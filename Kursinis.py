
#inventorius
#sudaryt ability  ir equipment list'as, jiems priskirt aprasyma ir atributus
#invetoriaus daiktam ir abilities priskirt kodus, kurie bus kazkam lygus, pvz #123 = sword

#cmd puslapis
#https://medium.com/@noransaber685/simple-guide-to-creating-a-command-line-interface-cli-in-python-c2de7b8f5e05

import cmd
import random

class SheetEditor:
    @staticmethod
    def import_sheet(imported_sheet_name):
        """Imports a sheet from a file."""
        print(f"Importing: {imported_sheet_name}\n")
        try:
            with open(imported_sheet_name, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)

    @staticmethod
    def create_sheet(new_sheet_name):
        """Creates a new sheet."""
        print(f"Creating: {new_sheet_name}\n")
        print("Let's put in some data\n")
        name = input("Enter Name: ")
        class_name = input("Enter Class: ")
        stats = SheetEditor._input_stats()
        health = SheetEditor._input_health()
        inventory = input("Enter Inventory content: ")
        abilities = input("Enter Abilities: ")
        history = input("Enter History: ")

        with open(new_sheet_name, 'w') as file:
            file.write(f"{name}\n{class_name}\n{' '.join(stats)}\n{health}\n{inventory}\n{abilities}\n{history}\n")
        print("Sheet created")

    @staticmethod
    def _input_stats():
        """Inputs statistics for the character."""
        while True:
            stats = input("Enter Statistics (STR DEX CON INT WIS CHA, separated by space): ").split()
            if len(stats) != 6:
                print("Error: Please enter exactly 6 statistics.")
            elif not all(stat.strip().isdigit() for stat in stats):
                print("Error: Statistics should be numeric.")
            else:
                return stats

    @staticmethod
    def _input_health():
        """Inputs health for the character."""
        while True:
            health = input("Enter Health: ")
            if health.isdigit():
                return health
            else:
                print("Error: Health should be a number.")

    @staticmethod
    def edit_sheet(sheet_name):
        """Edits an existing sheet."""
        print(f"Editing {sheet_name}")
        try:
            with open(sheet_name, 'r') as file:
                data = file.readlines()
                SheetEditor._display_current_data(data)

            while True:
                choice = input("Enter the number corresponding to what you want to edit or 'quit' to exit: ")
                if choice.lower() == 'quit':
                    print("Exiting editor.")
                    break

                if choice.isdigit():
                    line_num = int(choice)
                    if 1 <= line_num <= 7:
                        new_value = SheetEditor._get_new_value(line_num)
                        data[line_num - 1] = f"{new_value}\n"
                        with open(sheet_name, 'w') as file:
                            file.writelines(data)
                        print("Sheet updated successfully.")
                    else:
                        print("Error: Option number must be between 1 and 7.")
                else:
                    print("Error: Invalid input. Please enter a number.")

        except FileNotFoundError:
            print("Sheet not found.")

    @staticmethod
    def _display_current_data(data):
        """Displays current data of the sheet."""
        print("Current data:")
        labels = ["Name", "Class", "Statistics", "Health", "Inventory content", "Abilities", "History"]
        for i, label in enumerate(labels):
            print(f"{i + 1}. {label}: {data[i].strip()}")

    @staticmethod
    def _get_new_value(line_num):
        """Gets new value for the specified line number."""
        if line_num in [1, 2, 5, 6, 7]: 
            return input(f"Enter new {['Name', 'Class', 'Statistics', 'Health', 'Inventory content', 'Abilities', 'History'][line_num - 1]}: ")
        elif line_num == 3:
            return ' '.join(SheetEditor._input_stats())
        elif line_num == 4:
            return SheetEditor._input_health()

class DiceRoller:
    def __init__(self):
        self.dice_types = {
            'd4': 4,
            'd6': 6,
            'd8': 8,
            'd10': 10,
            'd12': 12,
            'd20': 20,
            'd100': 100
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
        self.sheet_name = ''

    def do_SheetExplain(self, line):
        """Explains sheets text file lines"""
        print("1. Name\n2. Class\n3. Stats\n4. Health\n5. inventory\n6. Abilities\n7. History")

    def do_CreateSheet(self, line):
        """Creates a new sheet"""
        new_sheet_name = input("Enter file name: ")
        SheetEditor.create_sheet(new_sheet_name)
        self.sheet_name = new_sheet_name

    def do_ImportSheet(self, line):
        """Imports an existing sheet"""
        imported_sheet_name = input("Enter file name: ")
        SheetEditor.import_sheet(imported_sheet_name)
        self.sheet_name = imported_sheet_name

    def do_EditSheet(self, line):
        """Edit an imported/created sheet"""
        if self.sheet_name == '':
            print("No imported/created sheet. Create a sheet with command 'CreateSheet' or import one using 'ImportSheet'")
        else:
            SheetEditor.edit_sheet(self.sheet_name)

    def do_SheetName(self, line):
        """Displays sheet name"""
        if self.sheet_name == '':
            print("No imported/created sheet. Create a sheet with command 'CreateSheet' or import one using 'ImportSheet'")
        else:
            print(self.sheet_name)

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
