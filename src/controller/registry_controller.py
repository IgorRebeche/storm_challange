from repositories.registry_repository import RegistryRepo
from repositories.schema_repository import SchemaRepo
from models.registry import Registry
from models.schema import Schema, SCHEMA_CARDINALITIES

from helpers.cardinality_verification import verify_one_to_many_cardi, verify_one_to_one_cardi


class RegistryContoller:
    def __init__(self, registry_repo: RegistryRepo, schemaRepo: SchemaRepo):
        self.registry_repo = registry_repo
        self.schemaRepo = schemaRepo

    def list_registries(self):
        return [registry.to_tuple() for registry in self.registry_repo.registries]

    def active_registries(self):
        registry: Registry
        schema: list[Schema]
        active_registries = []

        for entity in self.registry_repo.get_entities():
            for attribute in self.registry_repo.get_entity_atributes(entity):
                cardi = self.schemaRepo.findcardiByAttributeName(attribute)[0]

                if cardi == SCHEMA_CARDINALITIES.ONE_TO_MANY:
                    registries = self.registry_repo.find_by_entity_and_att(
                        entity, attribute, True)

                    removedRegistries = self.registry_repo.find_by_entity_and_att(
                        entity, attribute, False)

                    filtredRegistries = verify_one_to_many_cardi(
                        registries, removedRegistries)

                    if(len(filtredRegistries)):
                        active_registries.extend(filtredRegistries)

                if cardi == SCHEMA_CARDINALITIES.ONE_TO_ONE:
                    lastRegistry = self.registry_repo.find_last_by_entity_and_att(
                        entity, attribute, True)

                    lastRemovedRegistry = self.registry_repo.find_last_by_entity_and_att(
                        entity, attribute, False)

                    filtredRegistry = verify_one_to_one_cardi(
                        lastRegistry, lastRemovedRegistry)

                    if filtredRegistry:
                        active_registries.append(filtredRegistry)

        return active_registries