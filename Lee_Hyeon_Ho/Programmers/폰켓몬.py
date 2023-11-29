def solution(nums):
    answer = 0
    dic = {}
    for x in nums:
        dic[hash(x)] = x
    if len(dic) < len(nums)//2:
        return len(dic)
    return len(nums)//2