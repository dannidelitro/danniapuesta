import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Allsvenskan (SUE)", partido: "Örgryte vs Elfsborg", fecha: "29 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.18", prob: "92%", explicacion: "La visita promedia 1.40 goles frente a un colista local en crisis absoluta." },
  { liga: "Eliteserien (NOR)", partido: "Brann vs Sarpsborg", fecha: "29 Mayo", pronostico: "Local +0.5 Goles", cuota: "1.12", prob: "91%", explicacion: "Brann posee un ataque temible en casa promediando 2.09 goles por encuentro." },
  { liga: "Eliteserien (NOR)", partido: "Rosenborg vs Bodø/Glimt", fecha: "29 Mayo", pronostico: "Bodø/Glimt o Empate (X2)", cuota: "1.18", prob: "84%", explicacion: "El líder arrollador (Bodø/Glimt) visita a un gigante histórico hundido en crisis defensiva." },
  { liga: "Eliteserien (NOR)", partido: "Vålerenga vs Kristiansund", fecha: "29 Mayo", pronostico: "Vålerenga o Empate (1X)", cuota: "1.13", prob: "83%", explicacion: "Imbatibilidad reciente en el Intility Arena frente a una visita muy débil." },
  { liga: "Eliteserien (NOR)", partido: "Vålerenga vs Kristiansund", fecha: "29 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.50", prob: "82%", explicacion: "Vålerenga promedia unos asombrosos 7.4 saques de esquina por encuentro como local." },
  { liga: "Superliga (CHN)", partido: "Liaoning vs Shanghai Port", fecha: "29 Mayo", pronostico: "Más de 3.5 Tarjetas", cuota: "1.65", prob: "81%", explicacion: "Duelo de fricción alta en la zona media del fútbol asiático." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 29.")
