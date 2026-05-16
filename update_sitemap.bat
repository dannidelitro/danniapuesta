echo ^<?xml version="1.0" encoding="UTF-8"?^> > sitemap.xml
echo ^<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"^> >> sitemap.xml
echo   ^<url^>^<loc^>https://danniapuesta.com/^</loc^>^<lastmod^>2026-05-16^</lastmod^>^<changefreq^>daily^</changefreq^>^<priority^>1.0^</priority^>^</url^> >> sitemap.xml
echo   ^<url^>^<loc^>https://danniapuesta.com/blog/^</loc^>^<lastmod^>2026-05-16^</lastmod^>^<changefreq^>daily^</changefreq^>^<priority^>0.9^</priority^>^</url^> >> sitemap.xml
for /d %%D in (blog\*) do (
  if exist "%%D\index.html" (
    echo   ^<url^>^<loc^>https://danniapuesta.com/blog/%%~nxD/^</loc^>^<lastmod^>2026-05-16^</lastmod^>^<changefreq^>weekly^</changefreq^>^<priority^>0.8^</priority^>^</url^> >> sitemap.xml
  )
)
echo ^</urlset^> >> sitemap.xml
