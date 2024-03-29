def solution(phone_book):
    phone_book.sort(key=len)
    arr = [set() for i in range(20)]
    num = []
    for x in phone_book:
        i = len(x)
        arr[i-1].add(x)
        if i not in num:
            num.append(i)
        for j in num:
            if i > j:
                if x[:j] in arr[j-1]:
                    return False
    return True 