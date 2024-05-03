# DnD Helper

- A simple DnD helper program demo. This program makes dnd a bit more manageable by simplifying a few aspects and having useful features.
- Runs by opening .py file on cmd or running the file in an editing program (visual studio code, etc.)
- Interact with the program using implemented commands. To see list of commands, type “help”, or “help (specific command)” to get a description of what the program does.

## Program cover a few key DnD’s functions:

- Creating, importing and/or editing basic character sheet
- Dice roller

1\. Create a sheet using command “CreateSheet” which lets you put in data 1 line at a time prompting you with what information to put in:

```
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
```

Also included are checks for if entered health is a number and if entered statistics consist of a digit for each of its 6 stat:

```
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
```

2\. Using command “ImportSheet” allows you to import an already created sheet in to your program. Interfrace guides you thru the steps of importing your sheet. (Sheet should be placed in the same folder as the program. “.txt” must be added for it to work, for example: Sheet.txt):

```
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
```

3\. Command “EditSheet” allows you to edit the current imported or created sheet. It allows you to edit your sheet by allowing you to type in new information. Also includes same health and stat checks to prevent errors:

```
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
```

4\. Command “RollDice”allows you to roll between a selection of dnd dices:

```
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

These are the main functions of the program:
```

## Patterns used:

1. **Command Pattern -** The CommandInterface class uses the Command Pattern. Each method in this class represents a command that can be executed by the user. These commands (“CreateSheet”, etc.) are invoked by the user through the command-line interface. Each command encapsulates a particular action, and they are invoked dynamically based on user input.
2. **Static Method Pattern**: The SheetEditor class mostly uses static methods for operations like importing a sheet, creating a new sheet, editing a sheet, etc. These methods are stateless and can be called without instantiating the class. This pattern is useful when methods don't rely on instance variables.
3. **Factory Method Pattern**: the DiceRoller class uses Factory Method Pattern. It contains a method roll_dice which generates random numbers based on the input dice type. It could be extended to include more dice types easily.

## 4 OOP pillars:

1\. **Encapsulation**: Encapsulation is the bundling of data (variables) and methods (functions) that operate on the data into a single unit or class. It hides the internal state of an object and only exposes the necessary functionalities.

In the code:

Classes like “SheetEditor”, “DiceRoller”, and “CommandInterface” encapsulate related methods and data together. Methods within these classes operate on the data specific to their functionality. For example, \`SheetEditor\` methods deal with character sheet manipulation, “DiceRoller” methods handle dice rolling, and “CommandInterface” methods manage user interactions.

2\. **Inheritance**: Inheritance allows a class (subclass) to inherit properties and behavior (methods) from another class (superclass). It promotes code reuse and establishes a hierarchical relationship between classes.

In the code:

“CommandInterface” class inherits from Python's “cmd.Cmd” class. This allows “CommandInterface” to inherit built-in command-line interface functionalities and customize them for the DND helper tool without having to redefine everything from scratch.

3\. **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and modularity in code, as different subclasses can provide their own implementations of methods defined in the superclass.

In the code:

A form of polymorphism is used when invoking methods like “SheetEditor.create_sheet()\`” or “DiceRoller.roll_dice()”. These methods can behave differently based on the type of object they are called on.

4\. **Abstraction**: Abstraction refers to the process of hiding the complex implementation details and showing only the necessary features of an object. It allows programmers to focus on what an object does rather than how it does it.

In the code:

The classes and methods provide abstractions over complex functionalities. For example, users interact with the “CommandInterface” class through simple commands (“CreateSheet”, “EditSheet”, etc.) without needing to know the internal implementation details of how these commands are executed. Similarly, the “SheetEditor” class abstracts away the details of file handling and manipulation of character sheet data.

## File reading and writing:

Writing is used for creating a sheet using the command “CreateSheet”:

```
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
```

Writing and reading is used in the edit_sheet method for editing a already created/imported sheet:

```
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
```
## Results and Conclusions:

- The result is a rudimentary DnD helper programs that allows the user to easily manage his sheet, roll different dice without the need for physical dice.
- Of course this is a very bare-bones program. A program for the whole game would require a lot more time and skill, taking in to account how much content the actual DnD sheet holds.
- In the future the program could easily be expanded to have more functions by adding more commands.
- For a full sheet it would require a larger and more complex file reader.
- An front-end interface would make the program a lot more appealing
