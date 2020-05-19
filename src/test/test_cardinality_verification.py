import unittest
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES
from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from helpers.cardinality_verification import verify_one_to_many_cardi, verify_one_to_one_cardi


class test_cardinality_verification(unittest.TestCase):

    def setUp(self):

        self.schemas = [
            Schema('telefone', SCHEMA_CARDINALITIES.ONE_TO_MANY),
            Schema('endereco', SCHEMA_CARDINALITIES.ONE_TO_ONE)
        ]

        self.schemaRepo = SchemaRepo(self.schemas)

    def test_one_to_one_should_return_last_active_value(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'endereco', 'Rua Tirol', True),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registriesRepo = RegistryRepo(facts)

        lastRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste1', attribute='endereco', isAdded=True
        )

        lastRemovedRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste1', attribute='endereco', isAdded=False
        )

        filtredRegistry = verify_one_to_one_cardi(
            lastRegistry=lastRegistry, lastRemovedRegistry=lastRemovedRegistry
        )

        self.assertEqual(filtredRegistry, lastRegistry.toTuple())

    def test_one_to_one_with_one_removal_should_return_last_active_value(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'endereco', 'Rua Tirol', False),
            Registry('Teste', 'endereco', 'Rua da Noite', True),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registriesRepo = RegistryRepo(facts)

        lastRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste', attribute='endereco', isAdded=True
        )

        lastRemovedRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste', attribute='endereco', isAdded=False
        )

        filtredRegistry = verify_one_to_one_cardi(
            lastRegistry=lastRegistry, lastRemovedRegistry=lastRemovedRegistry
        )

        self.assertEqual(filtredRegistry, lastRegistry.toTuple())

    def test_one_to_one_with_one_assignment_and_one_removal_should_return_empty(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'endereco', 'Rua da Noite', True),
            Registry('Teste', 'endereco', 'Rua Tirol', True),
            Registry('Teste', 'endereco', 'Rua Tirol', False),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registriesRepo = RegistryRepo(facts)

        lastRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste', attribute='endereco', isAdded=True
        )

        lastRemovedRegistry = registriesRepo.findLastByEntityAndAtt(
            entity='Teste', attribute='endereco', isAdded=False
        )

        filtredRegistry = verify_one_to_one_cardi(
            lastRegistry=lastRegistry, lastRemovedRegistry=lastRemovedRegistry
        )
        
        self.assertEqual(filtredRegistry, None)
    
    def test_one_to_many_should_return_active_value(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'endereco', 'Rua Tirol', True),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registryRepo = RegistryRepo(facts)

        resgistries = registryRepo.findByEntityAndAtt(
            entity='Teste1', attribute='telefone', isAdded=True
        )

        removedRegistries = registryRepo.findByEntityAndAtt(
            entity='Teste1', attribute='telefone', isAdded=False
        )

        filtredRegistries = verify_one_to_many_cardi(
            registries=resgistries, removedRegistries=removedRegistries
        )

        expectedList = [registry.toTuple() for registry in resgistries]
        actualList = filtredRegistries

        self.assertEqual(actualList, expectedList)

    def test_one_to_many_with_one_removal(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '123456-11111', True),
            Registry('Teste1', 'telefone', '95478-11111', True),
            Registry('Teste1', 'telefone', '95478-11111', False),
            Registry('Teste', 'endereco', 'Rua Tirol', False),
            Registry('Teste', 'endereco', 'Rua da Noite', True),
            Registry('Teste', 'telefone', '2199088-1111', False),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registryRepo = RegistryRepo(facts)

        resgistries = registryRepo.findByEntityAndAtt(
            entity='Teste1', attribute='telefone', isAdded=True
        )

        removedRegistries = registryRepo.findByEntityAndAtt(
            entity='Teste1', attribute='telefone', isAdded=False
        )

        filtredRegistries = verify_one_to_many_cardi(
            registries=resgistries, removedRegistries=removedRegistries
        )

        expectedList = [
            Registry('Teste1', 'telefone', '123456-11111', True)
        ]
        actualList = filtredRegistries

        self.assertEqual(actualList, [registry.toTuple() for registry in expectedList])

    def test_one_to_many_with_one_assignment_and_one_removal_should_return_empty(self):
        facts = [
            Registry('Teste', 'telefone', '2199088-1111', True),
            Registry('Teste1', 'telefone', '2199088-11111', True),
            Registry('Teste', 'telefone', '2199088-1111', False),
            Registry('Teste', 'endereco', 'Rua da Noite', True),
            Registry('Teste', 'endereco', 'Rua Tirol', True),
            Registry('Teste', 'endereco', 'Rua Tirol', False),
            Registry('Teste1', 'endereco', 'Rua Araguaia', True)
        ]

        registryRepo = RegistryRepo(facts)

        resgistries = registryRepo.findByEntityAndAtt(
            entity='Teste', attribute='telefone', isAdded=True
        )

        removedRegistries = registryRepo.findByEntityAndAtt(
            entity='Teste', attribute='telefone', isAdded=False
        )

        filtredRegistries = verify_one_to_many_cardi(
            registries=resgistries, removedRegistries=removedRegistries
        )

        expectedList = []
        actualList = filtredRegistries

        self.assertEqual(actualList, expectedList)
