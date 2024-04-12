#komandu list'as "/help" 
#importuot egzistuojanti sheeta arba sukurt nauja
#sheeta editint
#pakeist health skaiciu
#inventorius
#ability list
#edit statistics
#dice roller

import cmd

class CommandInterface(cmd.Cmd):
    prompt = '> '
    intro = 'Welcome to DND helper. Type "help" for available commands.'
    
    def do_SheetExplain(self, line):
        """Explains sheets text file lines"""
        print("1. Name\n2. Class\n3. Stats\n4. Health\n5. inventory\n6. Abilities\n7. History")

    def do_ImportSheet(self, line):
        """Imports and existing sheet"""
        f = open('Sheet1.txt', 'r').read()

    def do_Quit(self, line):
        """Exits DND helper"""
        return True
    
    def postcmd(self, stop, line):
        print()  
        return stop
    
if __name__ == '__main__':
    CommandInterface().cmdloop()