#komandu list'as "/help" 
#importuot egzistuojanti sheeta arba sukurt nauja
#sheeta editint
#pakeist health skaiciu
#inventorius
#ability list
#edit statistics
#dice roller

#cmd puslapis
#https://medium.com/@noransaber685/simple-guide-to-creating-a-command-line-interface-cli-in-python-c2de7b8f5e05

import cmd
class SheetImporter:
    
    @staticmethod
    def import_sheet(importedSheetName):
        print("Importing importedSheetName:", importedSheetName, "\n")
        try:
            with open(importedSheetName, 'r') as file:
                for line in file:
                    print(line.strip())
                
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)
    
class CommandInterface(cmd.Cmd, SheetImporter):
    prompt = '> '
    intro = 'Welcome to DND helper. Type "help" for available commands.'
    
    def __init__(self):
        super().__init__()
        self.sheetName = 'No imported Sheet'
        
    def do_SheetExplain(self, line):
        """Explains sheets text file lines"""
        print("1. Name\n2. Class\n3. Stats\n4. Health\n5. inventory\n6. Abilities\n7. History")

    def do_ImportSheet(self, line):
        """Imports an existing sheet"""
        importedSheetName = input("Enter file name: ")
        SheetImporter.import_sheet(importedSheetName)
        self.sheetName = importedSheetName
    
    def do_SheetName(self, line):
        """Displays sheet name"""
        print(self.sheetName)
    
    def do_Quit(self, line):
        """Exits DND helper"""
        return True
    
    def postcmd(self, stop, line):
        print()  
        return stop
    
if __name__ == '__main__':
    CommandInterface().cmdloop()