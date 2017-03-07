#!/usr/python

# -----------------------------------------------------------------
# Interpretor Tspeech version 0.01 --------------------------------
# Author: Tarek El Saidi ------------------------------------------
# -----------------------------------------------------------------

import sys

# -----------------------------------------------------------------
# static syntax dictionary ----------------------------------------
# -----------------------------------------------------------------

INTEGER, PLUS, MINUS, EGAL = 'INTEGER', 'PLUS', 'MINUS', 'EGAL'

stype_dictionnary = {'int': INTEGER }
sop_dictionnary = {'+':PLUS, '-':MINUS, '=':EGAL }

# tempory variable dictionnary ------------------------------------

tvar_dictionnary = {}

# -----------------------------------------------------------------
# Token -----------------------------------------------------------
# -----------------------------------------------------------------
class Token(object):
    def __init__(self,type,value):
        # token type: INTEGER, PLUS
        self.type = type
        # token value: a number, '+' or None
        self.value = value
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = self.value
            )
    def __repr__(self):
        return self.__str__()

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

def interpretor(list_program):
    # curseur -------------------------------------------------
    pos = 0
    current_line = list_program[pos]
    while current_line != 'END':        
        listToken = current_line.split(' ')

        print listToken
        # analyse lexical     ---------------------------------
        if stype_dictionnary.has_key(listToken[0]):
            print 'It\'s a integer'
            
            # Dictionnary check -------------------------------
            if (len(listToken) > 2) and tvar_dictionnary.has_key(listToken[1]) and stype_dictionnary.has_key(listToken[1]) and sop_dictionnary.has_key(listToken[1]):
                raise IndentationError('syntaxe error: int definition at line {pos}'.format(pos))
            # Add new var to dictionnary ----------------------
            tvar_dictionnary.update({str(listToken[1]): 0 })

        elif str(listToken[0]) == '':
            print 'blank'
        elif isinstance(listToken[0], basestring):
            print 'It\'s a ID'
        else:
            raise IndentationError('syntaxe error')

        pos += 1
        print
        current_line = list_program[pos]

# main() 

def main():
    
    try:

        if len(sys.argv) == 1 or len(sys.argv) > 2:
            raise TypeError('one argument require')
        
        interpretor(splitFile(str(sys.argv[1])))
        print tvar_dictionnary
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
