# 05 - Admin Cookie

## Reproduce

While browsing the cookies in the `Application` on the developer console, we notice a cookie named `I_am_admin` with a hashed value, we decrypted the value using MD5  then we got the value `false`, by changing the value of the cookie to `true (hashed)`.
After we refresh the page, an alert pops with the flag


## Explaination of the vurnability

The developer tried to solve some sort of authentication by using cookies, by manipulating the values you can have access to some privileges, In general never put sensitive data in cookies.


## Fix 

- Use JWT (Json Web Token) for authentication
