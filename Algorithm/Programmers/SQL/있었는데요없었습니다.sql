--보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
--이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID AND B.DATETIME - A.DATETIME < 0
ORDER BY A.DATETIME