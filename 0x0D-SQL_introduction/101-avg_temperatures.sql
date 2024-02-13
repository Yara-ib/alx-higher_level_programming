-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- IMPORT TABLE FROM temperatures
-- SELECT city FROM temperatures
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
-- cat temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
