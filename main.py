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
print(f"Tiene {len(datos["telefonos"])} telefonos")

#Mengano no pertenece a nigún equipo
if(datos["equipo"]) == None:
    print(f"{datos["nombre"]} no pertenece a ningún equipo")

#Tiene 3 hermanos reales
print(f"Tiene {len(datos["hermanos"])} hermanos reales")

#Mengano a veces utiliza iPhone
print(f"{datos["nombre"]} a veces utiliza {datos["telefonos"][1]["modelo"]}")

#Mengano tiene posiblemente 2 hermanos
print(f"{datos["nombre"]} tiene posiblemente {len(datos["hermanos"])} hermanos")