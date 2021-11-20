# 12 - XSS Image

## Reproduce

While browsing the website we saw that just one on the images is clickable (NSA image), and it redirect us to:  `http://{IP}/index.php?page=media&src=nsa`

We inspected the HTML page and found that the image is displayed as follow:

`
<object data="http://192.168.1.19/images/nsa_prism.jpg"></object>
`

They used `<object>` instead of `<img>` and the url is the data,
so here we knew that we can use the XSS to execute an unwanted script, following this steps:

- Convert the unwanted script to base64 (passing it in encoded base64 is the best way):

`<script>alert('hacked')</script>` ==> `PHNjcmlwdD5hbGVydCgnaGFja2VkJyk8L3NjcmlwdD4=`

- Then we sent the request:

`http://{IP}/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGFja2VkJyk8L3NjcmlwdD4=`


## Explaination of vurnability

XSS: Cross Site Scripting, allows an attacker to execute arbitrary JavaScript within the browser of a victim user.


## Fix 

- Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
