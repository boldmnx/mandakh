--1
use supermarket create table worker(
    wcode nvarchar(50) not null primary key,
    wlast nvarchar(50),
    wname nvarchar(50),
    regdug nvarchar(50),
    dcode int,
);
--2
insert into worker
values(N'T101', N'Гэрэлтуяа', N'Бат', N'Нх86022510', 1),
    (N'T102', N'Дорж', N'Болд', N'Че88011425', 1);
--3
select *
from worker
ORDER BY wname;
--4
SELECT *
FROM customer
WHERE cname like N'%туяа%';
--5
SELECT *
FROM deposit
WHERE ozdate BETWEEN N'2009/12/01' AND N'2012/12/01';
--6
SELECT *
FROM worker
WHERE regdug LIKE N'%8602%';
--7
SELECT d.dname,
    COUNT(w.dcode) "Ажилчдийн тоо"
FROM worker w
    INNER JOIN department d ON w.dcode = d.dcode
GROUP BY d.dname;
--8
SELECT *
FROM customer
ORDER BY regdate DESC;
--9
SELECT *
FROM worker;
--10
SELECT w.wlast,
    SUM(CAST(d.deposit as int)) 'нийт орлого'
FROM deposit d
    INNER JOIN worker w ON w.wcode = d.wcode
WHERE w.wcode = 'T101'
GROUP BY w.wlast;
--11
SELECT w.wname,
    w.wlast,
    w.regdug,
    d.ozdate,
    d.deposit,
    d.oz,
    d.dnum
FROM worker w
    INNER JOIN deposit d ON d.wcode = w.wcode
WHERE d.oz = N'Орлого';
--12
INSERT INTO worker
VALUES(
        N'T103',
        N'Мөнхбат',
        N'Урангоо',
        N'нл95122540',
        2
    );
--13
UPDATE worker
SET wname = N'Уянга',
    dcode = 3
WHERE wcode = N'T103';
--14
DELETE FROM worker
WHERE wcode = N'T103';