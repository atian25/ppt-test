import re
import urllib.request
import os
import ssl

html_path = '/workspace/SOLO-0408-直播/ppt/index.html'
images_dir = '/workspace/SOLO-0408-直播/ppt/images'

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all remote image sources
pattern = r'src="(https?://[^"]+)"'
urls = list(set(re.findall(pattern, content)))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i, url in enumerate(urls):
    local_filename = f'{i+1:02d}-slide-image.png'
    local_path = os.path.join(images_dir, local_filename)
    
    print(f'Downloading image {i+1}...')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        
        # Replace in HTML
        content = content.replace(url, f'images/{local_filename}')
        print(f'Successfully downloaded and replaced: images/{local_filename}')
    except Exception as e:
        print(f'Failed to download {url}: {e}')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
