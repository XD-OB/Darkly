# 00 - Hidden Form Input

## Reproduce

On the password recovery page "http://{IP}/?page=recover#" we found only a button to submit the mail so we inspected the HTML page and we found a hidden input that contain an email 'webmaster@borntosec.com' as value, its normaly the admin mail that receive the password reset requests.

By just changing the value of this input and submiting the form, we got the flag.

## Explaination of the  vulnerability

It's a bad practice to send or hide the values in hidden field especially when the data is sensitive.
In this case the admin mail is exposed so the hacker can bruteforce the password of this mail, or he can flood the email address.

'FLOOD AN EMAIL ADDRESS': The process of sending large quantities of emails, often with large attachments, in order to disable a network or part of a network such as a mail server. This is an example of a denial of service attack.

## Fix 

Don't use the hidden field to send or hide sensitive data.

In this case we can handle the request recover password in the Back-end