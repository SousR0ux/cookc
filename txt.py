import os

# Список файлов для обработки
file_names = ['1.txt', '2.txt', '3.txt']

# Данные для каждого файла: имя, количество строк и содержимое
files_data = []

# Считываем данные из каждого файла
for fname in file_names:
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        files_data.append((fname, len(lines), lines))

# Сортируем файлы по количеству строк
files_data.sort(key=lambda x: x[1])

# Создаем итоговый файл
with open('result.txt', 'w', encoding='utf-8') as out:
    for fname, count, lines in files_data:
        out.write(f"{fname}\n")
        out.write(f"{count}\n")
        for line in lines:
            out.write(f"{line}\n")

print("Объединение файлов завершено. Результат сохранен в result.txt.")
