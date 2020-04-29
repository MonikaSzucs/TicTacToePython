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
