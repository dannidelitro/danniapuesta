import codecs

files = [
    r"c:\Users\dany\Documents\GitHub\danniapuesta\blog\tipos-de-apuestas-deportivas\index.html",
    r"c:\Users\dany\Documents\GitHub\danniapuesta\blog\apuestas-deportivas-guia-principiantes\index.html",
    r"c:\Users\dany\Documents\GitHub\danniapuesta\blog\apuestas-doble-oportunidad\index.html",
    r"c:\Users\dany\Documents\GitHub\danniapuesta\blog\como-hacer-pronosticos-deportivos\index.html",
    r"c:\Users\dany\Documents\GitHub\danniapuesta\blog\apuestas-primer-tiempo-segundo-tiempo\index.html",
]

css_block = """<style>
@keyframes pulseBono {
  0% { box-shadow: 0 0 0 0 rgba(0, 230, 118, 0.7); transform: scale(1); }
  50% { box-shadow: 0 0 25px 5px rgba(0, 230, 118, 0.5); transform: scale(1.02); }
  100% { box-shadow: 0 0 0 0 rgba(0, 230, 118, 0); transform: scale(1); }
}
.btn-novibet-pro {
  background: linear-gradient(135deg, #00e676, #00c6ff) !important;
  color: #051624 !important;
  font-weight: 900 !important;
  text-transform: uppercase !important;
  letter-spacing: 1px !important;
  border: 2px solid rgba(255,255,255,0.4) !important;
  animation: pulseBono 1.8s infinite !important;
  transition: all 0.3s ease !important;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 10px 15px;
  border-radius: 8px;
  text-decoration: none;
}
.btn-novibet-pro:hover {
  background: #fff !important;
  color: #00e676 !important;
  border-color: #00e676 !important;
  transform: translateY(-2px) scale(1.03) !important;
  box-shadow: 0 10px 30px rgba(0, 230, 118, 0.8) !important;
}
</style>
</head>"""

old_nav = '<nav class="nav-actions"><a class="nav-link" href="https://danniapuesta.com/blog/">Blog</a><a class="cta" href="https://danniapuesta.com/">Usar la App →</a></nav>'
new_nav = '<nav class="nav-actions"><a class="btn-novibet-pro" style="margin-right:12px; font-size:0.8rem;" href="javascript:void(0)" onclick="goNovibet()">🎁 Bono Novibet</a><a class="nav-link" href="https://danniapuesta.com/blog/">Blog</a><a class="cta" href="https://danniapuesta.com/">Usar la App →</a></nav>'

for f in files:
    with codecs.open(f, "r", "utf-8") as fh:
        content = fh.read()
    
    content = content.replace("</head>", css_block, 1)
    content = content.replace(old_nav, new_nav, 1)
    
    with codecs.open(f, "w", "utf-8") as fh:
        fh.write(content)
    
    print(f"OK Updated: {f.split(chr(92))[-2]}")

print("Done! Novibet button added to all 5 articles.")
