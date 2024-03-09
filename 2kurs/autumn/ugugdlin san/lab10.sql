--3
SELECT w.wname,
    w.wlast,
    w.regdug,
    w.email,
    d.depname
FROM worker w
    INNER JOIN department d ON w.depcode = d.depcode;
--4
SELECT *,
    p.proname
FROM worker w
    INNER JOIN profession p ON p.procode = w.procode;
--5
SELECT su.suutname,
    su.suutdun,
    n.nemname,
    n.nemdun,
    w.wname,
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
    INNER JOIN nemegdel n ON n.nemcode = s.nemcode
    INNER JOIN suutgal su ON su.suutcode = s.suutcode;
--6
SELECT w.wname,
    w.wlast,
    w.regdug,
    w.phone,
    p.proname,
    d.depname
FROM worker w
    INNER JOIN profession p ON p.procode = w.procode
    INNER JOIN department d ON d.depcode = w.depcode
WHERE w.wcode = 'AC1';
--7
SELECT *,
    d.depname,
    p.proname
FROM worker w
    INNER JOIN profession p ON w.procode = p.procode
    INNER JOIN department d ON d.depcode = w.depcode;
--8
SELECT w.wname,
    w.wlast,
    w.regdug,
    s.salary
FROM worker w
    INNER JOIN salary s ON s.wcode = w.wcode
ORDER BY s.salary;
--9
SELECT w.wname,
    w.wlast,
    w.regdug,
    p.procode,
    p.proname,
    s.salary
FROM worker w
    INNER JOIN profession p ON p.procode = w.procode
    INNER JOIN salary s ON s.wcode = w.wcode
ORDER BY w.wname DESC;
--10
SELECT d.depname,
    COUNT(w.wcode) "Хэлтэст ажилчдийн тоо"
FROM worker w
    INNER JOIN department d ON d.depcode = w.depcode
GROUP BY d.depname;