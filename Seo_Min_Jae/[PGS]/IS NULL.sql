-- 경기도에 위치한 식품창고 목록 출력하기
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IF(ISNULL(freezer_yn), 'N', FREEZER_YN) AS FREEZER_YN
from food_warehouse
where address like '경기%'
order by warehouse_id asc

-- 이름이 없는 동물의 아이디
SELECT animal_id
from animal_ins
where name is null
order by animal_id asc

-- 이름이 있는 동물의 아이디
SELECT animal_id
from animal_ins
where name is not null
order by animal_id asc

-- 나이 정보가 없는 회원 수 구하기
SELECT count(user_id) as USERS
from user_info
where age is null