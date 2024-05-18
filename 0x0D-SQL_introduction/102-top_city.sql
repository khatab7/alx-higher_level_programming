-- This script lists top 3 average temperatures during july and august

-- List top 3 average temperaturs during july and august
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
