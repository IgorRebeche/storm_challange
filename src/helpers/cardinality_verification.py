def verify_one_to_many_cardi(registries, removedRegistries):
        if (len(removedRegistries)):
            return [
                registry.toTuple() for registry in registries
                for removedRegistry in removedRegistries
                if removedRegistry.value != registry.value
            ]
        return [registry.toTuple() for registry in registries]

def verify_one_to_one_cardi(lastRegistry, lastRemovedRegistry):
    if not lastRemovedRegistry:
        return lastRegistry.toTuple()

    if lastRegistry and not lastRegistry.value == lastRemovedRegistry.value:
        return lastRegistry.toTuple()
    
    return None
