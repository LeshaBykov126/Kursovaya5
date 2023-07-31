from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    """ сбор параметров из файла database """
    parser = ConfigParser()
    parser.read(filename)
    db = {}  # создание словаря
    if parser.has_section(section):  # заполнение параметров
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db  # возвращаем словарь параметров
