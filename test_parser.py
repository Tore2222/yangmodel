#!/usr/bin/env python3

from yangify import parser
from yangify.parser.text_tree import parse_indented_config
from yangson.datamodel import DataModel
from yangson.exceptions import SchemaError
from yangson.exceptions import SemanticError
import json
from vht.impl.parsers.VHT_bgp_cfg.bgp import Bgp_Impl
from vht.impl.parsers.VHT_bgp_cfg.router import Router_Impl as BGPRouter_Impl
from vht.impl.parsers.VHT_ip_cfg.ip import Ip_Impl
from vht.impl.parsers.VHT_interface_cfg.interfaces import Interfaces_Impl
from vht.impl.parsers.VHT_ospf_cfg.router import Router_Impl as OSPFRouter_Impl
from vht.impl.parsers.VHT_segment_routing.segment_routing import SegmentRouting_Impl
from vht.helper import get_pretty_xml
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET

def pretty_print_xml(elem, level=0):
    """Custom function to pretty print XML elements."""
    indent = "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = "\n" + (level + 1) * indent
        if not elem.tail or not elem.tail.strip():
            elem.tail = "\n" + level * indent
        for child in elem:
            pretty_print_xml(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = "\n" + level * indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = "\n" + level * indent

class IOSParser(parser.RootParser):
    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native = {}
            self.root_native["show run"] = parse_indented_config(self.native["show run"].splitlines())

            self.native = self.root_native

    bgp = Bgp_Impl
    ip = Ip_Impl
    router_ospf = OSPFRouter_Impl
    router_bgp = BGPRouter_Impl
    segment_routing = SegmentRouting_Impl
    interfaces = Interfaces_Impl

if __name__ == '__main__':
    dm = DataModel.from_file('vht/yang/yang-library.json',["vht/yang/modules", "../test-yangson/yangson/yang-modules/ietf"])

    with open("test/data/test_giang_parser.txt", "r") as f:
        config = f.read()

    data = { "show run" : config }
    def test_1():
        p = IOSParser(dm, native=data)
        try:
            result = p.process(validate=True)
        except Exception as e:
            print(f"error: {e}")
            raise e

        #elm = result.to_xml()

        # Convert result to a dictionary (adjust based on the structure of `result`)
        result_dict = result.raw_value()

        # Convert dictionary to XML using dicttoxml
        xml_bytes = dicttoxml(result_dict, root=False, attr_type=False)
        xml_str = xml_bytes.decode('utf-8')

        # Parse XML string to Element object
        xml_root = ET.fromstring(xml_str)

        # Print JSON representation
        print("candidate", json.dumps(result_dict, indent=4))

        # Print pretty XML
        #pretty_xml = ET.tostring(xml_root, encoding='unicode', method='xml')

        # Assuming get_pretty_xml accepts a string
        #print(get_pretty_xml(pretty_xml))
        # Call the function to pretty print XML
        pretty_print_xml(xml_root)
        print(ET.tostring(xml_root, encoding="unicode"))

        #print(json.dumps(result.raw_value(), indent=4))
        #print(get_pretty_xml(elm))

    test_1()
