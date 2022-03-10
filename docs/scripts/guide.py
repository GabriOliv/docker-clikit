#!/usr/bin/env python3

#ARG Parser
import argparse
#Escape colors
import os
#Terminal Size 
from typing import Container, List

# ARG parse
# ARG --help -h
parser = argparse.ArgumentParser(
    prog = 'DockerStart',
    formatter_class=argparse.RawTextHelpFormatter,
    description='Show Docker Project Information'
)

# List Alias
parser.add_argument(
    '-a',
    '--alias',
    action='count',
    help = 'List of Alias\n - command\n - example\n - description'
)

# List Commands
parser.add_argument(
    '-p',
    '--package',
    action='count',
    help = 'List of Packages Installed\n - name\n - example\n - description'
)

# Parser
args = parser.parse_args()

#Image Name
IMAGE_NAME = "CLI Kit"

#Terminal Attributes
ROWS, COLUMNS = os.popen('stty size', 'r').read().split()
COLUMNS = int(float(COLUMNS)*4/5)

#Color List     Black         Red           Green         Yellow        Blue          Magenta       Cyan          Light gray    Dark gray     Light red     Light green   Light yellow  Light blue    Light magenta Light cyan    White
COLOR_LIST = [  '\u001b[30m', '\u001b[31m', '\u001b[32m', '\u001b[33m', '\u001b[34m', '\u001b[35m', '\u001b[36m', '\u001b[37m', '\u001b[90m', '\u001b[91m', '\u001b[92m', '\u001b[93m', '\u001b[94m', '\u001b[95m', '\u001b[96m', '\u001b[97m']



# Ascii Logos
logo = '''
\u001b[34m ____             _              \u001b[32m  ____ _     ___   _  ___ _   
\u001b[34m|  _ \  ___   ___| | _____ _ __  \u001b[32m / ___| |   |_ _| | |/ (_) |_ 
\u001b[34m| | | |/ _ \ / __| |/ / _ \ '__| \u001b[32m| |   | |    | |  | ' /| | __|
\u001b[34m| |_| | (_) | (__|   <  __/ |    \u001b[32m| |___| |___ | |  | . \| | |_ 
\u001b[34m|____/ \___/ \___|_|\_\___|_|    \u001b[32m \____|_____|___| |_|\_\_|\__|'''

logo_title = '''  ____ _     ___   _  ___ _   
 / ___| |   |_ _| | |/ (_) |_ 
| |   | |    | |  | ' /| | __|
| |___| |___ | |  | . \| | |_ 
 \____|_____|___| |_|\_\_|\__|'''

logo_image = ''' ____             _
|  _ \  ___   ___| | _____ _ __
| | | |/ _ \ / __| |/ / _ \ '__|
| |_| | (_) | (__|   <  __/ |
|____/ \___/ \___|_|\_\___|_|'''

logo_alias = '''    _    _ _           
   / \  | (_) __ _ ___ 
  / _ \ | | |/ _` / __|
 / ___ \| | | (_| \__ \\
/_/   \_\_|_|\__,_|___/'''

logo_packages = ''' ____            _                         
|  _ \ __ _  ___| | ____ _  __ _  ___  ___ 
| |_) / _` |/ __| |/ / _` |/ _` |/ _ \/ __|
|  __/ (_| | (__|   < (_| | (_| |  __/\__ \\
|_|   \__,_|\___|_|\_\__,_|\__, |\___||___/
                           |___/           '''



def color(input_text: str, color_id: int):
    return (COLOR_LIST[color_id] + input_text + '\u001b[39m')

def bold(input_text: str):
    return ('\u001b[1m'+input_text+'\u001b[0m')

def blink(input_text: str):
    return ('\u001b[5m'+input_text+'\u001b[25m')

class Package:
    def __init__(self, name: str, command: str, description: str):
         self.__name = name
         self.__command = command
         self.__description = description

    # GET
    @property
    def name(self):
        return self.__name

    @property
    def command(self):
        return self.__command

    @property
    def description(self):
        return self.__description



package = [
    Package('atop','atop -M','advanced system & process monitor'),
    Package('bat','bat /root/.bashrc --color=always | less -r',' A cat(1) clone with wings. '),
    Package('bmon','bmon','bandwidth monitor and rate estimator'),
    Package('calcurse','calcurse','text-based calendar'),
    Package('chafa','chafa --help','character art facsimile generator'),
    Package('cmatrix','cmatrix -bs','simulates the display from \"The Matrix\"'),
    Package('cmus','cmus','lightweight ncurses music player'),
    Package('ctop','ctop','top-like interface for container metrics'),
    Package('figlet','figlet Docker.Feels','output banner with large characters '),
    Package('git','git','git is a fast, scalable, distributed revision control system'),
    Package('glances','glances','monitoring tool which aims to present a large amount of information'),
    Package('hollywood','hollywood','fill your console with Hollywood melodrama technobabble'),
    Package('htop','htop','interactive process viewer'),
    Package('less','less --help','displays the contents of a file or a command output, one page at a time'),
    Package('make','make --help','maintain, update, and regenerate groups of programs'),
    Package('neofetch','dockerfetch','highly customizable system info script'),
    Package('nload','nload','displays the current network usage'),
    Package('nmon','nmon','systems administrator, tuner, benchmark tool'),
    Package('pipes.sh','pipes.sh -Kp4 -c2 -c4','animated pipes terminal screensaver '),
    Package('ranger','ranger','console file manager with VI key bindings'),
    Package('taskwarrior','taskhelp','TODO list from the command line'),
    Package('tmux','tmux','terminal multiplexer, enables a number of terminals from a single screen'),
    Package('top','top','dynamic real-time view of a running system'),
    Package('tree','tree','list contents of directories in a tree-like format'),
    Package('tty-clock','tty-clock -sxc','a terminal digital clock'),
    Package('w3m','w3m github.com/explore','a text based web browser and pager'),
]



alias = [
    Package('guide','python3 /etc/guides/guide.py','Guide of CLI Kit Project'),
    Package('dockerfetch','neofetch --ascii /etc/guides/docker_logo.txt  --ascii_colors 12 15 14 --colors 4 14 12 6 15 8','Custom Neofetch Call'),
    Package('','',''),
    Package('bat','batcat','Shortcut to Bat Project'),
    Package('clock-figlet','while true; do clear; echo "$(date \'+%T\' | figlet -ct)"; echo "[Ctrl+C] to EXIT"; sleep 1; done','Clock using Figlet Command'),
    Package('histcat','history|grep','Command History Search'),
    Package('taskhelp','cat /etc/guides/taskwarrior_guide.txt','TaskWarrior Guide'),
    Package('alias','rawraw','format'),
    Package('alias','rawraw','format'),
    Package('alias','rawraw','format')
]



if type(args.alias) != int and type(args.package) != int :
    print( bold( logo ) )
    print( bold( "\nDocker Project - " + IMAGE_NAME ) )
    print( color( "$ Version 1.0.2", 10 ) )



print( color( ''.ljust( COLUMNS, '_' ), 8 ) )
print("\nUse: 'guide -h' for more info")
print( color( ''.ljust( COLUMNS, '_' ), 8 ) + "\n" )



if type(args.alias) == int:
    print( bold( color( logo_alias, 14 ) ) )
    print( color( ''.ljust( COLUMNS, '_' ), 8 ) )

    for i in alias:
        print(
            (bold(color(i.name,2)) + "   " ),
            color( i.description.capitalize(), 8)
        )
        print(color( i.command, 14))
        print(color(''.ljust(COLUMNS,'_'),8))



if type(args.package) == int:
    print( bold( color( logo_packages, 14 ) ) )
    print( color( ''.ljust( COLUMNS, '_' ), 8 ) )

    #List Package Objects
    for i in package:
        print(
            (bold(color(i.name.capitalize(),2)) + "   " ).center(35),
            color( i.description.capitalize(), 7)
        )

        print(
            ''.ljust(17),
            color( i.command, 14)
        )
        print(color(''.ljust(COLUMNS,'_'),8))


