import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Besta deild (ISL)", partido: "Víkingur vs KR Reykjavík", fecha: "16 Junio", pronostico: "Más de 3.5 Goles", cuota: "1.95", prob: "71%", explicacion: "El líder promedia más de 3 goles a favor; la visita ha encajado 23 en 10 juegos. Proyección altísima de goles." },
  { liga: "Superettan (SUE)", partido: "Värnamo vs Helsingborgs", fecha: "16 Junio", pronostico: "Local (Gana Värnamo)", cuota: "2.16", prob: "62%", explicacion: "Dominio histórico absoluto (6 victorias seguidas sobre Helsingborgs) compensa el ligero déficit de forma reciente." },
  { liga: "A Lyga (LIT)", partido: "TransINVEST vs Riteriai", fecha: "16 Junio", pronostico: "Hándicap As. -1.5 (Local)", cuota: "1.85", prob: "68%", explicacion: "El sublíder recibe al colista (-37 goles de diferencia). Historial directo de 5-0 y 3-0 en esta campaña." },
  { liga: "Superettan (SUE)", partido: "Landskrona vs United IK", fecha: "16 Junio", pronostico: "Doble Oportunidad (X2)", cuota: "1.65", prob: "75%", explicacion: "United IK es una roca estructural, cubriendo su hándicap positivo en 8 de sus últimos 9 partidos." },
  { liga: "A Lyga (LIT)", partido: "Žalgiris vs Panevėžys", fecha: "16 Junio", pronostico: "Local (Gana Žalgiris)", cuota: "1.50", prob: "80%", explicacion: "Paternidad total: 20 victorias históricas frente a su rival de hoy. Localía inquebrantable." },
  { liga: "Besta deild (ISL)", partido: "Stjarnan vs Breidablik", fecha: "16 Junio", pronostico: "Visita o Empate (X2)", cuota: "1.45", prob: "78%", explicacion: "Breidablik invicto en sus últimos 6 duelos directos contra un Stjarnan relegado a la zona baja." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 16.")
