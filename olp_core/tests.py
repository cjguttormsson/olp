import unittest
import OLPManager
from OLPExceptions import *

class OLPInputTest(unittest.TestCase):
    def test_definition_failure(self):
        with self.assertRaises(OLPNeedOverrideToDefine):
            OLPManager.define("re = 2")

        with self.assertRaises(OLPInvalidDefinition):
            OLPManager.define("2 + 3")

        with self.assertRaises(OLPInvalidDefinition):
            OLPManager.define("\" 2 + 3") #This one is silly, but I want to make sure strings aren't escaped

    def test_add_module_failure(self):
        pass

    def test_reference_defintion_failure(self):
        pass

    def test_reference_module_failure(self):
        pass

    def test_definition_success(self):
        pass

    def test_add_module_success(self):
        pass

    def test_reference_definition_success(self):
        pass

    def test_reference_module_success(self):
        pass
    
    def test_stdin_pipe_failure(self):
        pass

    def test_stdin_pipe_success(self):
        pass

if __name__ == "__main__":
    unittest.main()
