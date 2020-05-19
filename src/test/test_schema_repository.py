import unittest

from models.schema import Schema, SCHEMA_CARDINALITIES
from repositories.schema_repository import SchemaRepo

class test_schema_repository(unittest.TestCase):

    def test_should_findcardiByAttributeName(self):
        schemas = [
            Schema('telefone', SCHEMA_CARDINALITIES.ONE_TO_MANY),
            Schema('endereco', SCHEMA_CARDINALITIES.ONE_TO_ONE)
        ]

        schemaRepo = SchemaRepo(schemas)

        actualSchema = schemaRepo.findcardiByAttributeName('telefone')
        expectedCardinality = SCHEMA_CARDINALITIES.ONE_TO_MANY
        self.assertEqual(actualSchema[0], expectedCardinality)
    