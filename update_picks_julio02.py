import re

new_picks = """const PICKS_DATA = [
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Víkingur Reykjavík vs KA Akureyri',
    fecha: '2 de Julio, 2026',
    pronostico: '1X (Local o Empate)',
    cuota: '1.15',
    prob: 94,
    explicacion: 'El líder invicto acumula 34 puntos de 36 posibles en casa. KA Akureyri sufre debilidad posicional extrema con 5 derrotas en fila en liga regular.'
  },
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Thór Akureyri vs KR Reykjavík',
    fecha: '2 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.18',
    prob: 92,
    explicacion: 'KR Reykjavík es la escuadra más realizadora de la liga pero concede demasiados goles. Thór tiene la peor defensa del campeonato regular.'
  },
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Víkingur Reykjavík vs KA Akureyri',
    fecha: '2 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.20',
    prob: 90,
    explicacion: 'Altísima consistencia goleadora del local ante un visitante que ha encajado un promedio de 2.6 goles por encuentro en su reciente racha negativa.'
  },
  {
    liga: 'Ykkönen (Finlandia)',
    partido: 'FC Jazz vs KPV Kokkola',
    fecha: '2 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.22',
    prob: 90,
    explicacion: 'KPV Kokkola presenta una seria debilidad defensiva, acumulando 41 goles encajados en 11 partidos y recibiendo al menos 2 goles en el 82% de sus visitas.'
  },
  {
    liga: 'Ykkönen (Finlandia)',
    partido: 'FC Jazz vs KPV Kokkola',
    fecha: '2 de Julio, 2026',
    pronostico: '1X (Local o Empate)',
    cuota: '1.25',
    prob: 88,
    explicacion: 'KPV Kokkola atraviesa una espiral autodestructiva con 4 derrotas recientes. FC Jazz mantiene un orden táctico sólido cuando juega en su estadio.'
  },
  {
    liga: 'Vysshaya Liga (Bielorrusia)',
    partido: 'FC Minsk vs Dinamo Minsk',
    fecha: '2 de Julio, 2026',
    pronostico: 'X2 (Visitante o Empate)',
    cuota: '1.25',
    prob: 88,
    explicacion: 'Dinamo Minsk mantiene un registro invicto como visitante, mientras que FC Minsk ha cedido puntos en el 50% de sus compromisos como local.'
  },
  {
    liga: 'Premium Liiga (Estonia)',
    partido: 'FC Kuressaare vs Flora Tallinn',
    fecha: '2 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.20',
    prob: 88,
    explicacion: 'Flora Tallinn promedia 17.1 disparos por partido y necesita recortar puntos urgentemente, lo que propicia un esquema ofensivo de alta intensidad.'
  },
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Thór Akureyri vs KR Reykjavík',
    fecha: '2 de Julio, 2026',
    pronostico: 'X2 (Visitante o Empate)',
    cuota: '1.35',
    prob: 85,
    explicacion: 'Thór Akureyri cuenta con la defensa más frágil del campeonato regular, ofreciendo amplias oportunidades al potencial ultraofensivo del KR Reykjavík.'
  },
  {
    liga: 'Vysshaya Liga (Bielorrusia)',
    partido: 'BATE Borisov vs FK Gomel',
    fecha: '2 de Julio, 2026',
    pronostico: 'X2 (Visitante o Empate)',
    cuota: '1.45',
    prob: 78,
    explicacion: 'Omitiendo riesgos disciplinarios por variabilidad arbitral, el modelo detecta alto valor esperado a favor del visitante frente a un BATE inconsistente.'
  },
  {
    liga: 'Premium Liiga (Estonia)',
    partido: 'FC Kuressaare vs Flora Tallinn',
    fecha: '2 de Julio, 2026',
    pronostico: 'Más de 9.5 corners',
    cuota: '1.83',
    prob: 78,
    explicacion: 'Flora genera 7.5 saques de esquina por partido y Kuressaare aporta 5.4 mediante transiciones rápidas. Combinación ideal para superar la línea propuesta.'
  }
];"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'const PICKS_DATA = \[[^;]+\];'
new_content = re.sub(pattern, new_picks, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Picks updated successfully!")
