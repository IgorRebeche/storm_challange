class SCHEMA_CARDINALITIES(enumerate) :
    ONE_TO_ONE = 'ONE_TO_ONE'
    ONE_TO_MANY = 'ONE_TO_MANY'

class Schema:
    def __init__(self, attribute, cardi : SCHEMA_CARDINALITIES):
        self.attribute = attribute
        self.cardi = cardi
        self.__CARDINALITY = 'cardinality'

    def to_tuple(self):
        return (self.entity, self.__CARDINALITY, self.cardinality)