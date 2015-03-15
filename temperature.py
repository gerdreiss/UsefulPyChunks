## add something like the lines below to .bash_aliases, .bashrc, .bash_profile etc
## alias c2f='python /home/user/temperature.py c'
## alias f2c='python /home/user/temperature.py f'
## then use c2f 37 to convert Celsius to Fahrenheit, or f2c 75 to convert Fahrenheit to Celsius

import sys

def f_to_c(f):
    return 5*(int(f)-32)/9

def c_to_f(c):
    return 32 + 9*int(c)/5

if len(sys.argv) > 2:
    unit = sys.argv[1]
    number = sys.argv[2]
    if unit == "c":
        print('{0} c = {1} f'.format(number, c_to_f(number)))
    elif unit == "f":
        print("{0} f = {1} c".format( number, f_to_c(number)))
else:
    print("ERROR: unit and number args needed i.e. \"c 0\", \"f 32\"")