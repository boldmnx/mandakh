SELECT u."username",
    n."Titile",
    n."Content",
    c."Catname",
    s."subcatname"
FROM news n
    INNER JOIN "User" u on n.userid = u.userid
    INNER JOIN "Category" c on n."Category" = c.catid
    INNER JOIN "SubCategory" s on n."Subcategory" = s.subcatid
ALTER TABLE "news"
    RENAME "Titile" TO "Title"
SELECT *
FROM "news"