from models.registry import Registry

class RegistryRepo:
    def __init__(self, registries: list):
        self.__registries = registries

    @property
    def registries(self):
        return self.__registries

    @registries.setter
    def registries(self, registries):
        self.__registries = registries

    def get_entities(self):
        registry :Registry
        allRegistriesEntities = [registry.entity for registry in self.__registries]
        return set(allRegistriesEntities)
    
    def get_entity_atributes(self, entity):
        registry :Registry
        attrsByEntity = [registry.attribute for registry in self.__registries if registry.entity == entity ]
        return set(attrsByEntity)

    def find_by_entity_and_att(self, entity, attribute, isAdded):
        registry: Registry
        return [
            registry for registry in self.__registries
            if registry.entity == entity
            and registry.attribute == attribute
            and registry.isAdded == isAdded
        ]

    def find_last_by_entity_and_att(self, entity, attribute, isAdded):
        registry: Registry
        foundRegistries = [
            registry for registry in self.__registries
            if registry.entity == entity
            and registry.attribute == attribute
            and registry.isAdded == isAdded
        ]
        if len(foundRegistries):
            return foundRegistries[len(foundRegistries) - 1]