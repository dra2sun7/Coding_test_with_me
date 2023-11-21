def solution(chicken):
    answer = 0
    coupon = 0
    while chicken > 1:
        coupon += chicken%10
        chicken = chicken//10
        answer += chicken
    coupon += chicken
    # 쿠폰이 10개가 넘는다면 추가 계산 필요
    if coupon >= 10:
        answer += (coupon//10+coupon)//10
    return answer

# 다른 풀이
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer