Tarea: filtro_hackathon.py
edad: int = int(input("Ingresa tu edad: "))
lenguaje_favorito: str = input("Lenguaje favorito (Python/JavaScript/Otro): ").lower()
tiene_experiencia_defi: bool = input("¿Tienes experiencia en DeFi? (si/no): ").lower() == 'si' 

# ...existing code...

if edad > 18 and lenguaje_favorito == "python" and tiene_experiencia_defi:
    print(True)
else:
    print(False)

# ...existing code...