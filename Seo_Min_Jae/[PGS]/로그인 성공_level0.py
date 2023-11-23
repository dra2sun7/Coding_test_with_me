def solution(id_pw, db):
    answer = ''
    for user in db:
        if id_pw[0] == user[0]:
            if id_pw[1] == user[1]:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break
        else:
            answer = 'fail'
    return answer

# 다른 풀이
def solution(id_pw, db):
    # db를 dict의 형태로 바꾸고 get을 통해 id_pw[0]의 키와 연관된 값을 검색
    # 값이 존재하면 db_pw가 할당되고 true가 되며, 존재하지 않으면 db_pw는 None이 되고 false가 된다
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"