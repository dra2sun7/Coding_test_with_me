-- 평일 일일 대여 요금 구하기
SELECT ROUND(AVG(daily_fee), 0) as AVERAGE_FEE
from car_rental_company_car
where car_type = 'SUV'

-- 흉부외과 또는 일반외과 의사 목록 출력하기
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd, "%Y-%m-%d")
from doctor
where mcdp_cd = 'CS' or mcdp_cd = 'GS'
order by hire_ymd desc, dr_name asc

-- 3월에 태어난 여성 회원 목록 출력하기
SELECT member_id, member_name, gender, date_format(date_of_birth, "%Y-%m-%d") as date_of_birth
from member_profile
where month(date_of_birth) = 3 and gender = 'W' and tlno is not null
order by member_id asc

-- 인기있는 아이스크림
SELECT flavor
from first_half
order by total_order desc, shipment_id asc

-- 강원도에 위치한 생산공장 목록 출력하기
SELECT factory_id, factory_name, address
from food_factory
where address like "강원도%"
order by factory_id asc

-- 12세 이하인 여자 환자 목록 출력하기
SELECT pt_name, pt_no, gend_cd, age, if(isnull(tlno), 'NONE', tlno) as tlno
from patient
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name asc

-- 조건에 맞는 도서 리스트 출력하기
SELECT book_id, date_format(published_date, "%Y-%m-%d") as published_date
from book
where year(published_date) = 2021 and category = '인문'
order by published_date asc

-- 모든 레코드 조회하기
SELECT *
from animal_ins
order by animal_id

-- 역순 정렬하기
SELECT name, datetime
from animal_ins
order by animal_id desc

-- 아픈 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick';

-- 어린 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged';

-- 동물의 아이디와 이름
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

-- 여러 기준으로 정렬하기
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC;

-- 상위 n개 레코드
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1;

-- 조건에 맞는 회원수 구하기
SELECT COUNT(USER_ID) FROM USER_INFO 
    WHERE YEAR(JOINED) = 2021 AND AGE >= 20 AND AGE <= 29

-- 업그레이드 된 아이템 구하기
SELECT IT.ITEM_ID, II.ITEM_NAME, II.RARITY
FROM ITEM_INFO AS II
    INNER JOIN ITEM_TREE AS IT ON II.ITEM_ID = IT.ITEM_ID
WHERE IT.PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY='RARE')
ORDER BY IT.ITEM_ID DESC