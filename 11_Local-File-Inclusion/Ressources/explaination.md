# 11 - Local File Inclusion

## Reproduce

Developers usually divide a website’s code into directories, multiple files, etc. to make everything neat and readable. In order for an interpreter to find these files you need to designate the correct file path and then pass it to a function. The function then opens the file in question and includes it inside the document.

What happens when there’s no effective filtering? then we can access a file critical file like `/etc/passwd`

http://192.168.1.19/index.php?page=../../../../../../../etc/passwd

Tadaaaa we have the flag


## Explaination of vurnability

An attacker can use Local File Inclusion (LFI) to trick the web application into exposing or running files on the web server. An LFI attack may lead to information disclosure, remote code execution, or even Cross-site Scripting (XSS). Typically, LFI occurs when an application uses the path to a file as input


## Fix 

- Prevent users from passing input into the file systems and framework API. If this is not possible, the application can maintain a whitelist of files
