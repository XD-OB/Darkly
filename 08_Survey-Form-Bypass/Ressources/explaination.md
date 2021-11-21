# 08 - Survey Form Bypass

## Reproduce

On the survey page: `http://{IP}/?page=survey`
There is some forms to submit the grades, by inspecting the select element we found that the form take the values from the front, so we can easily bypass the front-end verification by simply edit the value and submit the form.

## Explanation of the vulnerability

In this case the user can bypass easily this simple front-end verification and send whatever the value he want.

## Fix

- Add a verification layer in the back-end
