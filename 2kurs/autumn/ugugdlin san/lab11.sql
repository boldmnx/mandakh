--2
SELECT w.wname,
    w.wname,
    w.email,
    d.depname
FROM worker w
    INNER JOIN department d ON d.depcode = w.depcode;
--3
SELECT w.*,
    p.proname
FROM worker w
    INNER JOIN profession p ON p.procode = w.procode;
--4
SELECT w.wname,
    w.wlast,
    s.salary,
    s.tax,
    s.ndsh,
    n.nemname,
    n.nemdun,
    s.payment,
    s.garolgoh
FROM worker w
    INNER JOIN salary s ON s.wcode = w.wcode
    INNER JOIN nemegdel n ON n.nemcode = s.nemcode;
--5
SELECT d.depname,
    COUNT(w.depcode) "Ажилтны тоо"
FROM worker w
    INNER JOIN department d ON d.depcode = w.depcode
GROUP BY d.depname;
--6
SELECT d.depname,
    SUM(s.salary) "Хэлтэс тус бүрийн нийт цалин"
FROM worker w
    INNER JOIN department d ON d.depcode = w.depcode
    INNER JOIN salary s ON s.wcode = w.wcode
GROUP BY d.depname;
--7
SELECT MAX(CAST(nemdun AS INT)) "MAX",
    MIN(CAST(nemdun AS INT)) "MIN"
FROM nemegdel;
--8
SELECT w.*,
    p.proname,
    d.depname
FROM worker w
    INNER JOIN department d ON d.depcode = w.depcode
    INNER JOIN profession p ON p.procode = w.procode;
--9 NO task
--10 used in lab9
SELECT o.id,
    f.name,
    o.hemjee
FROM food f
    INNER JOIN tbl_order o ON o.food_id = f.id
ORDER BY o.hemjee DESC;
--
SELECT f.name,
    COUNT(o.food_id)
FROM tbl_order o
    INNER JOIN food f ON f.id = o.food_id
GROUP BY f.name;