
from yangify.translator import Translator, TranslatorData, unneeded
from vht.common.translators.VHT_segment_routing.segment_routing import *
from vht.helper import *
from pprint import pprint


class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes):
    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 6
            self.submode_indent = ' ' * 8
            self.cli_fmt      = "{ipprefix} {label_type} {label_value}"
            self.undo_cli_fmt = "no {ipprefix} {label_type} {label_value}"

        @debug_function(log_exit=True, log_return=True)
        def extract_cli_data2(self, cli_data):
            if 'index' in cli_data:
                cli_data['label_type'] = 'index'
                cli_data['label_value'] = cli_data['index']
            elif 'absolute' in cli_data:
                cli_data['label_type'] = 'absolute'
                cli_data['label_value'] = cli_data['absolute']

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Prefixes_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4):
    class Yangify(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Ipv4_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 4
            self.submode_indent = ' ' * 5
            self.cli_fmt = "address-family ipv4"

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
            self.indent     = ' ' * 2
            self.submode_indent = ' ' * 4
            self.cli_fmt = "connected-prefix-sid"

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_ConnectedPrefixSidMap_Impl, self).__init__(*args, **kwargs)
    address_family = SegmentRouting_Mpls_ConnectedPrefixSidMap_AddressFamily_Impl

class SegmentRouting_Mpls_GlobalBlock_Impl(SegmentRouting_Mpls_GlobalBlock):
    class Yangify(SegmentRouting_Mpls_GlobalBlock.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_GlobalBlock_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 2
            self.submode_indent = ' ' * 4

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_GlobalBlock_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_Mpls_LocalBlock_Impl(SegmentRouting_Mpls_LocalBlock):
    class Yangify(SegmentRouting_Mpls_LocalBlock.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_LocalBlock_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 2
            self.submode_indent = ' ' * 4

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_Mpls_LocalBlock_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_Mpls_Impl(SegmentRouting_Mpls):
    class Yangify(SegmentRouting_Mpls.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_Mpls_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ""
            self.submode_indent = ' ' * 2
            self.cli_fmt = "segment-routing"

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

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl, self).__init__(*args, **kwargs)
    metric = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Metric_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Impl, self).__init__(*args, **kwargs)
    dynamic = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Dynamic_Dynamic_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl.Yangify, self).__init__(*args, **kwargs)


    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl, self).__init__(*args, **kwargs)
    segment_list = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_PathChoice_Explicit_Explicit_Impl

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
            self.indent = ' ' * 6
            self.submode_indent = self.indent + '  '
            self.cli_fmt      = "preference {preference}"
            self.undo_cli_fmt = "no preference {preference}"

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl, self).__init__(*args, **kwargs)
    constraints = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Constraints_Impl

class SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl(SegmentRouting_TrafficEng_Policy_CandidatePaths):
    class Yangify(SegmentRouting_TrafficEng_Policy_CandidatePaths.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent = ' ' * 4
            self.submode_indent = self.indent + '  '
            self.cli_fmt = 'candidate-paths'

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl, self).__init__(*args, **kwargs)
    preference = SegmentRouting_TrafficEng_Policy_CandidatePaths_Preference_Impl

class SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl(SegmentRouting_TrafficEng_Policy_ColorEndpoint):
    class Yangify(SegmentRouting_TrafficEng_Policy_ColorEndpoint.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent = ' ' * 4
            self.submode_indent = self.indent + '  '
            self.cli_fmt = "color {color} endpoint {end_point}"

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl, self).__init__(*args, **kwargs)



class SegmentRouting_TrafficEng_Policy_Impl(SegmentRouting_TrafficEng_Policy):
    class Yangify(SegmentRouting_TrafficEng_Policy.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Policy_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent = ' ' * 2
            self.submode_indent = self.indent + '  '
            self.cli_fmt      = "policy {name}"
            self.undo_cli_fmt = "no policy {name}"

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_Policy_Impl, self).__init__(*args, **kwargs)
    binding_sid = SegmentRouting_TrafficEng_Policy_BindingSid_Impl
    candidate_paths = SegmentRouting_TrafficEng_Policy_CandidatePaths_Impl
    color_endpoint = SegmentRouting_TrafficEng_Policy_ColorEndpoint_Impl

class SegmentRouting_TrafficEng_SegmentList_Index_Impl(SegmentRouting_TrafficEng_SegmentList_Index):
    class Yangify(SegmentRouting_TrafficEng_SegmentList_Index.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_Index_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 4
            self.submode_indent = ' ' * 6
            self.cli_fmt      = "index6 {index} mpls {key} {value}"
            self.undo_cli_fmt = "no index {index} mpls {key} {value}"

        def extract_cli_data2(self, cli_data):
            print(cli_data)
            if 'mpls' in cli_data:
                for key in ['label', 'adjacency', 'prefix']:
                    if key in cli_data['mpls']:
                        cli_data['key'] = key
                        cli_data['value'] = cli_data['mpls'][key]
                        return

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_Index_Impl, self).__init__(*args, **kwargs)

class SegmentRouting_TrafficEng_SegmentList_Impl(SegmentRouting_TrafficEng_SegmentList):
    class Yangify(SegmentRouting_TrafficEng_SegmentList.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_SegmentList_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ' ' * 2
            self.submode_indent = ' ' * 4
            self.cli_fmt      = "segment-list name {name}"
            self.undo_cli_fmt = "no segment-list name {name}"

    def __init__(self, *args, **kwargs):
        super(SegmentRouting_TrafficEng_SegmentList_Impl, self).__init__(*args, **kwargs)
    index = SegmentRouting_TrafficEng_SegmentList_Index_Impl

class SegmentRouting_TrafficEng_Impl(SegmentRouting_TrafficEng):
    class Yangify(SegmentRouting_TrafficEng.Yangify):
        def __init__(self, *args, **kwargs):
            super(SegmentRouting_TrafficEng_Impl.Yangify, self).__init__(*args, **kwargs)
            self.indent     = ''
            self.submode_indent = ' ' * 2
            self.cli_fmt = "segment-routing traffic-eng"

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