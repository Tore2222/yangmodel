from yangify import translator
from yangify.translator import Translator, TranslatorData
from yangify.translator.config_tree import ConfigTree
from yangson import instance
from yangson import DataModel
from yangson import schemanode

from vht.impl.translators.VHT_ip_cfg.ip import Ip_Impl
from vht.impl.translators.VHT_ospf_cfg.router import Router_Impl
from vht.impl.translators.VHT_segment_routing.segment_routing import *
import json
import xmltodict

def xml_to_json(xml_str):
    if xml_str is None:
        return None
    try:
        # parse the xml string
        xml_dict = xmltodict.parse(xml_str, force_list={'policy', 'prefixes', 'segment-list', 'preference', 'segment-entry'})
        json_dict = json.loads(json.dumps(xml_dict))
        return json_dict

    except Exception as e:
        print(f"Error converting XML to JSON: {e}")
        return None

class XMLRootTranslator(translator.RootTranslator):
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
        print("Candidate Dict:", json.dumps(n, indent=2))
        print("Running Dict:", json.dumps(o, indent=2))
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
    segment_routing = SegmentRouting_Impl


class JsonRootTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    ip = Ip_Impl
    router = Router_Impl
    segment_routing = SegmentRouting_Impl
