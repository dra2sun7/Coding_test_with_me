def check_opening(pos, op_start, op_end):
    if pos >= op_start and pos < op_end:
        return op_end
    else:
        return pos

def check_end(pos, video):
    x = pos.split(":")
    
    if (int(x[1]) + 10) > 60:
        x[0] = str(int(x[0]) + 1).zfill(2)
        x[1] = str(int(x[1]) - 50).zfill(2)
        
    else:
        x[1] = str(int(x[1]) + 10).zfill(2)
        
    pos = x[0] + ":" + x[1]
    
    if pos > video:
        return video
    else:
        return pos

def check_start(pos):
    x = pos.split(":")
    
    if (int(x[1]) - 10) < 0:
        x[0] = str(int(x[0]) - 1).zfill(2)
        
        x[1] = str(int(x[1]) + 50).zfill(2)
        
    else:
        x[1] = str(int(x[1]) - 10).zfill(2)
    
    if int(x[0]) == -1:
        return "00:00"
    else:
        return x[0] + ":" + x[1]
    
    

def solution(video_len, pos, op_start, op_end, commands):
    for x in commands:
        pos = check_opening(pos, op_start, op_end)
        
        if x == "next":
            pos = check_end(pos, video_len)
        elif x == "prev":
            pos = check_start(pos)
            
        print(x + "                 " + pos)
        
    
    return check_opening(pos, op_start, op_end)
