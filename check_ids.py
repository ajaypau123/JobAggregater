import re

app_js = open('dashboard/app.js', encoding='utf-8').read()
index_html = open('dashboard/index.html', encoding='utf-8').read()

ids = set(re.findall(r"document\.getElementById\(['\"](.*?)['\"]\)", app_js))
print(f"Total unique getElementById: {len(ids)}")

missing = []
for el_id in sorted(ids):
    pattern = rf'id=[\'"]{re.escape(el_id)}[\'"]'
    if not re.search(pattern, index_html):
        missing.append(el_id)

print(f"Missing IDs ({len(missing)}): {missing}")

