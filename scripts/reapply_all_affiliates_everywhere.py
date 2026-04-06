import os
import glob
import re

files = glob.glob(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\**\index.html", recursive=True)

script_tag = """
<script>
window.goNovibet = async function() {
  document.body.style.cursor = 'wait';
  try {
    const res = await fetch('https://ipapi.co/json/');
    const data = await res.json();
    const country = data.country_code;
    document.body.style.cursor = 'default';
    if(country === 'MX') {
      window.open('https://promo.novibet.mx/apuestas-deportivas/maquinav1/?btag=2007720_8533519146&utm_source=2007720_&utm_medium=affiliate&utm_campaign=DEPORTES&promocode=MAQUINAV1', '_blank');
    } else if(country === 'EC') {
      window.open('https://promo.ec.novibet.com/apuestas-deportivas/?btag=2007720_8533519157&utm_source=2007720_&utm_medium=affiliate&utm_campaign=welcomebonussports', '_blank');
    } else {
      window.open('https://pro.cl.novibet.com/apuestas-deportivas/chilean200/?btag=2007720_8533518657&utm_source=2007720_&utm_medium=affiliate&utm_campaign=CHILEAN200', '_blank');
    }
  } catch (err) {
    document.body.style.cursor = 'default';
    window.open('https://pro.cl.novibet.com/apuestas-deportivas/chilean200/?btag=2007720_8533518657&utm_source=2007720_&utm_medium=affiliate&utm_campaign=CHILEAN200', '_blank');
  }
};
</script>"""

css = """
<style>
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
</head>
"""

new_header_btn = r'<a class="btn-novibet-pro" style="margin-right:12px; font-size:0.8rem;" href="javascript:void(0)" onclick="goNovibet()">🎁 Bono Novibet</a>'
new_cta_btn = r'<br><br><a class="btn-novibet-pro" style="margin-top:10px;" href="javascript:void(0)" onclick="goNovibet()">💸 Reclamar Bono Novibet</a>'

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Add script tag
    if "window.goNovibet =" not in content:
        content = content.replace("</body>", script_tag + "\n</body>")
    else:
        # replace existing
        content = re.sub(r'<script>\s*window\.goNovibet.*?</script>', script_tag, content, flags=re.DOTALL)
    
    # 2. Add CSS
    if "pulseBono" not in content:
        content = content.replace("</head>", css)

    # Strip existing affiliate buttons to prevent dupes
    content = re.sub(r'<a[^>]*>(?:🎁 |)Bono Novibet.*?</a\s*>', "", content)
    content = re.sub(r'<a[^>]*>(?:💸 |)Reclamar Bono Novibet.*?</a\s*>', "", content)
    
    # Strip empty <br><br> traces
    content = re.sub(r'<br><br>\s*(</a>)?', "", content)

    # 3. Add to Header
    if '<div class="header-actions">' in content:
        content = content.replace('<div class="header-actions">', '<div class="header-actions">\n        ' + new_header_btn)
        
    # 4. Add to CTA Box (only in articles, not in the index which doesn't have it)
    if 'MEDIR MÍ RENDIMIENTO HOY' in content:
        content = content.replace('MEDIR MÍ RENDIMIENTO HOY →</a>', 'MEDIR MÍ RENDIMIENTO HOY →</a>\n        ' + new_cta_btn)
        
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print(f"Updated {len(files)} files!")
