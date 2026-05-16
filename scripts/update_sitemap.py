import os
from datetime import datetime

base_dir = r"c:\Users\dany\Documents\GitHub\danniapuesta"
blog_dir = os.path.join(base_dir, "blog")
sitemap_path = os.path.join(base_dir, "sitemap.xml")

today_str = datetime.now().strftime("%Y-%m-%d")

urls = []
urls.append(f"""  <url>
    <loc>https://danniapuesta.com/</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")
urls.append(f"""  <url>
    <loc>https://danniapuesta.com/blog/</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>""")

# Iterate through all subdirectories in the blog folder
for item in os.listdir(blog_dir):
    item_path = os.path.join(blog_dir, item)
    if os.path.isdir(item_path):
        # Check if index.html exists in this folder
        if os.path.exists(os.path.join(item_path, "index.html")):
            # Add to sitemap
            urls.append(f"""  <url>
    <loc>https://danniapuesta.com/blog/{item}/</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Sitemap updated successfully with {len(urls)} URLs.")
