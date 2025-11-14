# ...existing code...
try:
    score_confianza = float(input("Ingresa score de confianza (0-1): ").strip())
except ValueError:
    print("Entrada inválida. Usa un número.")
    raise SystemExit(0)

if not 0.0 <= score_confianza <= 1.0:
    print("El score debe estar entre 0 y 1.")
    raise SystemExit(1)

if score_confianza >= 0.9:
    print("Acción: Ejecutar automáticamente.")
elif score_confianza >= 0.7:
    print("Acción: Marcar para revisión humana.")
else:
    print("Acción: Descartar o reintentar análisis.")
# ...existing code...