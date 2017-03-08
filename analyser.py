import lexer

# -----------------------------------------------------------------
# Token -----------------------------------------------------------
# -----------------------------------------------------------------
class Token(object):
    def __init__(self,type,value,ltoken,rtoken):
        # token type: INTEGER, PLUS
        self.type = type
        # token value: a number, '+' or None
        self.value = value
        self.ltoken = Token(ltoken)
        self.rtoken = Token(rtoken)
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = self.value
            )
    def __repr__(self):
        return self.__str__()
# Parser ----------------------------------------------------------
def Parser(current_line_program):
    # cursor ------------------------------------------------------
    print 'en construction'

def interpretor(list_program):
    # curseur -------------------------------------------------
    pos = 0
    current_line = list_program[pos]
    while current_line != 'END':        
        listToken = current_line.split(' ')

        print listToken
        # analyse lexica --------------------------------------

        if lexer.stype_dictionnary.has_key(listToken[0]):
            
            # Dictionnary error check -------------------------
            if (len(listToken) > 2) and lexer.tvar_dictionnary.has_key(listToken[1]) and lexer.stype_dictionnary.has_key(listToken[1]) and lexer.sop_dictionnary.has_key(listToken[1]):
                raise IndentationError('syntaxe error: int definition at line {}'.format(pos))
            # Add new var to dictionnary ----------------------
            lexer.tvar_dictionnary.update({str(listToken[1]): 0 })
            print 'Integer created and loaded in tvar_dictionnary'

        elif lexer.tvar_dictionnary.has_key(listToken[0]):
            if len(listToken) == 1:
                print 'It\'s {}:{}'.format(str(listToken[0]), lexer.tvar_dictionnary[str(listToken[0])])
            else:
                if listToken[1] == '=':
                    print 'call of calculator: not implemented'
                else:
                    raise IndentationError('syntaxe error')

        elif str(listToken[0]) == '':
            print 'blank'
        else:
            raise IndentationError('syntaxe error')

        pos += 1
        print
        current_line = list_program[pos]


