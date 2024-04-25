import unittest
from unittest.mock import patch
from io import StringIO
import os
from Kursinis import SheetEditor, DiceRoller, CommandInterface

class TestSheetEditor(unittest.TestCase):
    def setUp(self):
        self.test_sheet_name = "test_sheet.txt"

    @patch('builtins.input', side_effect=['New Name', 'New Class', '10 12 14 8 15 16', '30', 'New Inventory', 'New Abilities', 'New History'])
    def test_create_sheet(self, mock_input):
        SheetEditor.create_sheet(self.test_sheet_name)
        self.assertTrue(os.path.isfile(self.test_sheet_name))

    @patch('builtins.input', side_effect=['1', 'New Value', 'quit'])
    def test_edit_sheet(self, mock_input):
        with open(self.test_sheet_name, 'w') as f:
            f.write("Old Name\nOld Class\n10 12 14 8 15 16\n30\nOld Inventory\nOld Abilities\nOld History\n")
        SheetEditor.edit_sheet(self.test_sheet_name)
        with open(self.test_sheet_name, 'r') as f:
            content = f.readlines()
            self.assertEqual(content[0].strip(), 'New Value')  # Assuming Name is edited

    def tearDown(self):
        try:
            os.remove(self.test_sheet_name)
        except FileNotFoundError:
            pass

class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        self.roller = DiceRoller()

    @patch('sys.stdout', new_callable=StringIO)
    def test_roll_dice(self, mock_stdout):
        self.roller.roll_dice('d6')
        result = mock_stdout.getvalue().strip()
        self.assertTrue(result.startswith('Rolling d6: '))
        value = int(result.split(': ')[1])
        self.assertTrue(1 <= value <= 6)

class TestCommandInterface(unittest.TestCase):
    def setUp(self):
        self.command_interface = CommandInterface()

    def test_quit(self):
        result = self.command_interface.do_Quit('')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()