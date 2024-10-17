def check_max(hp, health, plus):
    if hp + plus > health:
        return health
    else:
        return hp + plus


def solution(bandage, health, attacks):
    
    time = 1
    b_time = 0
    a_time = 0
    hp = health
    
    while time <= attacks[-1][0]:
        
        if attacks[a_time][0] == time:
            hp -= attacks[a_time][1]
            if hp <= 0:
                return -1
            a_time += 1
            b_time = 0
        else:
            
            hp = check_max(hp, health, bandage[1])
            b_time += 1
            
            if b_time == bandage[0]:
                hp = check_max(hp, health, bandage[2])
                b_time = 0
                
        time += 1
        
    return hp
