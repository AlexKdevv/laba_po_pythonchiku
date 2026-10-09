types = (str, list, tuple, set, frozenset, dict)
def pustoe(x):
    return isinstance(x, types) and len(x) == 0
def clean(obj):
    if isinstance(obj, dict):
        cleaned = {k: clean(v) for k, v in obj.items()}
        return {k: v for k, v in cleaned.items() if not pustoe(v)}
    if isinstance(obj, (list, tuple, set, frozenset)):
        cleaned = (clean(x) for x in obj)
        return type(obj)(x for x in cleaned if not pustoe(x))
    return obj
res = [ 0, "", [], [[], {}, 0], {"z": [3], "v": {"o": ""}, "Goida": 100}, {(), 1}, ((1, "")), ]
print(clean(res))