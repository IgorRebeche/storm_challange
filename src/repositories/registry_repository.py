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

    def extendRepo(self, new_registries):
        self.__registries.extend(new_registries)

    def findLastByEntityAndAtt(self, entity, attribute, isAdded):
        registry: Registry
        foundRegistries = [
            registry for registry in self.__registries
            if registry.entity == entity
            and registry.attribute == attribute
            and registry.isAdded == isAdded
        ]
        return foundRegistries[len(foundRegistries) - 1]


    def get_entities(self):
        registry :Registry
        allRegistriesEntities = [registry.entity for registry in self.__registries]
        return set(allRegistriesEntities)
    
    def get_entity_atributes(self, entity):
        registry :Registry
        attrsByEntity = [registry.attribute for registry in self.__registries if registry.entity == entity ]
        return set(attrsByEntity)

    def findByEntityAndAtt(self, entity, attribute, isAdded):
        registry: Registry
        return [
            registry for registry in self.__registries
            if registry.entity == entity
            and registry.attribute == attribute
            and registry.isAdded == isAdded
        ]

    # def findByTuple(self, registryTuple):
    #     registry: Registry
    #     return [
    #         registry for registry in self.__registries
    #         if registry.toTuple() == registryTuple
    #     ]

    # def findLastByTuple(self, registryObj):
    #     registry: Registry
    #     foundRegistries = [registry for registry in self.__registries
    #                        if registry.toTuple() == registryObj.toTuple()]
    #     return foundRegistries[foundRegistries.count-1]

    # def removeRegistry(self, registryObj):
    #     registry: Registry
    #     for index, registry in enumerate(self.__registries):
    #         if registry.toTuple() == registryObj.toTuple():
    #             self.__registries.pop(index)
    #             break

    # def findByAddedStatus(self, entity, attribute, added_status: bool):
    #     registry: Registry
    #     return [registry for registry in self.__registries
    #             if registry.isAdded == added_status]


    # def findByAll(self, entity, attribute, value, isAdded):
    #     pass
