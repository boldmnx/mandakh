--2
SELECT b.bookcode,
    b.bookname,
    b.author,
    b.bindex,
    b.page,
    t.tname,
    dt.dtname
FROM book b
    INNER JOIN torol t ON t.tcode = b.tcode
    INNER JOIN dedtorol dt ON dt.dtcode = b.dtcode;
--3
SELECT *,
    m.mname
FROM student s
    INNER JOIN mergejil m ON m.mcode = s.mcode
WHERE s.stname ILIKE '%гэрэл%';
--4
SELECT m.mname,
    count(s.mcode)
FROM student s
    INNER JOIN mergejil m on m.mcode = s.mcode
GROUP BY m.mname;
--5
SELECT *
FROM student
WHEre stcode ILIKE 'SA14d005';
--6
SELECT s.stname "оюутан",
    l.lname "номын олгогч"
from BOok b
    INNER JOIN bookgive bg on bg.bcode = b.bookcode
    INNER JOIN student s on bg.stcode = s.stcode
    INNER JOIN librarian l on bg.libcode = l.lcode
where b.bookcode ilike 'swco001';
--7
SELECT ognoo,
    *
from student
ORDER BY ognoo;
--8
select s.stname,
    bg.enterognoo,
    bg.retognoo,
    b.bookname,
    l.lname "Номын санч"
from student s
    inner join bookgive bg on bg.stcode = s.stcode
    inner join librarian l on bg.libcode = l.lcode
    inner join book b on b.bookcode = bg.bcode
where s.ognoo BETWEEN '10/1/2014' and '9/1/2015';
--9
SELECT m.mname "Мэргэжил",
    count(s.mcode) "Оюутны тоо"
FROM student s
    inner join mergejil m on s.mcode = m.mcode
GROUP BY m.mname;