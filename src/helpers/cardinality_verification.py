def verify_one_to_many_cardi(registries, removedRegistries):
        if (len(removedRegistries)):
            return [
                registry.to_tuple() for registry in registries
                for removedRegistry in removedRegistries
                if removedRegistry.value != registry.value
            ]
        return [registry.to_tuple() for registry in registries]

def verify_one_to_one_cardi(lastRegistry, lastRemovedRegistry):
    if not lastRemovedRegistry:
        return lastRegistry.to_tuple()

    if lastRegistry and not lastRegistry.value == lastRemovedRegistry.value:
        return lastRegistry.to_tuple()
    
    return None
