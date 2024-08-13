
from yangify.parser import Parser, ParserData, unneeded
from vht.common.parsers.VHT_bgp_cfg.bgp import *
from vht.helper import *
from pprint import pprint
from scanf import scanf

class Bgp_NexthopTrigger_Impl(Bgp_NexthopTrigger):

    class Yangify(Bgp_NexthopTrigger.Yangify):
        def __init__(self, *args, **kwargs):
            super(Bgp_NexthopTrigger_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Bgp_NexthopTrigger_Impl, self).__init__(*args, **kwargs)
class Bgp_Impl(Bgp):

    class Yangify(Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Bgp_Impl, self).__init__(*args, **kwargs)
    nexthop_trigger = Bgp_NexthopTrigger_Impl
