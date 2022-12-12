from jsonpath_ng import parse
from .paginate import ddb_paginate

#####################################

class list_tables(ddb_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('TableNames[*]')