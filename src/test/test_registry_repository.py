import unittest
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES
from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from controller.registry_controller import RegistryContoller

from repositories.registry_repository import RegistryRepo
from models.registry import Registry


class test_registry_repository(unittest.TestCase):

    def setUp(self):
        self.facts = [
            Registry('Teste', 'telefone', '2199088-1111', False),
            Registry('Teste', 'telefone', '21231231-1111', True),
            Registry('Teste', 'telefone', '12345-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'endereco', 'Rua Tirol', True),
            Registry('Teste', 'endereco', 'Rua Tirol', False),
            Registry('Teste', 'endereco', 'Rua Araguaia', True)
        ]
        self.registriesRepo = RegistryRepo(self.facts)

        self.schemas = [
            Schema('telefone', SCHEMA_CARDINALITIES.ONE_TO_MANY),
            Schema('endereco', SCHEMA_CARDINALITIES.ONE_TO_ONE)
        ]

        self.schemaRepo = SchemaRepo(self.schemas)

    def test_should_get_entities(self):
        actualList = self.registriesRepo.get_entities()
        expectedList = {'Teste1', 'Teste'}

        self.assertEqual(actualList, expectedList)

    def test_should_get_entity_atributes(self):
        actualList = self.registriesRepo.get_entity_atributes('Teste')

        expectedList = {'telefone', 'endereco'}

        self.assertEqual(actualList, expectedList)

    def test_should_find_by_entity_and_att(self):
        actualList = self.registriesRepo.find_by_entity_and_att(
            'Teste', 'telefone', True)

        expectedList = [
            ('Teste', 'telefone', '21231231-1111', True),
            ('Teste', 'telefone', '12345-1111', True)
        ]

        self.assertEqual([registry.to_tuple() for registry in actualList], expectedList)

    def test_should_find_last_by_entity_and_att(self):
        actualRegistry = self.registriesRepo.find_last_by_entity_and_att(
            'Teste', 'telefone', True)

        expectedRegistry = ('Teste', 'telefone', '12345-1111', True)

        self.assertEqual(actualRegistry.to_tuple(), expectedRegistry)
