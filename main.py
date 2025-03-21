import json

datos = json.load(open("datos.json"))

#Mengano tiene 99 años
print(f"{datos["nombre"]} tiene {datos["edad"]} años")

#Mengano es conductor: True
print(f"{datos["nombre"]} es conductor: {datos["conductor"]}")

#Mengano tiene 3 coches
print(f"{datos["nombre"]} tiene {len(datos["coches"])}")

#Coches de Mengano:
print(f"Coches de {datos["nombre"]}:")
for coche in datos["coches"]:
    print(f"{coche}")
#Tiene 2 teléfonos
#Mengano no pertenece a nigún equipo
#Tiene 3 hermanos reales
#Mengano a veces utiliza iPhone
#Mengano tiene posiblemente 2 hermanos