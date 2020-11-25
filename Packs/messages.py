# -- coding: utf-8 --

from colorama import Fore, Back, Style
import time, sys


def currectmsg(string):
    print(Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + 'Great! Your setting is ' + Fore.LIGHTRED_EX + string)
    print(Style.RESET_ALL)
    time.sleep(1)


def finishmsg():
    print('')
    print(Back.GREEN, Fore.RED + '*** Execution finished *** ' + Style.RESET_ALL)
    print(Style.RESET_ALL + '')


def successmsg():
    print('')
    print(Back.LIGHTGREEN_EX, Fore.RED + '*** Execution succeed *** ' + Style.RESET_ALL)
    print(Style.RESET_ALL + '')


def runningmsg():
    print(Style.RESET_ALL)
    print('Now loading thread process, Please wait...')
    print(Style.RESET_ALL)


def wrongmsg():
    print(Style.RESET_ALL)
    print(Fore.LIGHTRED_EX, Style.BRIGHT + 'Wrong format, try it again please.')
    print(Style.RESET_ALL)
    time.sleep(1)


def faildmsg():
    print('')
    print(Back.LIGHTYELLOW_EX, Fore.RED + '*** Execution failed *** ' + Style.RESET_ALL)
    print(Style.RESET_ALL + '')


def errormsg():
    print(Style.RESET_ALL)
    print(Fore.YELLOW,
          Style.BRIGHT + '*** The daemon encountered an unrecoverable error and the process will be killed due to '
                         'security issues ***' + Style.RESET_ALL)
    print(Style.RESET_ALL)


def settingmsg():
    print('')
    print('*** Welcome to use HyperVisor Link Settings Menu ***')
    print('')
    print(Fore.YELLOW, Style.BRIGHT + 'Please complete all option values as much as possible')
    print(Style.RESET_ALL + '')
    time.sleep(1)
    print('--------------------------')
    print('1. MySQL Settings')
    print('2. Port Settings')
    print('3. API Settings')
    print('--------------------------')
    time.sleep(1)


def mainmenumsg():
    print('')
    print('*** Welcome to use HyperVisor Link Main Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. Install requests')
    print('2. Settings menu')
    print('3. Web menu')
    print('4. Control menu')
    print('--------------------------')
    time.sleep(1)


def controlmenumsg():
    print('')
    print('*** Welcome to use HyperVisor Link Control Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. List all VMs')
    print('2. Start a VM')
    print('3. Stop a VM')
    print('4. Reset a VM')
    print('5. Find a VM')
    print('6. Create a new VM')
    print('7. Create a backup-point')
    print('8. Delete a VM')
    print('9. Delete a backup-point')
    print('10. Import a VM from a template')
    print('11. Export a VM into the template')
    print('q. Exit the menu')
    print('--------------------------')
    time.sleep(1)


def newvmmenumsg():
    print('')
    print('*** New-VM Settings & Manage Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. Continue to create a new VM')
    print('q. Exit the menu')
    print('--------------------------')
    time.sleep(1)

def importvmmenumsg():
    print('')
    print('*** Import VM Manage Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. Import and create a copy of the VM')
    print('2. Import and register the VM in place')
    print('3. Import and move the VM to a new location')
    print('q. Exit the menu')
    print('--------------------------')
    time.sleep(1)