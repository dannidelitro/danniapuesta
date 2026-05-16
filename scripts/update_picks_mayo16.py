import re
import sys

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "MLS", partido: "Montréal vs Chicago", fecha: "16 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.85", prob: "68%", explicacion: "Racha de 7 Over 2.5 consecutivos de Chicago Fire. Montréal letal en transiciones en el Stade Saputo. (Value +0.258)" },
  { liga: "Série A (Brasil)", partido: "Fluminense vs São Paulo", fecha: "16 Mayo", pronostico: "Más de 5.5 Tarjetas", cuota: "1.75", prob: "70%", explicacion: "Choque de altísima intensidad en el Maracanã con promedio histórico de alta fricción táctica en la zona de gestación." },
  { liga: "Primeira Liga", partido: "Sporting CP vs Gil Vicente", fecha: "16 Mayo", pronostico: "Sporting +6.5 Córners", cuota: "1.65", prob: "69%", explicacion: "Sistema 3-4-3 del Sporting que abusa del juego por bandas frente a un bloque bajo muy estrecho de Gil Vicente." },
  { liga: "MLS", partido: "New England vs Minnesota", fecha: "16 Mayo", pronostico: "Minnesota o Empate (X2)", cuota: "1.80", prob: "58%", explicacion: "Minnesota registra 13 puntos obtenidos fuera de casa de 21 posibles. New England transita por inestabilidad táctica local." },
  { liga: "Primeira Liga", partido: "Benfica vs Estoril", fecha: "16 Mayo", pronostico: "Menos de 3.5 Goles", cuota: "1.50", prob: "71%", explicacion: "Estructura defensiva impecable de Benfica fuera de casa y bajo volumen ofensivo de Estoril. Partido de posesión controlada." },
  { liga: "Pro League", partido: "Sint-Truidense vs KAA Gent", fecha: "16 Mayo", pronostico: "Menos de 2.5 Goles", cuota: "1.80", prob: "62%", explicacion: "Tendencia defensiva cerrada en play-offs belgas. Proyección de partido de alta posesión horizontal con baja profundidad." },
  { liga: "MLS", partido: "Montréal vs Chicago", fecha: "16 Mayo", pronostico: "Montréal o Empate (1X)", cuota: "1.45", prob: "74%", explicacion: "Fortaleza extrema como local del CF Montréal con récord invicto de 4-1-0 en casa esta temporada." },
  { liga: "Série A (Brasil)", partido: "Fluminense vs São Paulo", fecha: "16 Mayo", pronostico: "Empate al Descanso", cuota: "1.95", prob: "55%", explicacion: "Fricción excesiva y miedo a perder en los primeros 45 minutos del derbi, proyectando un 0-0 al medio tiempo." },
  { liga: "Primeira Liga", partido: "Sporting CP vs Gil Vicente", fecha: "16 Mayo", pronostico: "Sporting Gana", cuota: "1.25", prob: "82%", explicacion: "Obligación de asegurar tres puntos con un poder de fuego de 86 goles a favor. Ancla perfecta para combinadas." },
  { liga: "MLS", partido: "NY Red Bulls vs NY City FC", fecha: "16 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.85", prob: "65%", explicacion: "Encuentro de alta presión y juego directo por las bandas. El modelo lineal múltiple estima una media conjunta de 10.4 córners." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 16.")
