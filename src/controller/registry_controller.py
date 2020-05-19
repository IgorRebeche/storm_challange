from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES


class RegistryContoller:
    def __init__(self, registry_repo: RegistryRepo, schemaRepo: SchemaRepo):
        self.registry_repo = registry_repo
        self.schemaRepo = schemaRepo

    def listRegistries(self):
        return [registry.toTuple() for registry in self.registry_repo.registries]

    def activeRegistries(self):
        registry: Registry
        schema: list[Schema]
        activeRegistries = []

        for entity in self.registry_repo.get_entities():
            for attribute in self.registry_repo.get_entity_atributes(entity):
                cardinality = self.schemaRepo.findCardinalityByAttributeName(attribute)[
                    0]

                if cardinality == SCHEMA_CARDINALITIES.MANY_TO_MANY:
                    pass

                if cardinality == SCHEMA_CARDINALITIES.ONE_TO_MANY:
                    registries = self.registry_repo.findByEntityAndAtt(
                        entity, attribute, True)
                    removedRegistries = self.registry_repo.findByEntityAndAtt(
                        entity, attribute, False)
                    filtredRegistries = []
                    if (len(removedRegistries)):
                        filtredRegistries = [
                            registry.toTuple() for registry in registries
                            for removedRegistry in removedRegistries
                            if removedRegistry.value != registry.value
                        ]
                    else:
                        filtredRegistries = [registry.toTuple()
                                             for registry in registries]

                    activeRegistries.extend(filtredRegistries)

                if cardinality == SCHEMA_CARDINALITIES.ONE_TO_ONE:
                    lastRegistry = self.registry_repo.findLastByEntityAndAtt(
                        entity, attribute, True)
                    lastRemovedRegistry = self.registry_repo.findLastByEntityAndAtt(
                        entity, attribute, False)

                    if not lastRemovedRegistry or not lastRegistry.value == lastRemovedRegistry.value:
                        activeRegistries.append(lastRegistry.toTuple())

        print(activeRegistries)
