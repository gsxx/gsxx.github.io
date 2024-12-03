import os
import json

# Ruta a la carpeta de ROMs
rom_folder = "roms"

# Lista de archivos en la carpeta roms que terminan con .gb (ROMs de Game Boy)
rom_files = [f for f in os.listdir(rom_folder) if f.endswith('.gb')]

# Crear el objeto JSON
roms_list = {"games": rom_files}

# Guardar el archivo roms-list.json
with open("roms-list.json", "w") as json_file:
    json.dump(roms_list, json_file, indent=4)

print("Archivo roms-list.json actualizado.")

