import unittest

from biolinkml.utils.schemaloader import SchemaLoader

from testlink import TESTLINK_MODEL_YAML


class testlinkModelTestCase(unittest.TestCase):
    def test_testlink_model(self):
        """ Make sure the testlink model is valid """
        schema = SchemaLoader(TESTLINK_MODEL_YAML)
        errors = []
        try:
            schema.resolve()
        except ValueError as e:
            errors.append(str(e))
        if not errors:
            errors = schema.synopsis.errors()
        self.assertEqual([], errors, "testlink-model.yaml - errors detected")


if __name__ == '__main__':
    unittest.main()
