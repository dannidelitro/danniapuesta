import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Amistosos FIFA", partido: "Noruega vs Suecia", fecha: "1 Junio", pronostico: "Suecia o Empate (X2)", cuota: "1.85", prob: "65%", explicacion: "Noruega llega con dudas ofensivas, mientras que Suecia arrastra un óptimo momento goleador." },
  { liga: "Amistosos FIFA", partido: "Austria vs Túnez", fecha: "1 Junio", pronostico: "Gana Austria", cuota: "1.50", prob: "75%", explicacion: "Claro favoritismo local en Viena (cuota 1/2) de cara a la preparación final mundialista." },
  { liga: "Amistosos FIFA", partido: "Turquía vs Macedonia N.", fecha: "1 Junio", pronostico: "Gana Turquía", cuota: "1.22", prob: "80%", explicacion: "Turquía muestra un bloque muy superior y las casas le asignan una cuota de 2/9 de victoria." },
  { liga: "Copa Argentina", partido: "Racing Club vs Defensa y Justicia", fecha: "1 Junio", pronostico: "Más de 5.5 Tarjetas", cuota: "1.65", prob: "70%", explicacion: "Choque eliminatorio de altísima fricción e intensidad física típica del fútbol argentino." },
  { liga: "Série A (BRA)", partido: "Cruzeiro vs Fluminense", fecha: "1 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.60", prob: "68%", explicacion: "Duelo estratégico y cerrado por la necesidad de puntuar antes de la pausa invernal." },
  { liga: "WK League (KOR)", partido: "Hwacheon KSPO vs Suwon FC", fecha: "1 Junio", pronostico: "Ambos Marcan (Sí)", cuota: "1.75", prob: "72%", explicacion: "Choque directo en la cima del torneo femenino. Alta vocación ofensiva de ambas escuadras." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 1.")
