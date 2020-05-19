class SCHEMA_CARDINALITIES(enumerate) :
    ONE_TO_ONE = 'ONE_TO_ONE'
    MANY_TO_MANY = 'MANY_TO_MANY'
    ONE_TO_MANY = 'ONE_TO_MANY'

class Schema:
    def __init__(self, attribute, cardinality : SCHEMA_CARDINALITIES):
        self.attribute = attribute
        self.cardinality = cardinality
        self.__CARDINALITY = 'cardinality'

    def toTuple(self):
        return (self.entity, self.__CARDINALITY, self.cardinality)