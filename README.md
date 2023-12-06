# Возраст из ИИН
Тестовое задание: Сервис позволяет высчитать возраст по введённому ИИН

## Технологии

- Python 3.10
- Django REST framework

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:SowaSova/iin_to_age.git
```
Войти в папку проекта

```
cd iin_to_age/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в каталог

```
cd iin_to_age/
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
