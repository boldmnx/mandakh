SELECT w.id,
    w.name,
    b.bname
FROM worker AS w
    INNER JOIN branch AS b ON w.b_id = b.id
WHERE w.id = 1