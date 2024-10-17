-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, count(animal_id) as count
from animal_ins
group by animal_type
order by animal_type asc

-- 동명 동물 수 찾기
SELECT name, count(name) as COUNT
from animal_ins
where name is not null
group by name
having count(name) > 1
order by name

-- 입양 시각 구하기(1)
SELECT HOUR(DATETIME) as HOUR, count(animal_id) as COUNT
from animal_outs
group by hour(datetime)
having HOUR >= 9 and hour <= 19
order by hour(datetime)