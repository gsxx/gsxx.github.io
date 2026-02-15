#!/bin/bash

# Monitorea la carpeta 'roms' para detectar cambios en los archivos
inotifywait -m roms/ -e create -e moved_to -e delete -e moved_from |
    while read path action file; do
        echo "Archivo $file $action en $path"
        python3 generate_roms_list.py  # Ejecutar tu script para actualizar el archivo JSON
    done

