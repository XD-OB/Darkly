# 04 - Robots Hidden

## Reproduce

To search for the directories and files we used `dirsearch` an advanced command-line tool designed to brute force directories and files in webservers (web path scanner)
`https://github.com/maurosoria/dirsearch`

We used the command:

`python3 dirsearch.py -u {IP}`

==> We found this paths:
- `http://{IP}/robots.txt`

Inside `robots.txt` we found some rules that forbide the rebots from indexing or visiting the folders:
- `/whatever`
- `/.hidden`

Inside `.hidden` we found a lot of nested directories, so we wrote a python script to browse them and print unique lines with there link, this results are stored in 'results.txt', aaaaaand BINGOOO! we found the flag

- `python3 find_flag.py`

`
...
99dde1d35d1fdd283924d84e6d9f1d820
`

## Explaination of the vurnability

Hiding very well the sensitive data, it's not a smart move, because hacker can use scripts to show all the data even the most hidded ones


## Fix 

- Delete all the sensitive files or hide it
