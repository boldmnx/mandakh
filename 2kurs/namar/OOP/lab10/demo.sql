SELECT *
FROM worker w
    INNER JOIN branch b ON w.b_id = b.id;