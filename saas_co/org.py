from jsonpath_ng import parse
from .paginate import org_paginate

class list_accounts(org_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('Accounts[*]')
