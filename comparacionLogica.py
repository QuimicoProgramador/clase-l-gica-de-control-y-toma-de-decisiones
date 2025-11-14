# ...existing code...
try:
    a = float(input("Ingresa A: ").strip())
    b = float(input("Ingresa B: ").strip())
except ValueError:
    print("Entrada inválida. Usa números.")
    raise SystemExit(1)

while True:
    try:
        c = float(input("Ingresa C: ").strip())
    except ValueError:
        print()
        continue

    resultado = a + b - c
    if resultado >= 10:
        print(True)
        break
    else:
        print(False)
        # se vuelve a preguntar el valor de C
# ...existing code...
# filepath: c:\Users\Sergioi\Documents\GitHub\clase-l-gica-de-control-y-toma-de-decisiones\comparacionLogica.py
# ...existing code...