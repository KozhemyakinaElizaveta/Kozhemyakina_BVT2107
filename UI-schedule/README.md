# UI-Schedule

### Libraries:

1. PyQt5
2. Psycopg2
3. requests

### Functions timetable.py:

* Удалить - delete records from database 
* Сохранить - add records to database 
* Изменить - update records

### Methods of the "MainWindow" class:

* _connect_to_db - connect to database "Schedule"
* datetime - add time in project
* _create_sсhedule_tab - create tab for selected day of week
* _create_one_day_table - create tabel
* _update_day_table - add rows from db and other update tabel
* _change_day_from_table - change rows in tabel
* _delete_row - delete row in tabel and db
