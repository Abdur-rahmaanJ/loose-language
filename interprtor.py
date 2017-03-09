#!/usr/python

import sys

PLUS, MINUS, EGAL = '+', '-', '='

sfon_dictionnay = {}
tvar_dictionnay = {}

def fileToList(path_program):
    if path_program.find('.loose') == len(path_program)-1:
        raise TypeError('Wrong type file')
    # open the file and store in a buffer
    f = open(str(path_program), 'r')
    str_buf = f.read()
    f.close
    
    # get ride of the line break and split
    str_buf = str_buf.replace('\n','')
    list_buf = str_buf.split(';')
    
    # get ride of spaces in each element of list_buf
    for i in range(0, len(list_buf)-1):
        list_buf[i] = list_buf[i].replace(' ','')

    i = 0
    # algo to suppress empty elements
    # a master piece : yay...
    while i < len(list_buf): 
        if list_buf[i] == '':
            del list_buf[i]
            if i != 0:
                i = i - 1
        else:
            i = i + 1
        
    return list_buf

def interprtor(list_program): 
    print list_program

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
