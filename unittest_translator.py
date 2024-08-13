from yangson import DataModel
from yangson import instance
from yangson import schemanode
from yangson.exceptions import NonexistentInstance


from yangify import translator
from yangify.translator.config_tree import ConfigTree
from vht.impl.translators.VHT_ip_cfg.ip import Ip_Impl
from vht.impl.translators.VHT_ospf_cfg.router import Router_Impl
from vht.impl.translators.VHT_segment_routing.segment_routing import *
from functools import wraps
import json
import copy
import unittest
import logging

@wraps
def logging_fn(func):
    def wrapper(*args, **kwargs):
        logging.info("linh %s", func.__name__)
        logging.info("Starting testcase %s" , func.__name__)
        result = func(*args, **kwargs)
        logging.info("Finishing testcase %s ", func.__name__)
        return result
    return wrapper

class IOSTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result
            self.maxDiff = None

        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    ip = Ip_Impl
    router = Router_Impl
    segment_routing = SegmentRouting_Impl


class Test(unittest.TestCase):

   # result: any()

    dm = DataModel.from_file('vht/yang/yang-library.json',
                             ["vht/yang/modules", "../test-yangson/yangson/yang-modules/ietf"])

    with open("test/data/test_sr.json", "r") as f:
        data = json.load(f)

    with open("test/data/test_sr.txt", "r") as f:
        expected = f.read()
        expected = expected.split("\n***\n")

    def assertCompareConfig(self, candidate, running, expected):
        p = IOSTranslator(self.dm, candidate = candidate, running = running, replace = False)
        try:
            self.result = p.process()
        except Exception as e:
            logging.error("Error occurred: %s", e)
            raise e
        logging.info(">>>>>RESULT<<<<<")
        logging.info(self.result)
        logging.info(">>>>>RESULT<<<<<")
        self.assertEqual(self.result, expected)

    @logging_fn
    def test_trans_1(self):
        candidate = self.data['test-segment-routing'][0]
        expected = self.expected[0]
        self.maxDiff = None
        self.assertCompareConfig(candidate, None, expected)

    @logging_fn
    def test_trans_2(self):
        candidate = self.data['test-segment-routing'][1]
        expected = self.expected[1]
        self.maxDiff = None
        self.assertCompareConfig(candidate, None, expected)

    @logging_fn
    def test_trans_3(self):
        candidate = self.data['test-segment-routing'][1]
        running = self.data['test-segment-routing'][0]
        expected = self.expected[2]
        self.maxDiff = None
        self.assertCompareConfig(candidate, running, expected)

    @logging_fn
    def test_trans_4(self):
        candidate = self.data['test-segment-routing'][0]
        running = self.data['test-segment-routing'][1]
        expected = self.expected[3]
        self.maxDiff = None
        self.assertCompareConfig(candidate, running, expected)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

    #python3 -m unittest -v unittest_translator.py
