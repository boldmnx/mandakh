SELECT EXTRACT(
        year
        FROM age(current_date, enterognoo)
    ) as Нас
FROM "Bookgive"
WHERE bookcode = 'Swco001';
-- extractaar yeariig avna
-- ageeer year,month,day iig gargah avna
-- to_date str to date ru horwuulne
-- substring n datanas hussen hesege tasdaj avna
SELECT extract(
        year
        from age(
                current_date,
                TO_DATE(
                    SUBSTRING(
                        'Вю95123008'
                        FROM 3 for 6
                    ),
                    'YYMMDD'
                )
            )
    ) AS Нас
from "Bookgive"
where bookcode = 'Swco001';
--
select bookname
from "Book"
order by random()
limit 1