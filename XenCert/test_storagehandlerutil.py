import sys
sys.path.append("/local/home/Work/XS_STO/Creedence-Storage/Fresh/build.hg/myrepos/sm/drivers")
import unittest

class fake_stub(object):
    MSIZE = object()

class TestExtractXML(unittest.TestCase):

    def setUp(self):
        self.original_modules = ["scsiutil", "util", "lvutil", "vhdutil", "lvhdutil", "iscsilib", "mpath_cli", "mpath_dmp"]
        self.module_dict = {}

        for mod in self.original_modules:
            self.module_dict[mod] = sys.modules.get(mod)

        for mod in self.original_modules:
            sys.modules[mod] = fake_stub

    def test_xml_split_by_commas(self):
        import StorageHandlerUtil
        error_string = 'a,b,c,d'
        expected_res = 'd'

        result = StorageHandlerUtil.extract_xml_from_exception(error_string)

        self.assertEqual(expected_res, result)

    def test_xml_xml_tag_recognised(self):
        import StorageHandlerUtil
        error_string = 'a,b,c,d,e'
        expected_res = 'd,e'

        result = StorageHandlerUtil.extract_xml_from_exception(error_string)

        self.assertEqual(expected_res, result)

    def tearDown(self):
        for mod, path in self.module_dict:
            sys.modules[mod] = path

if __name__ == '__main__':
    unittest.main()
