--1. Ажилдаг нь үнэн болно
SELECT *
from worker;
--2.Орлогын дэлгэрэнгүй тайлан
SELECT *,
    (fprice::int * reapeat::int) "total"
FROM food
ORDER BY total desc;
--3. Захиалгын тайлан
SELECT w.wname,
    w.wlast,
    f.fname,
    b.fcount,
    b.bognoo
from bill b
    inner join worker w on w.wid = b.wid
    INNER JOIN food f on f.fid = b.fid;
--4. Сар хамгийн их зарагдсан хоол
SELECT f.fname,
    b.fcount "гарсан тоо",
    b.bognoo::varchar,
    (f.fprice::int * f.reapeat::int) "total"
from bill b
    INNER JOIN worker w on w.wid = b.wid
    INNER JOIN food f ON f.fid = b.fid
where b.bognoo between '2023-10-01' and '2023-10-31'
ORDER BY b.fcount::int DESC;
--5. Хамгийн олон захиалга авсан ажилтан (сараар)
SELECT w.wname,
    f.reapeat "Ширээний тоо",
    b.bognoo::varchar,
    (f.fprice::int * f.reapeat::int) "total"
from bill b
    INNER JOIN worker w on w.wid = b.wid
    INNER JOIN food f ON f.fid = b.fid
where b.bognoo between '2023-10-01' and '2023-10-31'
ORDER BY f.reapeat::int DESC;
-- # Орлогын тайлан
select w.wname,
    f.fname,
    d.dname,
    t.tname,
    b.bognoo,
    d.dprice,
    f.fprice,
    b.dcount,
    b.fcount,
    fc.fcat_name,
    (
        b.fcount::int * f.fprice::int + b.dcount::int * d.dprice::int
    ) "нийт үнэ"
from bill b
    inner join worker w on w.wid = b.wid
    inner join food f on f.fid = b.fid
    inner join "table" t on t.tid = b.tid
    inner join drink d on d.did = b.did
    inner join food_cat fc on fc.fcat_id = f.fid
group by f.fname,
    w.wname,
    d.dname,
    t.tname,
    b.bognoo,
    d.dprice,
    f.fprice,
    b.dcount,
    b.fcount,
    fc.fcat_name