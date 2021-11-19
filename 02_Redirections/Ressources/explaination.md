# 02 - Redirections

## Reproduce

In the footer there are some social media links, inspecting this part we see the link used for the redirection as follow: `index.php?page=redirect&amp;site=facebook`, changing the site value and use this new value give the flag


## Explaination of the vulnerability

Hackers can use this vulnerability to :
- Give the user the illusion that he still in the original website, but instead he was redirected to a fake website to steal his credentials.
- Redirect him to unsafe website that contain malwares


## Fix 

- List the redirections in the backend
- Warn the users if they are going to leave the website