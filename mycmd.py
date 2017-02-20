from __future__ import print_function, division
import cmd

class MyCmd(cmd.Cmd):
    prompt = 'mycmd >>> '
    intro = 'Simple command-line interpreter, mycmd has the following commands \n \
1. deploy 2. kill 3. benchmark 4. report.\n \
Enter your command:'
    
    def do_deploy(self, line):
        print("deploy")

    def do_kill(self,line):
        print("kill")

    def do_benchmark(self,line):
        print("benchmark")

    def do_report(self,line):
        print("report")
    
    def do_EOF(self, line):
        print("bye bye")
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
