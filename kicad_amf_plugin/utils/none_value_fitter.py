def none_value_fitter(fn):
    def wrapper(*args, **kwargs):
        map : 'dict' = fn(*args, **kwargs)
        newDict = dict(filter(lambda elem: elem[1] is not None, map.items()))           
        return  newDict
    return wrapper
