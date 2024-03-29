-- 코드를 입력하세요
SELECT A.ID, A.NAME, COUNT(*)
  FROM (SELECT P.ID, P.NAME, SC.SCHEDULED_AT
          FROM PLACES P, SCHEDULES SC
         WHERE P.ID = SC.PLACE_ID) A
GROUP BY A.ID, A.NAME