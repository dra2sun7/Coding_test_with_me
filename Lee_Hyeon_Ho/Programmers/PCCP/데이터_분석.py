def solution(data, ext, val_ext, sort_by):
    answer = []
    a = ["code", "date", "maximum", "remain"]
    
    for x in data:
        if val_ext - x[a.index(ext)] > 0:
            answer.append(x)
            
    return sorted(answer, key = lambda x: x[a.index(sort_by)])
