class Registry:
    def __init__(self, entity, attribute, value, isAdded):
        self.entity = entity
        self.attribute = attribute
        self.value = value
        self.isAdded = isAdded
        
    def to_tuple(self):
        return (self.entity, self.attribute, self.value, self.isAdded)