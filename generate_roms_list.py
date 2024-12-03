
import os

# Carpeta de entrada y salida
roms_folder = './roms'
generated_html_folder = './generated_html'
welcome_page = './index.html'  # Este archivo será sobrescrito

# Asegúrate de que la carpeta de salida exista
if not os.path.exists(generated_html_folder):
    os.makedirs(generated_html_folder)

# Plantilla básica de HTML para los archivos de ROM
def rom_html_template(game_name):
    return f"""
<!DOCTYPE html>
<!-- copied from
https://github.com/chrismaltby/gb-studio/blob/v2beta/appData/js-emulator/index.html
(see LICENSE.gbstudio)
-->
<head>
  <meta charset="utf-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="simple.css">
  <title>binjgb (simple)</title>
</head>
<body>
  <div id="game">
    <canvas id="mainCanvas" width="160" height="144">No Canvas Support</canvas>
  </div>
  <div id="controller">
    <div id="controller_dpad">
      <div id="controller_left"></div>
      <div id="controller_right"></div>
      <div id="controller_up"></div>
      <div id="controller_down"></div>
    </div>
    <div id="controller_select" class="capsuleBtn">Select</div>
    <div id="controller_start" class="capsuleBtn">Start</div>
    <div id="controller_b" class="roundBtn">B</div>
    <div id="controller_a" class="roundBtn">A</div>
  </div>
  <script>
    const ROM_FILENAME = "../roms/"+"{game_name}"+".gb"
  </script>
  <script src="binjgb.js"></script>
  <script src="simple.js"></script>
</body>
"""

# Plantilla básica de la página de bienvenida
def welcome_page_template(buttons_html):
    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenida</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }}
        .button {{
            display: inline-block;
            padding: 20px 40px;
            margin: 10px;
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
        }}
        .button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>
<body>
    <h1>Bienvenido a la página de juegos</h1>
    <p>A continuación, puedes elegir un juego para jugar:</p>
    {buttons_html}
</body>
</html>
"""

# Leer los archivos de ROMs en la carpeta
def generate_html_files():
    rom_html_files = []
    buttons_html = []

    for file in os.listdir(roms_folder):
        # Filtrar solo archivos .gb
        if file.endswith('.gb'):
            game_name = os.path.splitext(file)[0]  # Nombre del juego sin la extensión
            output_html_path = os.path.join(generated_html_folder, f'{game_name}.html')

            # Generar el contenido del HTML para la ROM
            html_content = rom_html_template(game_name)
            with open(output_html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f'Archivo HTML generado para {game_name}')

            # Crear un botón para la página de bienvenida
            buttons_html.append(f'<a href="/generated_html/{game_name}.html" class="button">{game_name}</a>')

    # Generar la página de bienvenida con los botones
    welcome_page_content = welcome_page_template('\n'.join(buttons_html))
    with open(welcome_page, 'w', encoding='utf-8') as f:
        f.write(welcome_page_content)
    print('Página de bienvenida generada.')

# Ejecutar la generación de archivos HTML
generate_html_files()

