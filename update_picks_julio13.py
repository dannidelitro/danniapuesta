import re

new_picks = """const PICKS_DATA = [
  {
    liga: 'Allsvenskan (Suecia)',
    partido: 'Djurgården vs Halmstad',
    fecha: '13 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.18',
    prob: 88,
    explicacion: 'Djurgården promedia alto volumen de ataque (56% posesión), mientras que Halmstad sufre la baja clave de su lateral derecho titular por sanción.'
  },
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Breidablik vs Keflavik',
    fecha: '13 de Julio, 2026',
    pronostico: 'Más de 1.5 goles',
    cuota: '1.20',
    prob: 87,
    explicacion: 'Partido de alto volumen ofensivo. Breidablik promedia 2.46 goles a favor y 1.92 en contra en casa. Keflavik encaja 1.85 como visitante.'
  },
  {
    liga: 'Primera Nacional (Argentina)',
    partido: 'Atlanta vs Colegiales',
    fecha: '13 de Julio, 2026',
    pronostico: '1X (Local o Empate)',
    cuota: '1.25',
    prob: 85,
    explicacion: 'Atlanta registra un índice de imbatibilidad del 75% en su estadio. Colegiales sufre severa ineficiencia como visitante (0% de victorias).'
  },
  {
    liga: 'Allsvenskan (Suecia)',
    partido: 'Djurgården vs Halmstad',
    fecha: '13 de Julio, 2026',
    pronostico: 'Gana Local',
    cuota: '1.30',
    prob: 84,
    explicacion: 'El absoluto dominio de posesión de Djurgården y la vulnerabilidad en las transiciones de un Halmstad mermado por sanciones consolidan la victoria.'
  },
  {
    liga: 'Besta deildin (Islandia)',
    partido: 'Breidablik vs Keflavik',
    fecha: '13 de Julio, 2026',
    pronostico: 'Ambos equipos marcan (BTTS)',
    cuota: '1.45',
    prob: 81,
    explicacion: 'Alta vulnerabilidad defensiva de Breidablik, que a pesar de su poderío ofensivo, solo mantiene su portería a cero en el 20% de sus partidos locales.'
  },
  {
    liga: 'Serie B (Brasil)',
    partido: 'Ceará vs Athletic Club',
    fecha: '13 de Julio, 2026',
    pronostico: 'Menos de 2.5 goles',
    cuota: '1.58',
    prob: 80,
    explicacion: 'Fuerte tendencia de bajo volumen ofensivo en enfrentamientos trabados de la liga brasileña, respaldado por un 80% de probabilidad modelada.'
  },
  {
    liga: 'Russian First League (Rusia)',
    partido: 'Chelyabinsk vs SKA Khabarovsk',
    fecha: '13 de Julio, 2026',
    pronostico: 'Más de 3.5 tarjetas',
    cuota: '1.65',
    prob: 80,
    explicacion: 'Chelyabinsk promedia un estilo defensivo muy agresivo que fuerza amonestaciones recurrentes (más de 1.5 tarjetas en el 80% de sus compromisos).'
  },
  {
    liga: 'Segunda División (Uruguay)',
    partido: 'La Luz vs Tacuarembó',
    fecha: '13 de Julio, 2026',
    pronostico: 'Menos de 2.5 goles',
    cuota: '1.50',
    prob: 79,
    explicacion: 'Encuentro entre dos de los ataques menos productivos (0.60 goles de media). El 85% del historial de La Luz local ha sido por debajo de la línea.'
  },
  {
    liga: 'Serie B (Brasil)',
    partido: 'América MG vs Londrina',
    fecha: '13 de Julio, 2026',
    pronostico: 'X2 (Visitante o Empate)',
    cuota: '1.67',
    prob: 77,
    explicacion: 'Ineficiencia masiva de mercado: América MG es favorito por nombre pero va último (6 puntos). Londrina (18 ptos) viene al alza tras golear 5-0.'
  }
];"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'const PICKS_DATA = \[[^;]+\];'
new_content = re.sub(pattern, new_picks, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Picks updated successfully!")
