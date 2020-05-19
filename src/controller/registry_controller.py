from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES

from helpers.cardinality_verification import verify_one_to_many_cardi, verify_one_to_one_cardi


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
                cardi = self.schemaRepo.findcardiByAttributeName(attribute)[0]

                if cardi == SCHEMA_CARDINALITIES.ONE_TO_MANY:
                    registries = self.registry_repo.findByEntityAndAtt(
                        entity, attribute, True)

                    removedRegistries = self.registry_repo.findByEntityAndAtt(
                        entity, attribute, False)

                    filtredRegistries = verify_one_to_many_cardi(
                        registries, removedRegistries)

                    if(len(filtredRegistries)):
                        activeRegistries.extend(filtredRegistries)

                if cardi == SCHEMA_CARDINALITIES.ONE_TO_ONE:
                    lastRegistry = self.registry_repo.findLastByEntityAndAtt(
                        entity, attribute, True)

                    lastRemovedRegistry = self.registry_repo.findLastByEntityAndAtt(
                        entity, attribute, False)

                    filtredRegistry = verify_one_to_one_cardi(
                        lastRegistry, lastRemovedRegistry)

                    if filtredRegistry:
                        activeRegistries.append(filtredRegistry)

        return activeRegistries