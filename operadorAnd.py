try:
    tipo_evento = input("Ingresa tipo_evento: ").strip()
    saldo_cuenta = float(input("Ingresa saldo_cuenta: ").strip())
except ValueError:
    print("Entrada inválida.")
    raise SystemExit(1)

if tipo_evento == "nuevo_usuario" and saldo_cuenta > 100.00:
    print("✅ Enviar Email 1: ¡Bienvenido y Gracias por tu depósito!")
else:
    print("❌ Condición de email de bienvenida no cumplida.")