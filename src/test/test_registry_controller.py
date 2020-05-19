import unittest
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES
from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from controller.registry_controller import RegistryContoller


class test_registry_controller(unittest.TestCase):

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

    def test_should_return_empty_resgistry_list(self):
        emptyFacts = []
        emptyRepo = RegistryRepo(emptyFacts)
        registryController = RegistryContoller(
            registry_repo=emptyRepo,
            schemaRepo=self.schemaRepo
        )

        actualList = registryController.list_registries()

        expectedList = []

        self.assertEqual(actualList, expectedList)

    def test_should_return_list_registries(self):
        registryController = RegistryContoller(
            registry_repo=self.registriesRepo,
            schemaRepo=self.schemaRepo
        )

        actualList = registryController.list_registries()

        expectedList = [
            ('Teste', 'telefone', '2199088-1111', False),
            ('Teste', 'telefone', '21231231-1111', True),
            ('Teste', 'telefone', '12345-1111', True),
            ('Teste1', 'telefone', '2199088-11111', True),
            ('Teste', 'endereco', 'Rua Tirol', True),
            ('Teste', 'endereco', 'Rua Tirol', False),
            ('Teste', 'endereco', 'Rua Araguaia', True)
        ]

        self.assertEqual(actualList, expectedList)
