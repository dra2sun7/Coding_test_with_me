-- 5월 식품들의 총매출 조회하기
SELECT A.product_id, A.product_name, sum(A.price*B.amount)
from food_product A left join food_order B on A.product_id = B.product_id
where B.produce_date like "2022-05%"
group by A.product_id
order by sum(A.price*B.amount) desc, A.product_id asc

-- 주문량이 많은 아이스크림들 조회하기
SELECT A.flavor
from first_half A inner join july B on A.flavor = B.flavor
group by A.flavor
having sum(A.total_order)+sum(B.total_order)
order by sum(A.total_order)+sum(B.total_order) desc
limit 3

-- 조건에 맞는 도서와 저자 리스트 출력하기
SELECT A.book_id, B.author_name, date_format(A.published_date, "%Y-%m-%d") as published_date
from book A inner join author B on A.author_id = B.author_id
where A.category = '경제'
order by A.published_date

-- 없어진 기록 찾기
SELECT B.animal_id, B.name
from animal_outs B left join animal_ins A on B.animal_id = A.animal_id
where A.animal_id is Null
order by B.animal_id

-- 있었는데요 없었습니다
SELECT A.animal_id, B.name
from animal_ins A inner join animal_outs B on A.animal_id = B.animal_id
where A.datetime > B.datetime
order by A.datetime

-- 오랜 기간 보호한 동물
SELECT A.name, A.datetime
from animal_ins A left join animal_outs B on A.animal_id = B.animal_id
where B.animal_id is null
order by A.datetime
limit 3

-- 보호소에서 중성화된 동물
SELECT A.animal_id, A.animal_type, A.name
from animal_ins A inner join animal_outs B on A.animal_id = B.animal_id
where A.sex_upon_intake != B.sex_upon_outcome
order by A.animal_id

-- 상품 별 오프라인 매출 구하기
SELECT A.product_code, SUM(A.price*B.sales_amount) as sales
from product A inner join offline_sale B on A.product_id = B.product_id
group by A.product_code
order by SUM(A.price*B.sales_amount) desc, A.product_code asc
