try:
    tipo_evento = input("Ingresa tipo_evento: ").strip()
    es_premium = input("¿Es premium? (True/False): ").strip().lower() == "true"
    saldo_cuenta = float(input("Ingresa saldo_cuenta: ").strip())
except ValueError:
    print("Entrada inválida.")
    raise SystemExit(1)

if tipo_evento == "nuevo_usuario" and es_premium == False and saldo_cuenta == 120.50:
    print(True)
else:
    print(False)