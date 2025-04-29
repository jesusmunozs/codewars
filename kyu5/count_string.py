def count(s):
    dic = {}
    if s == "":
        return {}
    else:
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic.setdefault(i, 1)
    return dic
print(count("ava"))