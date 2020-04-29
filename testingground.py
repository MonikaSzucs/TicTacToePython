import examplemod
examplemod.do_a_thing()

#two different ways to import

from examplemod import do_a_thing, do_another_thing
#or you can do
#from examplemod import *

do_a_thing()
do_another_thing()

#or you can do it like This

from examplemod import do_a_thing as dat
dat()

#or you can do

from moddir.examplemod2 import do_a_thing
do_a_thing()

#google python package index and look through the website to find what you want to install


'''
Adding in Colorama Package
'''

'''
from colorama import Fore, Back, Style, init
init()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now
'''
