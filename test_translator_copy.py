#!/usr/bin/env python3

from yangson import DataModel
from yangson import instance
from yangson import schemanode
#from yangson.exceptions import NonexistentInstance, RawTypeError, RawMemberError


from yangify import translator
from yangify.translator.config_tree import ConfigTree
from vht.impl.translators.VHT_ip_cfg.ip import Ip_Impl
from vht.impl.translators.VHT_ospf_cfg.router import Router_Impl
from vht.impl.translators.VHT_segment_routing.segment_routing import *
from vht.impl.translators import XMLRootTranslator
import json
#import copy
import xmltodict

def xml_to_json(xml_str):
    if xml_str is None:
        return None
    try:
        # parse the xml string
        xml_dict = xmltodict.parse(xml_str, force_list={'policy', 'prefixes', 'segment-list', 'preference', 'segment-entry', 'ip-route-static', 'vrf'})
        # ensure the specific "a" node is a list
        #if isinstance(xml_dict['VHT-ip-cfg:ip']['route']['ip-route-static'], dict):
            #xml_dict['VHT-ip-cfg:ip']['route']['ip-route-static'] = [xml_dict['VHT-ip-cfg:ip']['route']['ip-route-static']]
        #if isinstance(xml_dict['VHT-ip-cfg:ip']['route']['vrf']['ip-route-static'], dict):
            #xml_dict['VHT-ip-cfg:ip']['route']['vrf']['ip-route-static'] = [xml_dict['VHT-ip-cfg:ip']['route']['vrf']['ip-route-static']]
        #if isinstance(xml_dict['VHT-ip-cfg:ip']['route']['vrf'], dict):
            #xml_dict['VHT-ip-cfg:ip']['route']['vrf'] = [xml_dict['VHT-ip-cfg:ip']['route']['vrf']]
        json_dict = json.loads(json.dumps(xml_dict))
        return json_dict
    
    except Exception as e:
        print(f"Error converting XML to JSON: {e}")
        return None

class RootTranslator2(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    def __init__(self, dm, candidate, running = None, replace = False, extra = None) -> None:
        print("start2\n\n")

        n = xml_to_json(candidate)
        o = xml_to_json(running) if running is not None else None
        print("Candidate Dict:", json.dumps(n, indent=2))
        print("Running Dict:", json.dumps(o, indent=2))

        if not isinstance(n, dict):
            print("Error: Candidate is not a dictionary")
        if running is not None and not isinstance(o, dict):
            print("Error: Running is not a dictionary")

        super().__init__(
            #result=None,
            #root_result=None,
            #path=instance.InstanceRoute(),
            dm=dm,
            #schema=dm.schema,
            #keys={},
            candidate=n,
            running=o if running is not None else {},
            replace=replace,
            extra=extra or {},
        )

    def __str__(self) -> str:
        return self.__class__.__qualname__

    def process(self) -> Any:
        self.yy.init()
        self._process_container()
        self.yy.post()
        #return self.yy.root_result
        return self.yy.result.to_string()

    def pre_process(self):
        # Call pre_process for nested Translator classes in the correct order
        self.result = self.root_result.new_section("segment-routing")
        self.result.new_section("traffic-eng")
        candidate_paths = SegmentRouting_TrafficEng_Policy_CandidatePaths.Yangify(self)
        candidate_paths.pre_process()
        preference = candidate_paths.preference.Yangify(candidate_paths)
        preference.pre_process()

    def post_process(self):
        # Call post_process for nested Translator classes in the correct order
        candidate_paths = SegmentRouting_TrafficEng_Policy_CandidatePaths.Yangify(self)
        candidate_paths.post_process()
        preference = candidate_paths.preference.Yangify(candidate_paths)
        preference.post_process()


    ip = Ip_Impl
    router = Router_Impl
    segment_routing = SegmentRouting_Impl

class RootTranslator(translator.RootTranslator):
    def __init__(self):
        super().__init__()

    def xml_to_json(self, xml_data):
        print("Converting XML to JSON...")
        json_data = xmltodict.parse(xml_data, dict_constructor=OrderedDict)
        return json.dumps(json_data, indent=4)

    def json_to_txt(self, json_data):
        print("Converting JSON to TXT...")
        data = json.loads(json_data, object_pairs_hook=OrderedDict)
        txt_lines = []
        
        def process_dict(d, indent=0):
            for key, value in d.items():
                if isinstance(value, dict):
                    txt_lines.append(" " * indent + f"{key}:")
                    process_dict(value, indent + 2)
                else:
                    txt_lines.append(" " * indent + f"{key}: {value}")

        process_dict(data)
        return "\n.join(txt_lines)"

    def process(self, xml_data):
        json_data = self.xml_to_json(xml_data)
        txt_data = self.json_to_txt(json_data)
        return txt_data

class IOSTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    ip = Ip_Impl
    router = Router_Impl
    segment_routing = SegmentRouting_Impl

'''class XMLRootTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):   
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    def __init__(self, dm, candidate, running = None, replace = False, extra = None) -> None:
        #n = dm.from_xml(candidate)
        #o = dm.from_xml(running) if running else None
        n = xml_to_json(candidate)
        o = xml_to_json(running) if running else None
        super().__init__(
            #result=None,
            #root_result=None,
            #path=instance.InstanceRoute(),
            dm=dm,
            #schema=dm.schema,
            #keys={},
            candidate=n,
            running=o,
            replace=replace,
            extra=extra or {},
        )

    def __str__(self) -> str:
        return self.__class__.__qualname__

    def process(self) -> Any:
        self.yy.init()
        self._process_container()
        self.yy.post()
        return self.yy.root_result

    ip = Ip_Impl
    router = Router_Impl
    segment_routing = SegmentRouting_Impl'''

if __name__ == '__main__':
    dm = DataModel.from_file('vht/yang/yang-library.json',["vht/yang/modules", "../test-yangson/yangson/yang-modules/ietf"])
    #dm = DataModel.from_file('../yang/yang-library.json',["../yang/modules", "../test-yangson/yangson/yang-modules/ietf"])
    print(dm.ascii_tree())
    print("hello\n\n")
    def test_1():
        with open("test/data/test_translator.json", "r") as f:
            data = json.load(f)

        # for cfg in data['test-ip-route-static']:
        #     print(cfg)
        #     p = IOSTranslator(dm, candidate=cfg)
        #     result = p.process()
        #     print(result)

        candidate=data['test-ip-route-static'][1]
        running=data['test-ip-route-static'][0]
        p = IOSTranslator(dm, candidate=candidate, running=running, replace=False)
        result = p.process()
        print(result)
        print("========================================================================")
        candidate=data['test-ip-route-static'][0]
        running=data['test-ip-route-static'][1]
        p = IOSTranslator(dm, candidate=candidate, running=running, replace=False)
        result = p.process()
        print(result)
        print("========================================================================")


    with open("test/data/test_131.json", "r") as f:
        candidate = json.load(f) 

    # print("start1\n\n")

    def test_2():
        p = IOSTranslator(dm, candidate=candidate, replace=False)
        return p.process()

    def test_3():
        running = copy.deepcopy(candidate)
        running.pop('VHT-ospf-cfg:router')
        running['VHT-segment-routing:segment-routing']['traffic-eng']['policy'].pop(0)
        running['VHT-ip-cfg:ip']['route']['ip-route-static'].pop(0)
        running['VHT-ip-cfg:ip']['route']['ip-route-static'][0]['out-if'] = 'ce1'
        p = IOSTranslator(dm, candidate=candidate, running=running, replace=False)
        res = p.process()
        print(F"candidate to running:\n{res}\n\n")

        p = IOSTranslator(dm, candidate=running, running=candidate, replace=False)
        res = p.process()
        print(F"running to candidate:\n{res}\n\n")


    def test_2():
        p = IOSTranslator(dm, candidate=candidate, replace=False)
        print("giang\n\n")
        print("candidate========================================================================")
        print(candidate)
        print("========================================================================")
        return p.process()

    def test_4():
        #from xml.etree import cElementTree as ElementTree
        #import xml.etree.ElementTree as ET

        #tree = ET.parse('test/data/config1.xml')
        #candidate1 = tree.getroot()
        #print ("candidate1\n")
        #pprint(candidate1) 

        with open('test/data/before.xml', 'r') as file:
            before_data = file.read()
        with open('test/data/after.xml', 'r') as file:
            after_data = file.read()

        #with open('test/data/config1.xml', 'r') as file:
            #xml_data = file.read()
        #xml_data = json.loads(json_data)
        
        #print (xml_data)

        #translator = RootTranslator2(dm, candidate=xml_data)
        translator = XMLRootTranslator(dm, candidate=after_data, running=before_data)
        return translator.process()

    def test_5():
        with open('test/data/config_bgp1.xml', 'r') as file:
            xml_data = file.read()
        translator = RootTranslator2(dm, candidate=xml_data)
        return translator.process()

        
    result = test_5()
    print(result)