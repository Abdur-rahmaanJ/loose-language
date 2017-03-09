#!/usr/python

import sys

PLUS, MINUS, EGAL = '+', '-', '='

sfon_dictionnay = {'print': print}
tvar_dictionnay = {}

def fileToList(path_program):
    if path_program.find('.loose') == len(path_program)-1:
        raise TypeError('Wrong type file')
    
    f = open(str(path_program), 'r')
    str_buf = f.read()
    f.close

    str_buf = str_buf.replace('\n','')
    list_buf = str_buf.split(';')

    for i in range(0,len(list_buf)-1): 
        if list_buf[i] == '':
            del list_buf[i]
    return list_buf

def interprtor(list_program):
    for line in list_program:
        line =  line.replace(' ','')
        
        
        print line

def main():
    try:
        if len(sys.argv) == 0 and len(sys.argv) > 2:
            raise TypeError('one argument needed')
        interprtor(fileToList(sys.argv[1]))
    except TypeError as e:
        print e
    except KeyboardInterrupt:
        print 'Halting requested'

if __name__ == '__main__':
    main()
