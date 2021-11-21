# 12 - XSS Feedback

## Reproduce

In the feedback section:  `http://{IP}/?page=feedback`

The user insert the name and a message as feedback, It was obvious that the trick is to try to insert a JavaScript script

`
<body onload="alert(1)"/>script
`

on submit ==> Tadaaa we got the flag 

PS: We found that inserting only `script` in one of the fields give the flag


## Explaination of vurnability

XSS: Cross Site Scripting, allows an attacker to execute arbitrary JavaScript within the browser of a victim user.


## Fix 

- Filter inputs on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
