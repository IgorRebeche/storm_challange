from models.schema import Schema

class SchemaRepo:
    def __init__(self, schemas :list):
        self.__schemas = schemas

    @property
    def schemas(self):
        return self.__schemas

    @schemas.setter
    def schemas(self, schemas):
        self.__schemas = schemas

    def findCardinalityByAttributeName(self, attribute):
        schema: Schema
        return [schema.cardinality for schema in self.__schemas if schema.attribute == attribute]

    
    def toTuple(self):
        return [schema.toTuple() for schema in self.__schemas]