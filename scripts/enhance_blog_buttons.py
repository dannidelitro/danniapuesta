import glob
import re

files = glob.glob(r'C:\Users\dany\Documents\GitHub\danniapuesta\blog\*\index.html')

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

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # Inject CSS once
    if "btn-novibet-pro" not in content:
        content = content.replace("</head>", css)
        modified = True
        
    # Replace old buttons
    content = re.sub(r'<a class="header-cta"[^>]*>🎁 Bono Novibet</a>', 
                     r'<a class="btn-novibet-pro" style="margin-left:8px;" href="javascript:void(0)" onclick="goNovibet()">🎁 Bono Novibet</a>',
                     content)
                     
    content = re.sub(r'<a class="cta-button"[^>]*>💸 Bono Novibet</a>', 
                     r'<br><br><a class="btn-novibet-pro" style="margin-top:10px;" href="javascript:void(0)" onclick="goNovibet()">💸 Reclamar Bono Novibet</a>',
                     content)
                     
    with open(f, 'w', encoding='utf-8') as out:
        out.write(content)

print("Blog buttons enhanced.")
