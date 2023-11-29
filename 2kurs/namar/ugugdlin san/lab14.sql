--1
SELECT b.bookname,
    b.bookcode,
    b.author,
    t.tname,
    bg.enterognoo,
    bg.retognoo,
    l.lname,
    s.stname
FROM bookgive bg
    INNER JOIN book b on b.bookcode = bg.bcode
    INNER JOIN torol t ON b.tcode = t.tcode
    INNER JOIN librarian l ON l.lcode = bg.libcode
    INNER JOIN student s ON s.stcode = bg.stcode;
--2
SELECT s.stcode,
    s.stlast,
    s.stname,
    s.regdug,
    m.mname,
    s.phone,
    s.ognoo
FROM student s
    INNER JOIN mergejil m ON m.mcode = s.mcode;
--3
SELECT b.bookcode,
    b.bookname,
    b.author,
    t.tname,
    dt.dtname,
    b.bindex,
    b.page,
    l.lname
FROM book b
    INNER JOIN torol t ON t.tcode = b.tcode
    INNER JOIN dedtorol dt ON dt.dtcode = b.dtcode
    INNER JOIN bookgive bg ON bg.bcode = b.bookcode
    INNER JOIN librarian l ON l.lcode = bg.libcode;
--4
SELECT *
FROM librarian