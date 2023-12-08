select t.name "tname",
    *,
    o.name "oname"
from hicheel h
    INNER JOIN turul t on t.id = h.turul_id
    INNER JOIN oholboo o ON o.id = h.oholboo_id
where hcode COLLATE NOCASE LIKE '%harr%'