--check fk
SELECT *
FROM sys.foreign_keys
WHERE name = 'fk_wcode';
--add fk
ALTER TABLE workera
ADD CONSTRAINT fk_dcode FOREIGN KEY (dcode) REFERENCES departmeant(dcode);
PostgreSQL 15