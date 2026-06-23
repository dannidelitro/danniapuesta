import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Veikkausliiga (FIN)", partido: "IFK Mariehamn vs HJK", fecha: "23 Junio", pronostico: "X2 (Visita o Empate)", cuota: "1.15", prob: "94%", explicacion: "Mariehamn sigue sin victorias en el torneo. HJK domina históricamente y llega con inercia goleadora letal." },
  { liga: "Veikkausliiga (FIN)", partido: "FC Inter vs SJK", fecha: "23 Junio", pronostico: "1X (Local o Empate)", cuota: "1.18", prob: "93%", explicacion: "El líder FC Inter está invicto en casa (4 victorias, 3 empates). SJK sufre enormemente fuera de su feudo." },
  { liga: "Veikkausliiga (FIN)", partido: "KuPS vs Ilves", fecha: "23 Junio", pronostico: "1X (Local o Empate)", cuota: "1.20", prob: "92%", explicacion: "KuPS es un bastión defensivo: 8 juegos invicto en casa y solo 0.71 goles en contra. Ilves no gana a domicilio." },
  { liga: "Primera Nac (ARG)", partido: "Nueva Chicago vs Atl. Rafaela", fecha: "23 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "88%", explicacion: "La defensa de Chicago en Mataderos es muy compacta. Rafaela arrastra 6 salidas sin conseguir los tres puntos." },
  { liga: "Veikkausliiga (FIN)", partido: "FC Lahti vs TPS", fecha: "23 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "88%", explicacion: "El 94% de sus históricos superaron esta línea. Lahti anota 1.83 de local y encaja con facilidad ante transiciones." },
  { liga: "Série B (BRA)", partido: "América-MG vs Criciúma", fecha: "23 Junio", pronostico: "X2 (Visita o Empate)", cuota: "1.35", prob: "85%", explicacion: "América-MG marcha último, sin ganar. Criciúma es vertical y sabrá explotar la desesperación y los espacios del local." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 23.")
