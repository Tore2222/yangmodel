#!/usr/bin/env python3

from yangson import DataModel
from yangson import instance
from yangson import schemanode
from yangson.exceptions import NonexistentInstance


from yangify import translator
from yangify.translator.config_tree import ConfigTree
from vht.impl.translators.VHT_ip_cfg.ip import Ip_Impl
from vht.impl.translators.VHT_ospf_cfg.router import Router_Impl
from vht.impl.translators.VHT_segment_routing.segment_routing import *
import json
import copy




class RootTranslator2(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    def __init__(self, dm, candidate, running = None, replace = False, extra = None) -> None:
        n = dm.from_xml(candidate)
        o = dm.from_xml(running) if running is not None else None
        super().__init__(
            result=None,
            root_result=None,
            path=instance.InstanceRoute(),
            dm=dm,
            schema=dm.schema,
            keys={},
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
    segment_routing = SegmentRouting_Impl


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

if __name__ == '__main__':
    dm = DataModel.from_file('vht/yang/yang-library.json',["vht/yang/modules", "../test-yangson/yangson/yang-modules/ietf"])
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


    with open("test/data/translator_01.json", "r") as f:
        candidate = json.load(f)

    print(candidate)

    print("start1\n\n")

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
        print(p.process())
        return p.process()

    def test_4():
        from xml.etree import cElementTree as ElementTree
        import xml.etree.ElementTree as ET

        tree = ET.parse('test/data/config1.xml')
        candidate = tree.getroot()
        pprint(candidate)

        p = RootTranslator2(dm, candidate=candidate)
        return p.process()

    result = test_4()
    print(result)

