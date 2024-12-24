import os

# Путь к директории 'docs'
docs_dir = 'docs'

# Список HTML-файлов в папке 'docs'
html_files = ['main.html', 'utils.html', 'user_interface.html', 'difficulty_levels.html', 'game_logic.html']

# Создаем index.html с ссылками на другие файлы документации
with open(os.path.join(docs_dir, 'index.html'), 'w', encoding='utf-8') as index_file:
    index_file.write('<!DOCTYPE html>\n')
    index_file.write('<html lang="ru">\n')
    index_file.write('<head>\n')
    index_file.write('    <meta charset="UTF-8">\n')
    index_file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    index_file.write('    <title>Документация</title>\n')
    index_file.write('</head>\n')
    index_file.write('<body>\n')
    index_file.write('    <h1>Документация</h1>\n')
    index_file.write('    <ul>\n')

    # Добавляем ссылки на файлы
    for html_file in html_files:
        index_file.write(f'        <li><a href="{html_file}">{html_file}</a></li>\n')

    index_file.write('    </ul>\n')
    index_file.write('</body>\n')
    index_file.write('</html>\n')
