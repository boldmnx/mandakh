-- 3
SELECT *
FROM tbl_order;
-- 4
SELECT a.id,
    a.name,
    s.name
FROM worker a
    INNER JOIN branch s ON a.branch_id = s.id;
-- 5
SELECT w.name,
    p.id,
    p.paid
FROM paid p
    INNER JOIN worker w ON p.worker_id = w.id;
--6
SELECT w.name,
    b.name
FROM worker w
    INNER JOIN branch b ON w.branch_id = b.id
WHERE w.name = 'Баатархүү';
--7
SELECT w.name,
    f.name,
    f.une,
    p.paid
FROM paid p ,tbl_order t 
    INNER JOIN food f ON p.food_id = f.id
    INNER JOIN worker w ON t.worker_id = w.id
WHERE t.id = '20121024/001'
OR p.id = '20121024/001'