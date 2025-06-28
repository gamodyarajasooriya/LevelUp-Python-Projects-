def index_all(obj, item):
    result = []

    def search(sub_obj, path):
        if isinstance(sub_obj, list):
            for i, element in enumerate(sub_obj):
                search(element, path + [i])
        else:
            if sub_obj == item:
                result.append(path)

    search(obj, [])
    return result
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

print(index_all(example, 1))