#!/usr/python
# -----------------------------------------------------------------
# Interpretor Tspeech version 0.01 --------------------------------
# Author: Tarek El Saidi ------------------------------------------
# -----------------------------------------------------------------

import sys
import analyser

# -----------------------------------------------------------------
# splitFile() open a file .ts -------------------------------------
# -----------------------------------------------------------------

def splitFile(nameFile):
    if nameFile.find('.ts') == -1:
        raise TypeError('Wrong extension file')
    
    file_program = open(nameFile,'r')
    buf = file_program.read()
    file_program.close()

    split_program = buf.split('\n')

    return split_program 
# main() 

def main():
    try:
        if len(sys.argv) == 1 or len(sys.argv) > 2:
            raise TypeError('one argument require')
        
        analyser.interpretor(splitFile(str(sys.argv[1])))
        # affiche le tvar_dictionnary
        print analyser.Parser()

    except IndentationError as e:
        print str(e)
        raise
    except TypeError as e:
        print str(e)
        print '--> \'calc2.py nameFile.ts\''
        raise
    except IOError as e:
        print 'I/O error({0}): {1}'.format(e.errno, e.strerror)
    except KeyboardInterrupt:
        print 'Shutdown requested ..'
    sys.exit(0)


if __name__ == '__main__':
    main()
