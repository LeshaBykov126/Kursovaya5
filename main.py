from DBManager import DBManager
from config import config
from hh_get_company import connect_vacancy
from work_with_BD import create_database, write_table

ID_COMPANY = [9498112, 3529, 78638, 2324020, 2000762, 1918903, 1579449, 873105, 80, 1049556, 3388]
params = config()
DB_class = DBManager(params)  # параметры файла database.ini

input(f'Чтобы загрузить вакансии кампаний по id {len(ID_COMPANY)} \n'
      'нажми enter')

print('Создаем базу данных и таблицы')
create_database()  # функция создание БД и создание таблиц

print('Загружаем БД')
for one_id in ID_COMPANY:
    vac_list = connect_vacancy(one_id)
    #  Вставить функцию заполнения БД
    write_table(vac_list, one_id)
    print('||||||||', vac_list['items'][0]['employer']['name'], '|||||||||||||||||||||||||||||||||||||||')
    count_vacancy = vac_list['found']
    print(f'Всего ваканcий {count_vacancy}, в БД добавленно до 100')

while True:
    user_call = input('Введи id компании\n'
                      '1 - список всех компаний и количество вакансий\n'
                      '2 - список вакансий, название компании, зп, ссылка на вакансию\n'
                      '3 - показать среднюю зп\n'
                      '4 - вакансии с зп выше среднего по всем вакансиям\n'
                      '5 - вакансии со словом python\n'
                      'Для выхода введи стоп\n')

    if user_call == '1':
        DB_class.get_companies_and_vacancies_count()

    elif user_call == '2':
        DB_class.get_all_vacancies()

    elif user_call == '3':
        DB_class.get_avg_salary()

    elif user_call == '4':
        DB_class.get_vacancies_with_higher_salary()

    elif user_call == '5':
        DB_class.get_vacancies_with_keyword()

    elif user_call == 'stop' or user_call == 'cnjg' or user_call == 'стоп':
        break

    else:
        print('Ошибка')
        input('Чтобы начать заново, нажми enter')
