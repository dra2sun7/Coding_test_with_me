-- 가장 비싼 상품 구하기
SELECT MAX(PRICE) AS MAX_PRICE FROM PRODUCT

-- 가격이 제일 비싼 식품의 정보 출력하기
SELECT product_id, product_name, product_cd, category, price
from food_product
where price in (select max(price) from food_product)

-- 최댓값 구하기
SELECT MAX(DATETIME) FROM ANIMAL_INS

-- 최솟값 구하기
SELECT MIN(DATETIME) FROM ANIMAL_INS

-- 동물 수 구하기
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS

-- 중복 제거하기
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS

-- 조건에 맞는 아이템들의 가격의 총합 구하기
SELECT SUM(price) AS TOTAL_PRICE
from item_info
where RARITY = 'LEGEND'

-- 잡은 물고기 중 가장 큰 물고기의 길이 구하기
SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO