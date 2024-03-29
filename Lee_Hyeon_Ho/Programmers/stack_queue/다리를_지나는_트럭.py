def solution(bridge_length, weight, truck_weights):
    answer = 0
    location = []
    in_truck = []
    while len(truck_weights) != 0:
        if len(location) == 0:
            in_truck.append(truck_weights.pop(0))
            location.append(1)
        else:
            for i in range(len(location)):
                location[i] += 1
            if location[0] > bridge_length:
                location.pop(0)
                in_truck.pop(0)
            if sum(in_truck) + truck_weights[0] <= weight:
                in_truck.append(truck_weights.pop(0))
                location.append(1)
        answer += 1
    answer += bridge_length - location[-1] + 1
    return answer
