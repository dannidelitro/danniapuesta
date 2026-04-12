import os
import glob
from datetime import datetime

base_dir = r"C:\Users\dany\Documents\GitHub\danniapuesta"
blog_dir = os.path.join(base_dir, "blog")

base_url = "https://danniapuesta.com"

urls = [
    {"loc": base_url + "/", "priority": "1.0", "changefreq": "daily"},
    {"loc": base_url + "/blog/", "priority": "0.9", "changefreq": "daily"},
]

# Find all index.html in blog subdirectories
for root, dirs, files in os.walk(blog_dir):
    if "index.html" in files and root != blog_dir:
        # Extract folder name
        folder_name = os.path.basename(root)
        url = f"{base_url}/blog/{folder_name}/"
        urls.append({"loc": url, "priority": "0.8", "changefreq": "weekly"})

# Generate sitemap XML
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

today = datetime.now().strftime("%Y-%m-%d")

for u in urls:
    xml += '  <url>\n'
    xml += f'    <loc>{u["loc"]}</loc>\n'
    xml += f'    <lastmod>{today}</lastmod>\n'
    xml += f'    <changefreq>{u["changefreq"]}</changefreq>\n'
    xml += f'    <priority>{u["priority"]}</priority>\n'
    xml += '  </url>\n'

xml += '</urlset>'

sitemap_path = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Sitemap generado con {len(urls)} URLs")
