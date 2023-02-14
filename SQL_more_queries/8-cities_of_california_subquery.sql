-- list all cities
SELECT id,name FROM cities WHERE state_id IN(SELECT id FROM states WHERE name = 'california') ORDER BY id;
