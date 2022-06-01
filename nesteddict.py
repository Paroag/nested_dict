import copy


def merge_nested(dic1, dic2):
    dic = copy.deepcopy(dic1)
    for key, value in dic2.items():
        if key not in dic:
            dic[key] = value
        elif not isinstance(value, dict) and not isinstance(dic[key], dict):
            dic[key] = value
        elif isinstance(value, dict) and isinstance(dic[key], dict):
            dic[key] = merge_nested(dic[key], value)
        else:
            raise ValueError
    return dic


def is_included(dic1, dic2):
    for key, value in dic1.items():
        if key not in dic2:
            return False
        if not isinstance(value, dict):
            if value != dic2[key]:
                return False
        else:
            if not is_included(value, dic2[key]):
                return False
    return True