import re

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "La Liga", partido: "Celta de Vigo vs Sevilla", fecha: "23 Mayo", pronostico: "Celta o Empate (1X)", cuota: "1.20", prob: "90%", explicacion: "Asimetría motivacional. Celta busca Europa en casa, mientras el Sevilla no se juega nada y promedia 2.40 goles en contra de visita." },
  { liga: "MLS", partido: "FC Cincinnati vs Orlando City", fecha: "23 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "85%", explicacion: "Sistemas defensivos inmaduros en la MLS. Cincinnati promedia marcadores altos (3-3, 3-2) y Orlando concede muchísimo." },
  { liga: "La Liga", partido: "Celta de Vigo vs Sevilla", fecha: "23 Mayo", pronostico: "Sevilla Más 2.5 Tarjetas", cuota: "1.55", prob: "83%", explicacion: "El Sevilla promedia 3.03 amonestaciones por partido, mostrando muchísima frustración defensiva como visitante." },
  { liga: "La Liga", partido: "Valencia vs Barcelona", fecha: "23 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.60", prob: "82%", explicacion: "Dominio de posesión del Barça (68%) empuja al rival a defender en su área, generando una altísima frecuencia de despejes laterales." },
  { liga: "Veikkausliiga", partido: "KuPS vs Lahti", fecha: "23 Mayo", pronostico: "KuPS Más 5.5 Córners", cuota: "1.50", prob: "81%", explicacion: "KuPS asfixia con posesión y disparos a puerta en casa, promediando una increíble cifra de 7.6 tiros de esquina a favor." },
  { liga: "La Liga", partido: "Girona vs Elche", fecha: "23 Mayo", pronostico: "Girona Anota (Más 0.5)", cuota: "1.12", prob: "85%", explicacion: "Girona promedia un xG de 1.53 en casa frente a un Elche con defensa frágil (1.60 goles en contra de visita)." },
  { liga: "La Liga", partido: "Celta de Vigo vs Sevilla", fecha: "23 Mayo", pronostico: "Celta Más 1.5 Tarjetas", cuota: "1.45", prob: "78%", explicacion: "Celta recurrirá a faltas tácticas para frenar el juego y asegurar su clasificación europea en casa." },
  { liga: "Ekstraklasa", partido: "Legia Varsovia vs Motor", fecha: "23 Mayo", pronostico: "Legia o Empate (1X)", cuota: "1.12", prob: "77%", explicacion: "Solidez del Legia en casa (0.75 goles encajados). Ideal para acumuladores de bajo riesgo." },
  { liga: "Serie A", partido: "Bologna vs Inter", fecha: "23 Mayo", pronostico: "Inter Más 4.5 Córners", cuota: "1.70", prob: "72%", explicacion: "Desdoblamiento constante de carrileros como Dimarco ante la presión alta de Italiano." },
  { liga: "MLS", partido: "Minnesota Utd vs RSL", fecha: "23 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.65", prob: "67%", explicacion: "Consistencia ofensiva de RSL y fragilidad de Minnesota generan un entorno ideal de BTTS." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 23.")
