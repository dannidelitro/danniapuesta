import os
import glob
import re

files = glob.glob(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\*\index.html")

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
      window.open('https://rt.novibet.partners/o/AidpXC?lpage=qCU90V&site_id=1024102', '_blank');
    } else if(country === 'EC') {
      window.open('https://rt.novibet.partners/o/3_uD5_?lpage=kg9EYJ&site_id=1024102', '_blank');
    } else {
      window.open('https://rt.novibet.partners/o/hwi2qC?site_id=1024102', '_blank');
    }
  } catch (err) {
    document.body.style.cursor = 'default';
    window.open('https://rt.novibet.partners/o/hwi2qC?site_id=1024102', '_blank');
  }
};
</script>
"""

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    modified = False
    
    # 1. Add script tag
    if "goNovibet" not in content:
        content = content.replace("</body>", script_tag + "\n</body>")
        modified = True
    
    # 2. Extract CSS variable values explicitly because blog template doesn't have var(--verde) mapped inside style tag
    verde_color = "#00e676"
    
    # 3. Add to Header
    header_btn = f'\\n        <a class="header-cta" style="background:{verde_color};color:#000;font-weight:bold;margin-left:8px;" href="javascript:void(0)" onclick="goNovibet()">🎁 Bono Novibet</a>'
    if "Bono Novibet" not in content and '<div class="header-actions">' in content:
        content = content.replace('      </div>\n    </div>\n  </header>', header_btn + '\n      </div>\n    </div>\n  </header>')
        modified = True
        
    # 4. Add to CTA Box
    cta_btn = f'<a class="cta-button" style="background:{verde_color};color:#000;margin-left:10px;" href="javascript:void(0)" onclick="goNovibet()">💸 Bono Novibet</a>'
    if "Bono Novibet" not in content and 'MEDIR MÍ RENDIMIENTO HOY' in content:
        content = content.replace('MEDIR MÍ RENDIMIENTO HOY →</a>', 'MEDIR MÍ RENDIMIENTO HOY →</a>\n        ' + cta_btn)
        modified = True

    if modified:
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated: {f}")
print("All blogs updated successfully!")
