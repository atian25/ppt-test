import re

with open('/workspace/SOLO-0408-直播/ppt/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find <figure class="frame-img" ...> ... <div class="frame-cap"> ... </div> </figure>
# and replace it with <figure class="tile" ...> <div class="frame-img" ...> <img ...> </div> <div class="frame-cap"> ... </div> </figure>

def replacer(match):
    style = match.group(1)
    img_tag = match.group(2)
    cap_div = match.group(3)
    return f'<figure class="tile" style="align-self:center">\n      <div class="frame-img" style="{style}">\n        {img_tag}\n      </div>\n      {cap_div}\n    </figure>'

pattern = r'<figure class="frame-img" style="([^"]+)">(.*?)(<div class="frame-cap">.*?</div>)\s*</figure>'
content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open('/workspace/SOLO-0408-直播/ppt/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed image wrappers")
