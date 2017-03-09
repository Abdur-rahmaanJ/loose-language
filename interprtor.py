#!/usr/python

import sys

def fileToList(path_program):
    if path_program.find('.loose') == len(path_program)-1:
        raise TypeError('Wrong type file')
    
    f = open(str(path_program), 'r')
    str_buf = f.read()
    f.close

    str_buf = str_buf.replace('\n','')
    return str_buf.split(';')

def main():
    try:
        if len(sys.argv) == 0 and len(sys.argv) > 2:
            raise TypeError('one argument needed')
        print fileToList(sys.argv[1])

    except TypeError as e:
        print e
    except KeyboardInterrupt:
        print 'Halting requested'



if __name__ == '__main__':
    main()
