from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES

from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo

from controller.registry_controller import RegistryContoller

def main():
    facts = [
        Registry('Teste', 'telefone', '2199088-1111', False),
        Registry('Teste', 'telefone', '21231231-1111', True),
        Registry('Teste', 'telefone', '12345-1111', True),
        Registry('Teste1', 'telefone', '2199088-11111', True),
        Registry('Teste', 'endereco', 'Rua Tirol', True),
        Registry('Teste', 'endereco', 'Rua Tirol', False),
        Registry('Teste', 'endereco', 'Rua Araguaia', True)
    ]
    registriesRepo = RegistryRepo(facts)

    schemas = [
        Schema('telefone', SCHEMA_CARDINALITIES.ONE_TO_MANY),
        Schema('endereco', SCHEMA_CARDINALITIES.ONE_TO_ONE)
    ]
    
    schemaRepo = SchemaRepo(schemas)

    create_registry = RegistryContoller(registriesRepo, schemaRepo)
    
    print(create_registry.activeRegistries())

main()