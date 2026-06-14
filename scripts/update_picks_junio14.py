import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "OBOS-ligaen (NOR)", partido: "FK Haugesund vs Ranheim", fecha: "14 Junio", pronostico: "Más de 2.5 Goles", cuota: "1.45", prob: "70%", explicacion: "Haugesund anota 2.5 por partido en casa; Ranheim encaja 3.25 de visita. P(>2.5) superior a 0.70." },
  { liga: "Primera Div (CHI)", partido: "U. La Calera vs Univ. de Chile", fecha: "14 Junio", pronostico: "Más de 8.5 Corners", cuota: "1.50", prob: "85%", explicacion: "Ambos promedian altísimo (5.6 y 5.9 a favor). Se proyecta asedio constante de la U." },
  { liga: "Série B (BRA)", partido: "EC Juventude vs Ponte Preta", fecha: "14 Junio", pronostico: "Local (Gana Juventude)", cuota: "1.65", prob: "75%", explicacion: "Juventude recibió 1 gol en toda la campaña local; Ponte Preta promedia 2.2 en contra de visita." },
  { liga: "OBOS-ligaen (NOR)", partido: "Åsane vs Odds BK", fecha: "14 Junio", pronostico: "Visita (Gana Odds BK)", cuota: "1.80", prob: "72%", explicacion: "Odds BK (4to) visita al colista Åsane, que apenas registra 15% de vallas invictas." },
  { liga: "Série B (BRA)", partido: "São Bernardo vs Sport Recife", fecha: "14 Junio", pronostico: "Local o Empate (1X)", cuota: "1.35", prob: "68%", explicacion: "Choque de punteros, pero el local es la mejor ofensiva del torneo (20 goles en 12 juegos)." },
  { liga: "Superettan (SUE)", partido: "Falkenbergs vs Örebro SK", fecha: "14 Junio", pronostico: "Local (Gana Falkenbergs)", cuota: "1.70", prob: "78%", explicacion: "Local en racha ganadora vs un Örebro con 3 derrotas al hilo y severa desconexión defensiva." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 14.")
