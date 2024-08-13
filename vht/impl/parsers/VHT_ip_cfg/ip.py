
from vht.common.parsers.VHT_ip_cfg.ip import *
from yangify.parser import Parser, ParserData, unneeded
from vht.helper import *
from pprint import pprint
from scanf import scanf

class Ip_Route_IpRouteStatic_Impl(Ip_Route_IpRouteStatic):

    class Yangify(Ip_Route_IpRouteStatic.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_IpRouteStatic_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['ip', 'route']

    def __init__(self, *args, **kwargs):
        super(Ip_Route_IpRouteStatic_Impl, self).__init__(*args, **kwargs)
        self.leaffamily_extract_paths['out_if'] = ['out-if', '#text']

    @debug_function(log_exit=True, log_return=True)
    def extract_out_if(self):
        print(self.leaffamily_extract_source())
        return search_by_path(self.leaffamily_extract_source(),
                              self.leaffamily_extract_paths['out_if'])
class Ip_Route_Vrf_IpRouteStatic_Impl(Ip_Route_Vrf_IpRouteStatic):

    class Yangify(Ip_Route_Vrf_IpRouteStatic.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Vrf_IpRouteStatic_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Ip_Route_Vrf_IpRouteStatic_Impl, self).__init__(*args, **kwargs)
class Ip_Route_Vrf_Impl(Ip_Route_Vrf):

    class Yangify(Ip_Route_Vrf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Vrf_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['ip', 'vrf']

    def __init__(self, *args, **kwargs):
        super(Ip_Route_Vrf_Impl, self).__init__(*args, **kwargs)
    ip_route_static = Ip_Route_Vrf_IpRouteStatic_Impl

class Ip_Route_Impl(Ip_Route):

    class Yangify(Ip_Route.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Route_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Ip_Route_Impl, self).__init__(*args, **kwargs)
    ip_route_static = Ip_Route_IpRouteStatic_Impl

    vrf = Ip_Route_Vrf_Impl

class Ip_Impl(Ip):

    class Yangify(Ip.Yangify):
        def __init__(self, *args, **kwargs):
            super(Ip_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Ip_Impl, self).__init__(*args, **kwargs)
    route = Ip_Route_Impl
