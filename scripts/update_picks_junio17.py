import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Meistriliiga (EST)", partido: "Nõmme Utd vs Levadia", fecha: "17 Junio", pronostico: "Visita (Gana Levadia)", cuota: "1.23", prob: "88%", explicacion: "Líder invicto con 100% de efectividad goleadora frente a la peor defensa del torneo. Valor esperado positivo del 8.2%." },
  { liga: "Veikkausliiga (FIN)", partido: "IF Gnistan vs FC Lahti", fecha: "17 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "85%", explicacion: "Convergencia ofensiva perfecta; Gnistan promedia 3.10 goles totales en sus juegos. Gran seguridad matemática." },
  { liga: "Veikkausliiga (FIN)", partido: "SJK vs VPS", fecha: "17 Junio", pronostico: "Córneres SJK +4.5", cuota: "1.44", prob: "83%", explicacion: "SJK genera 7.00 córneres en promedio como local debido a su intensidad por las bandas. Línea mal ajustada por las bookies." },
  { liga: "Meistriliiga (EST)", partido: "Kalju vs Tartu Tammeka", fecha: "17 Junio", pronostico: "Doble Oportunidad (1X)", cuota: "1.36", prob: "82%", explicacion: "Kalju es sólido en casa (1.75 PPG) frente a un Tartu que promedia casi 2 goles en contra como visitante." },
  { liga: "A Lyga (LIT)", partido: "Hegelmann vs Džiugas", fecha: "17 Junio", pronostico: "Doble Oportunidad (X2)", cuota: "1.48", prob: "78%", explicacion: "Džiugas llega en estado de forma excepcional; ineficiencia en las cuotas al subestimar su solidez fuera de casa." },
  { liga: "Veikkausliiga (FIN)", partido: "HJK vs Inter Turku", fecha: "17 Junio", pronostico: "Más de 8.5 Córneres", cuota: "1.50", prob: "80%", explicacion: "Choque de estilos verticales. Ambos promedian cerca de 10 córneres por partido; altísima probabilidad combinada." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 17.")
