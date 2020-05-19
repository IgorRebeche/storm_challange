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

    def findcardiByAttributeName(self, attribute):
        schema: Schema
        return [schema.cardi for schema in self.__schemas if schema.attribute == attribute]

    
    def toTuple(self):
        return [schema.toTuple() for schema in self.__schemas]