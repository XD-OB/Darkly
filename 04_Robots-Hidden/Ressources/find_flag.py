import requests
import re


# link pattern
link_pattern = re.compile(r'<a href=\"(.*)\">')
# List of unique results
results = []



def     get_dir_contents(url):
    '''
    Check the content of a directory
    '''
    response = requests.get(url)
    if response.ok :
        content = response.text
    else :
        return 'ERROR'
    if url.endswith('/') :
        files = link_pattern.findall(content)
        for file in files :
            # Skip the parrent folder
            if file == '../' :
                pass
            else:
                get_dir_contents(url + file)
    else :
        if content not in [result['content'] for result in results] :
            results.append({'url': url, 'content': content})



url = 'http://192.168.1.12/.hidden/'
get_dir_contents(url)

# Write the results
with open('results.txt', 'w') as f :
    for element in results :
        f.write(element['url'] + ': ' + element['content'])
