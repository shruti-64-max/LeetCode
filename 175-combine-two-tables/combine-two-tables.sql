# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM person p1
LEFT JOIN Address a1 
ON p1.personId=a1.personId;