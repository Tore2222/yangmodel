
from vht.common.parsers.VHT_segment_routing.segment_routing import *
from yangify.parser import Parser, ParserData, unneeded
from vht.helper import *
from pprint import pprint
from scanf import scanf

class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Index_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Index):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Index.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Index_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Index_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Absolute_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Absolute):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Absolute.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Absolute_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Absolute_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_LabelType_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['segment-routing', 'connected-prefix-sid', 'address-family', 'ipv4']


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl, self).__init__(*args, **kwargs)
        self.leaffamily_extract_paths['index'] = ['index', '#text']
        self.leaffamily_extract_paths['absolute'] = ['absolute', '#text']

    def leaffamily_extract_source(self):
        return self.yy.native

    def extract_index(self):
        return search_by_path(self.leaffamily_extract_source(),
                              self.leaffamily_extract_paths['index'])

    @debug_function(log_exit=True, log_return=True)
    @casting(int)
    def index(self):
        return self.extract_index()

    def extract_absolute(self):
        return search_by_path(self.leaffamily_extract_source(),
                              self.leaffamily_extract_paths['absolute'])

    @debug_function(log_exit=True, log_return=True)
    @casting(int)
    def absolute(self):
        return self.extract_absolute()

class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl, self).__init__(*args, **kwargs)
    prefixes = SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl

class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Impl, self).__init__(*args, **kwargs)
    ipv4 = SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl

class SegmentRouting_Mpls_ConnectedPrefixSidMap_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap):

    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_Impl, self).__init__(*args, **kwargs)
    address_family = SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Impl

class SegmentRouting_Mpls_GlobalBlock_Impl(SegmentRouting_Mpls_GlobalBlock):

    class Yangify(SegmentRouting_Mpls_GlobalBlock.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_GlobalBlock_Impl.Yangify, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_GlobalBlock_Impl, self).__init__(*args, **kwargs)

    def extract_range_start(self):
        text = search_by_path(self.leaffamily_extract_source(), ['segment-routing', 'global-block', '#text'])
        if text:
            range_start, _ = scanf("%d %d", text)
            return range_start
        return None

    def extract_range_start(self):
        text = search_by_path(self.leaffamily_extract_source(), ['segment-routing', 'global-block', '#text'])
        if text:
            _, range_end = scanf("%d %d", text)
            return range_end
        return None

class SegmentRouting_Mpls_LocalBlock_Impl(SegmentRouting_Mpls_LocalBlock):

    class Yangify(SegmentRouting_Mpls_LocalBlock.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_LocalBlock_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_LocalBlock_Impl, self).__init__(*args, **kwargs)

    def extract_range_start(self):
        text = search_by_path(self.leaffamily_extract_source(), ['segment-routing', 'local-block', '#text'])
        if text:
            range_start, _ = scanf("%d %d", text)
            return range_start
        return None

    def extract_range_start(self):
        text = search_by_path(self.leaffamily_extract_source(), ['segment-routing', 'local-block', '#text'])
        if text:
            _, range_end = scanf("%d %d", text)
            return range_end
        return None

class SegmentRouting_Mpls_Impl(SegmentRouting_Mpls):

    class Yangify(SegmentRouting_Mpls.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_Impl.Yangify, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_Impl, self).__init__(*args, **kwargs)
    connected_prefix_sid_map = SegmentRouting_Mpls_ConnectedPrefixSidMap_Impl

    global_block = SegmentRouting_Mpls_GlobalBlock_Impl

    local_block = SegmentRouting_Mpls_LocalBlock_Impl

class SegmentRouting_TrafficEng_AffinityMap_Impl(SegmentRouting_TrafficEng_AffinityMap):

    class Yangify(SegmentRouting_TrafficEng_AffinityMap.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_AffinityMap_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_AffinityMap_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List_Impl(SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List):

    class Yangify(SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Pcc_Pce_Impl(SegmentRouting_TrafficEng_Pcc_Pce):

    class Yangify(SegmentRouting_TrafficEng_Pcc_Pce.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Pcc_Pce_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Pcc_Pce_Impl, self).__init__(*args, **kwargs)
    pce_ipv4_list = SegmentRouting_TrafficEng_Pcc_Pce_PceIpv4List_Impl

class SegmentRouting_TrafficEng_Pcc_Impl(SegmentRouting_TrafficEng_Pcc):

    class Yangify(SegmentRouting_TrafficEng_Pcc.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Pcc_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Pcc_Impl, self).__init__(*args, **kwargs)
    pce = SegmentRouting_TrafficEng_Pcc_Pce_Impl

class SegmentRouting_TrafficEng_Policy_BindingSid_Impl(SegmentRouting_TrafficEng_Policy_BindingSid):

    class Yangify(SegmentRouting_TrafficEng_Policy_BindingSid.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_BindingSid_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_BindingSid_Impl, self).__init__(*args, **kwargs)
        self.leaffamily_extract_paths['mpls'] = ['binding-sid', 'mpls', '#text']

    def leaffamily_extract_source(self):
        return self.yy.native

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_Impl, self).__init__(*args, **kwargs)
    exclude_any = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_ExcludeAny_Impl

    include_all = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAll_Impl

    include_any = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_IncludeAny_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Impl, self).__init__(*args, **kwargs)
    affinity = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Affinity_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Impl, self).__init__(*args, **kwargs)
    metric = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep_Metric_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl, self).__init__(*args, **kwargs)
    #metric = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric_Impl
    pcep = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Pcep

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl, self).__init__(*args, **kwargs)
    dynamic = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl

'''class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList_Impl, self).__init__(*args, **kwargs)'''
class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl, self).__init__(*args, **kwargs)
    #segment_list = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_SegmentList_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Impl, self).__init__(*args, **kwargs)
    explicit = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['candidate-paths', 'preference']

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl, self).__init__(*args, **kwargs)
    constraints = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths):

    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl, self).__init__(*args, **kwargs)
    preference = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl

class SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl(SegmentRouting_TrafficEng_Policy_ColorEndpoint):

    class Yangify(SegmentRouting_TrafficEng_Policy_ColorEndpoint.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl, self).__init__(*args, **kwargs)
        self.leaffamily_extract_paths['color'] = ['color', '#text']

    def leaffamily_extract_source(self):
        return self.yy.native

    def extract_color(self):
        text = search_by_path(self.leaffamily_extract_source(), ['color', '#text'])
        try:
            color, _ = scanf("%d endpoint %s", text)
            return color
        except Exception as e:
            return None

    def extract_end_point(self):
        text = search_by_path(self.leaffamily_extract_source(), ['color', '#text'])
        try:
            _, end_point = scanf("%d endpoint %s", text)
            return end_point
        except Exception as e:
            return None


class SegmentRouting_TrafficEng_Policy_Impl(SegmentRouting_TrafficEng_Policy):

    class Yangify(SegmentRouting_TrafficEng_Policy.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['segment-routing', 'traffic-eng', 'policy']

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_Impl, self).__init__(*args, **kwargs)
    binding_sid = SegmentRouting_TrafficEng_Policy_BindingSid_Impl

    candidate_paths = SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl

    color_endpoint = SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl

class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Adjacency_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Adjacency):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Adjacency.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Adjacency_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Adjacency_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Label_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Label):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Label.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Label_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Label_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Prefix_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Prefix):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Prefix.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Prefix_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Prefix_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_SidType_Impl, self).__init__(*args, **kwargs)
class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_Impl, self).__init__(*args, **kwargs)

    def leaffamily_extract_source(self):
        return self.yy.native

    def extract_adjacency(self):
        try:
            text = search_by_path(self.leaffamily_extract_source(), ['#text'])
            adjacency = scanf("mpls adjacency %s", text)
            return adjacency[0]
        except Exception as e:
            return None

    def extract_label(self):
        try:
            text = search_by_path(self.leaffamily_extract_source(), ['#text'])
            label = scanf("mpls label %d", text)
            return label
        except Exception as e:
            return None

    def extract_prefix(self):
        try:
            text = search_by_path(self.leaffamily_extract_source(), ['#text'])
            prefix = scanf("mpls prefix %s", text)
            return prefix[0]
        except Exception as e:
            return None

class SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Impl(SegmentRouting_TrafficEng_SegmentList_SegmentEntry):

    class Yangify(SegmentRouting_TrafficEng_SegmentList_SegmentEntry.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['index']

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Impl, self).__init__(*args, **kwargs)
    mpls = SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Mpls_Impl

class SegmentRouting_TrafficEng_SegmentList_Impl(SegmentRouting_TrafficEng_SegmentList):

    class Yangify(SegmentRouting_TrafficEng_SegmentList.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_Impl.Yangify, self).__init__(*args, **kwargs)
            self.elements_extract_path = ['segment-routing', 'traffic-eng', 'segment-list', 'name']

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_Impl, self).__init__(*args, **kwargs)
    index = SegmentRouting_TrafficEng_SegmentList_SegmentEntry_Impl

class SegmentRouting_TrafficEng_Impl(SegmentRouting_TrafficEng):

    class Yangify(SegmentRouting_TrafficEng.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Impl, self).__init__(*args, **kwargs)
    pcc = SegmentRouting_TrafficEng_Pcc_Impl

    affinity_map = SegmentRouting_TrafficEng_AffinityMap_Impl

    policy = SegmentRouting_TrafficEng_Policy_Impl

    segment_list = SegmentRouting_TrafficEng_SegmentList_Impl

class SegmentRouting_Impl(SegmentRouting):

    class Yangify(SegmentRouting.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Impl, self).__init__(*args, **kwargs)
    mpls = SegmentRouting_Mpls_Impl

    traffic_eng = SegmentRouting_TrafficEng_Impl
