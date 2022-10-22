# Return False if there is no such keys and True if there is
def keys_in(body: dict, keys: list=[]) -> bool:
    for key in keys:
        if not key in body.keys():
            return False
    return True