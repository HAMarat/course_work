# Дипломная работа

Для начала работы скопируйте репозиторий на локальную машину: с помощью команды в терминале

- [course_work](https://github.com/HAMarat/course_work.git)

Откройте склонированный репозиторий в PyCharm.

## Cоздайте виртуальное окружение:
Простой вариант:
- Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом. В этом случае после открытия папки с проектом в PyCharm появляется всплывающее окно, Creating virtual environment c тремя полями. В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv в корне проекта Во втором поле выбираем устанавливаемый интерпритатор по умолчанию (можно оставить без изменений) В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt, находящийся в корне папки проекта)

Если этого не произошло, тогда следует выполнить следующие действия вручную:
Установка виртуального окружения:
- Во вкладке File выберите пункт Settings
- В открывшемся окне, с левой стороны найдите вкладку с именем вашего репозитория (Project: task_27)
- В выбранной вкладке откройте настройку Python Interpreter
- В открывшейся настройке кликните на значок ⚙ (шестеренки) расположенный сверху справа и выберите опцию Add
- В открывшемся окне слева выберите Virtualenv Environment, а справа выберите New Environment и нажмите ОК

- активация виртуального окружения:
  - `venv\Scripts\activate (Windows)`
  
- установка DRF:
  - `pip install djangorestframework`

- установка Simple JWT:
  - `pip install djangorestframework-simplejwt`

- создание django приложения
  - `python .\manage.py startapp [app_name]`

- создать миграции 
  - `python .\manage.py makemigrations`

- применить миграции
  - `python .\manage.py migrete`

- показать примененные миграции
  - `python .\manage.py showmigrations`

- создание админа (суперпользователя)
  - `python .\manage.py createsuperuser`
  
## Создание и запуск контейнера docker с postgres

- Запустите создание и запуск контейнера командой `docker-compose up -d` 
  - `docker-compose up` - создание и запуск контейнера
  - `-d` - запуск контейнера в качестве отдельного процесса


## Цели проекта

Код написан в учебных целях — это дипломная работа в курсе по Python [Skypro](https://sky.pro).