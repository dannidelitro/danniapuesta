import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "NPL Victoria (AUS)", partido: "Oakleigh vs St. Albans", fecha: "5 Junio", pronostico: "Local Anota (Más 0.5)", cuota: "1.15", prob: "95%", explicacion: "Oakleigh es dominante en casa frente a una zaga que concede 2.00 goles por visita." },
  { liga: "Leinster (IRE)", partido: "Tolka Rovers vs Inchicore", fecha: "5 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.20", prob: "93%", explicacion: "Línea hiper-segura: Tolka registra 100% de over 1.5 e Inchicore un 91% en liga regional." },
  { liga: "NPL N. NSW (AUS)", partido: "Valentine vs Broadmeadow", fecha: "5 Junio", pronostico: "Visita o Empate (X2)", cuota: "1.25", prob: "91%", explicacion: "Broadmeadow es el líder apabullante y ahogará a Valentine con su 58% de posesión." },
  { liga: "1 Lyga (LIT)", partido: "Ekranas vs Neptūnas", fecha: "5 Junio", pronostico: "Visita o Empate (X2)", cuota: "1.30", prob: "89%", explicacion: "El H2H histórico es brutal: 8 triunfos seguidos para Neptunas sobre un Ekranas hundido." },
  { liga: "NPL Victoria (AUS)", partido: "Bentleigh vs Hume City", fecha: "5 Junio", pronostico: "Visita o Empate (X2)", cuota: "1.35", prob: "84%", explicacion: "Hume anota 2.00 por duelo de visita; Bentleigh es ineficaz y pierde el 47% de sus juegos." },
  { liga: "CPL (CAN)", partido: "Vancouver FC vs Atl. Ottawa", fecha: "5 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.45", prob: "80%", explicacion: "Vancouver no rinde en casa y recibe a un Ottawa con inyección anímica por cambio de técnico." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 5.")
