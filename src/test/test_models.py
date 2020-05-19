import unittest

from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES

class test_models(unittest.TestCase):

    def test_should_create_registry_instance(self):
        registry = Registry('EntityName', 'Attribute', 'Value', True)
        self.assertEqual(registry.entity, 'EntityName')
        self.assertEqual(registry.attribute, 'Attribute')
        self.assertEqual(registry.value, 'Value')
        self.assertEqual(registry.isAdded, True)
    
    def test_should_create_schema_instance(self):
        schema = Schema('Attribute', SCHEMA_CARDINALITIES.ONE_TO_MANY)
        self.assertEqual(schema.attribute, 'Attribute')
        self.assertEqual(schema.cardi, SCHEMA_CARDINALITIES.ONE_TO_MANY)
    