SELECT name, lastname
FROM
 (
   SELECT valid_user.name, valid_user.lastname
   FROM valid_user
   UNION ALL
   SELECT reg_user.name, reg_user.lastname
   FROM reg_user
)  t
GROUP BY name, lastname
HAVING COUNT(*) = 1
ORDER BY name