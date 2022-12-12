from jsonpath_ng import parse
from .paginate import ec2_paginate

#####################################

class describe_regions(ec2_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('Regions[*]')

#####################################

class describe_instances(ec2_paginate):
    def name(self): return __class__.__name__        
    def jsonpath_expression(self): return parse('Reservations[*].Instances[*]')

#####################################

class describe_vpc_endpoints(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('VpcEndpoints[*]')

#####################################

class describe_nat_gateways(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('NatGateways[*]')

#####################################

class describe_subnets(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('Subnets[*]')

#####################################

class describe_route_tables(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('RouteTables[*]')

#####################################

class describe_prefix_lists(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('PrefixLists[*]')

#####################################

class describe_vpcs(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('Vpcs[*]')

#####################################

class describe_instance_types(ec2_paginate):
    def name(self): return __class__.__name__
    def jsonpath_expression(self): return parse('InstanceTypes[*]')