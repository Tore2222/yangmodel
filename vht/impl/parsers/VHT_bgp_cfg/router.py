
from yangify.parser import Parser, ParserData, unneeded
from vht.common.parsers.VHT_bgp_cfg.router import *
from vht.helper import *
from pprint import pprint
from scanf import scanf

class Router_Bgp_Bgp_Impl(Router_Bgp_Bgp):

    class Yangify(Router_Bgp_Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Bgp_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_Neighbor_PeerGroup_Password_Impl(Router_Bgp_Neighbor_PeerGroup_Password):

    class Yangify(Router_Bgp_Neighbor_PeerGroup_Password.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_PeerGroup_Password_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_PeerGroup_Password_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_Neighbor_PeerGroup_Impl(Router_Bgp_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
    password = Router_Bgp_Neighbor_PeerGroup_Password_Impl

class Router_Bgp_Neighbor_Ipv4Neighbor_Password_Impl(Router_Bgp_Neighbor_Ipv4Neighbor_Password):

    class Yangify(Router_Bgp_Neighbor_Ipv4Neighbor_Password.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_Ipv4Neighbor_Password_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_Ipv4Neighbor_Password_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
    password = Router_Bgp_Neighbor_Ipv4Neighbor_Password_Impl

class Router_Bgp_Neighbor_Ipv6Neighbor_Password_Impl(Router_Bgp_Neighbor_Ipv6Neighbor_Password):

    class Yangify(Router_Bgp_Neighbor_Ipv6Neighbor_Password.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_Ipv6Neighbor_Password_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_Ipv6Neighbor_Password_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
    password = Router_Bgp_Neighbor_Ipv6Neighbor_Password_Impl

class Router_Bgp_Neighbor_Impl(Router_Bgp_Neighbor):

    class Yangify(Router_Bgp_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_Timers_Bgp_Impl(Router_Bgp_Timers_Bgp):

    class Yangify(Router_Bgp_Timers_Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Timers_Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Timers_Bgp_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_Timers_Impl(Router_Bgp_Timers):

    class Yangify(Router_Bgp_Timers.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Timers_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Timers_Impl, self).__init__(*args, **kwargs)
    bgp = Router_Bgp_Timers_Bgp_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_Impl, self).__init__(*args, **kwargs)
    nexthop_trigger = Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_NexthopTrigger_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
    send_label = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_SendLabel_Impl

    route_map = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
    send_label = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_SendLabel_Impl

    route_map = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
    send_label = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_SendLabel_Impl

    route_map = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_Network_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Network):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Network.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Network_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Network_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Impl, self).__init__(*args, **kwargs)
    connected = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Connected_Impl

    isis = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Isis_Impl

    rip = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Rip_Impl

    static = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Static_Impl

    ospf = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Ospf_Impl

class Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Unicast_Impl(Router_Bgp_AddressFamily_Ipv4_Unicast):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Unicast.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Unicast_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Unicast_Impl, self).__init__(*args, **kwargs)
    bgp = Router_Bgp_AddressFamily_Ipv4_Unicast_Bgp_Impl

    neighbor = Router_Bgp_AddressFamily_Ipv4_Unicast_Neighbor_Impl

    redistribute = Router_Bgp_AddressFamily_Ipv4_Unicast_Redistribute_Impl

    segment_routing = Router_Bgp_AddressFamily_Ipv4_Unicast_SegmentRouting_Impl

    network = Router_Bgp_AddressFamily_Ipv4_Unicast_Network_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_Impl, self).__init__(*args, **kwargs)
    nexthop_trigger = Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_NexthopTrigger_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Network_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Network):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Network.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Network_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Network_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Impl, self).__init__(*args, **kwargs)
    connected = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Connected_Impl

    isis = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Isis_Impl

    rip = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Rip_Impl

    static = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Static_Impl

    ospf = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Ospf_Impl

class Router_Bgp_AddressFamily_Ipv4_Vrf_Impl(Router_Bgp_AddressFamily_Ipv4_Vrf):

    class Yangify(Router_Bgp_AddressFamily_Ipv4_Vrf.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Vrf_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Vrf_Impl, self).__init__(*args, **kwargs)
    bgp = Router_Bgp_AddressFamily_Ipv4_Vrf_Bgp_Impl

    neighbor = Router_Bgp_AddressFamily_Ipv4_Vrf_Neighbor_Impl

    redistribute = Router_Bgp_AddressFamily_Ipv4_Vrf_Redistribute_Impl

    network = Router_Bgp_AddressFamily_Ipv4_Vrf_Network_Impl

class Router_Bgp_AddressFamily_Ipv4_Impl(Router_Bgp_AddressFamily_Ipv4):

    class Yangify(Router_Bgp_AddressFamily_Ipv4.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Ipv4_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Ipv4_Impl, self).__init__(*args, **kwargs)
    unicast = Router_Bgp_AddressFamily_Ipv4_Unicast_Impl

    vrf = Router_Bgp_AddressFamily_Ipv4_Vrf_Impl

class Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup_Impl(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Impl(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_AddressFamily_Rtfilter_Unicast_Impl(Router_Bgp_AddressFamily_Rtfilter_Unicast):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter_Unicast.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Unicast_Impl, self).__init__(*args, **kwargs)
    neighbor = Router_Bgp_AddressFamily_Rtfilter_Unicast_Neighbor_Impl

class Router_Bgp_AddressFamily_Rtfilter_Impl(Router_Bgp_AddressFamily_Rtfilter):

    class Yangify(Router_Bgp_AddressFamily_Rtfilter.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Rtfilter_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Rtfilter_Impl, self).__init__(*args, **kwargs)
    unicast = Router_Bgp_AddressFamily_Rtfilter_Unicast_Impl

class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_RouteMap_Impl

class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
    route_map = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_RouteMap_Impl

class Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_AddressFamily_Vpnv4_Unicast_Impl(Router_Bgp_AddressFamily_Vpnv4_Unicast):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4_Unicast.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Unicast_Impl, self).__init__(*args, **kwargs)
    neighbor = Router_Bgp_AddressFamily_Vpnv4_Unicast_Neighbor_Impl

class Router_Bgp_AddressFamily_Vpnv4_Impl(Router_Bgp_AddressFamily_Vpnv4):

    class Yangify(Router_Bgp_AddressFamily_Vpnv4.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Vpnv4_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Vpnv4_Impl, self).__init__(*args, **kwargs)
    unicast = Router_Bgp_AddressFamily_Vpnv4_Unicast_Impl

class Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup_Impl(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup):

    class Yangify(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor_Impl(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor):

    class Yangify(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor_Impl(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor):

    class Yangify(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor_Impl, self).__init__(*args, **kwargs)
class Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Impl(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor):

    class Yangify(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Impl, self).__init__(*args, **kwargs)
    peer_group = Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_PeerGroup_Impl

    ipv4_neighbor = Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv4Neighbor_Impl

    ipv6_neighbor = Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Ipv6Neighbor_Impl

class Router_Bgp_AddressFamily_LinkState_LinkState_Impl(Router_Bgp_AddressFamily_LinkState_LinkState):

    class Yangify(Router_Bgp_AddressFamily_LinkState_LinkState.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_LinkState_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_LinkState_Impl, self).__init__(*args, **kwargs)
    neighbor = Router_Bgp_AddressFamily_LinkState_LinkState_Neighbor_Impl

class Router_Bgp_AddressFamily_LinkState_Impl(Router_Bgp_AddressFamily_LinkState):

    class Yangify(Router_Bgp_AddressFamily_LinkState.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_LinkState_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_LinkState_Impl, self).__init__(*args, **kwargs)
    link_state = Router_Bgp_AddressFamily_LinkState_LinkState_Impl

class Router_Bgp_AddressFamily_Impl(Router_Bgp_AddressFamily):

    class Yangify(Router_Bgp_AddressFamily.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_AddressFamily_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_AddressFamily_Impl, self).__init__(*args, **kwargs)
    ipv4 = Router_Bgp_AddressFamily_Ipv4_Impl

    rtfilter = Router_Bgp_AddressFamily_Rtfilter_Impl

    vpnv4 = Router_Bgp_AddressFamily_Vpnv4_Impl

    link_state = Router_Bgp_AddressFamily_LinkState_Impl

class Router_Bgp_Impl(Router_Bgp):

    class Yangify(Router_Bgp.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Bgp_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Bgp_Impl, self).__init__(*args, **kwargs)
    bgp = Router_Bgp_Bgp_Impl

    neighbor = Router_Bgp_Neighbor_Impl

    timers = Router_Bgp_Timers_Impl

    address_family = Router_Bgp_AddressFamily_Impl

class Router_Impl(Router):

    class Yangify(Router.Yangify):
        def __init__(self, *args, **kwargs):
            super(Router_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(Router_Impl, self).__init__(*args, **kwargs)
    bgp = Router_Bgp_Impl
