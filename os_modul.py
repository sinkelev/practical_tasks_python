import os


def files(path):
    """Получить список файлов в папке"""
    file = os.listdir(path)
    print(file)


def current_folder():
    """Получить текущую директорию"""
    print(os.getcwd())


def new_folder(path, name):
    """Создание папки. Первый аргумент путь, второй название папки."""
    os.chdir(path)
    if not os.path.isdir(name):
        os.mkdir(name)


def join_folder_and_filename(folder, filename):
    """
    Склеить путь из папки и файла.
    Первый аргумент папка, второй название файла.
    """

    print(os.path.join(folder, filename))


def calc():
    """Посчитать сколько в каталоге установки python файлов и папок."""
    folder = []
    py_count = 0
    exe_count = 0
    all_files = 0
    dirs_count = 0

    for i in os.walk('C:/Users/va.sinkelev/AppData/'
                     'Local/Programs/Python/Python39'):
        folder.append(i)

    for address, dirs, files in folder:
        dirs_count += 1
        for file in files:
            all_files += 1
            if file.endswith('.py'):
                py_count += 1
            elif file.endswith('.exe'):
                exe_count += 1

    f = open('python_dir.txt', 'w')
    try:
        f.write(f"Папок: {dirs_count}\n")
        f.write(f"Файлов .py: {py_count}\n")
        f.write(f"Файлов .exe: {exe_count}\n")
        f.write(f"Всего файлов: {all_files}\n")
    finally:
        f.close()


# files('C:\dev\\va.sinkelev\practical_tasks\\')
# current_folder()
# new_folder('C:\dev\\va.sinkelev\practical_tasks', 'test')
# join_folder_and_filename('\dev\\', 'file.txt')
# calc()
