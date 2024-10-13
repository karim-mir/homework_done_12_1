# Функция *def load_transactions*

Этот проект предназначен для загрузки и обработки финансовых транзакций из JSON-файлов. Он предоставляет функцию для извлечения данных и проверки их валидности.

## Описание

Функция *load_transactions* принимает путь к JSON-файлу и возвращает список валидных транзакций. Загруженные данные должны быть в формате списка словарей. Функция выполняет следующие проверки:
- Существует ли указанный файл.
- Не повреждён ли файл и правильно ли он отформатирован в JSON.
- Являются ли загруженные данные списком и содержат ли требуемые поля.

Логирование настроено для отслеживания процесса загрузки и обработки данных.

## Установка

Для работы проекта необходимы следующие пакеты:

- json - встроенная библиотека Python.
- logging - встроенная библиотека Python.
- unittest - встроенная библиотека для тестирования.

1. Клонируйте репозиторий:
```
git clone [URL_РЕПОЗИТОРИЯ]   cd [ИМЯ_ПАПКИ С_КОДОМ]
```

2. Убедитесь, что у вас установлен Python

3. Создайте файл *operations.json* в модуле *data* с данными о транзакциях.
Формат данных может выглядеть следующим образом:
```
[
{"id": 1, "amount": 100.50, "currency_name": "USD", "currency_code": "USD", "from": "Alice", "to": "Bob", "description": "Payment for services"},
{"id": 2, "amount": 200.00, "currency_name": "EUR", "currency_code": "EUR", "from": "Charlie", "to": "Dave", "description": "Refund"}
]
```
4. Запустите скрипт:
```
python [ИМЯ_СКРИПТА].py
```

## Использование

1. Измените путь в переменной *path* в коде на путь к вашему JSON-файлу.
2. Запустите скрипт.

Пример:
```commandline
if __name__ == "__main__":
transactions = load_transactions("data/operations.json")
print("Полученные транзакции:", transactions)
```
## Логирование

Все события, происходящие во время выполнения скрипта, записываются в файл *logs.log*. В этом файле будут подробно описаны:

- Статусы загрузки.
- Ошибки и исключения, если они возникнут.

## Тестирование

Для тестирования функции *load_transactions* используется библиотека *unittest*
Тесты проверяют различные сценарии, включая:
- Успешную загрузку с корректными данными.
- Обработку ситуации, когда файл не существует.
- Обработку некорректного JSON.
- Обработку данных, не являющихся списком.
- Обработку пустых файлов.
- Проверку на корректность типов данных полей *id* и *amount*

### Запуск тестов

Для запуска тестов выполните следующий команду:
```
python -m unittest discover -s tests
```
Убедитесь, что тесты находятся в каталоге *tests*, а код находится в *src*

# Функция *convert_to_rub* 

Этот проект включает в себя функциональность для конвертации валют в рубли (RUB) с использованием *API* для получения курсов валют. Проект написан на *Python* и включает тестирование для обеспечения надежности функций.

## Установка

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/ваш_репозиторий.git
```
2. Создайте и активируйте виртуальное окружение:
```commandline
python -m venv venv
```
*для Linux/Mac*
```commandline
source venv/bin/activate 
```
*для Windows*
```commandline
venv\Scripts\activate
```
3. Установите необходимые зависимости:
```
pip install -r requirements
```
4. Создайте файл *.env* в корневом каталоге проекта и добавьте ваш *API* ключ:
```commandline
EXCHANGE_API_KEY=ваш_ключ_api
```

## Использование
Для конвертации суммы в рубли вы можете использовать функцию *convert_to_rub*.

Вот пример:
```commandline
from src.external_api import convert_to_rub

rub = convert_to_rub(100, "USD")
print(f"Сумма в рублях: {rub}")
```

## Тестирование
Проект включает тесты для проверки функциональности. Тесты написаны с использованием *unittest*.

Чтобы запустить тесты, выполните:
```commandline
python -m unittest discover -s tests
```
### Тестируемые функции

*test_convert_to_rub_success*: - Проверяет успешный сценарий конвертации валюты.

*test_convert_to_rub_failed_request*: - Проверяет поведение функции при ошибке *API*. 

*test_convert_to_rub_with_rub*: - Проверяет конвертацию суммы в рублях.

# Функция *get_financial_transactions* 

## Описание

Этот проект предназначен для чтения финансовых транзакций из *CSV* файла и их обработки. Он включает функцию, которая загружает транзакции, а также набор тестов для проверки правильности функционирования этой функции.

## Установка

Выполните следующие команды для установки необходимых модулей:
```commandline
pip install -r requirements
```

### Чтение транзакций из CSV

Чтобы использовать функцию *get_financial_transactions* для чтения данных из CSV-файла, выполните следующий код:
```commandline
from src.transactions_csv import get_financial_transactions
path = "transactions.csv"  # Путь к вашему CSV файлу 
transactions = get_financial_transactions(path)
print(transactions)
```
Функция *get_financial_transactions* принимает путь к CSV файлу в качестве аргумента и возвращает список транзакций в виде словарей. Каждая транзакция включает такие поля, как *id*, *state*, *date*, *amount*, *currency_name*, *currency_code*, *from*, *to* и *description*.

### Формат *CSV* файла

*CSV* файл должен следовать следующему формату, с разделителем ";" :
```commandline
id;state;date;amount;currency_name;currency_code;from;to;description
complete;2023-01-01;100;USD;USD;Alice;Bob;Payment
pending;2023-02-01;200;EUR;EUR;Alice;Charlie;Transfer
```
### Запуск

Вы можете запустить скрипт, который будет читать транзакции из файла, выполнив:
```commandline
python src/transactions_csv.py
```
Где *transactions_csv.py* — это файл, содержащий вашу функцию.

## Тестирование

В проекте также предусмотрены тесты для проверки работы функции *get_financial_transactions*. Тесты написаны с использованием библиотеки *unittest*.

### Запуск тестов

Чтобы запустить тесты, выполните следующую команду:
```commandline
python -m unittest discover
```
Или просто запустите тестовый файл, например:
```commandline
python src/test_transactions_csv.py
```

## Пример тестов

В тестах используется mock для имитации чтения *CSV* файла. Вот пример теста:
```commandline
@patch("builtins.open", new_callable=mock_open, read_data="id;state;date;amount;currency_name;currency_code;from;to;description;complete;2023-01-01;100;USD;USD;Alice;Bob;Payment")
def test_get_financial_transactions(self, mock_open):
```

# Функция *get_financial_transactions_operations* 

## Описание

Данный проект предназначен для работы с финансовыми транзакциями, которые хранятся в файле Excel. В проекте реализована функция для чтения транзакционных данных и представления их в виде списка словарей. Также предусмотрены тесты для проверки функциональности.

## Установка

1. Склонируйте репозиторий на локальную машину:
```commandline
git clone url_репозитория
```
2. Перейдите в каталог проекта:
```commandline
cd имя_каталога
```
3. Установите необходимые зависимости:
```commandline
pip install pandas openpyxl unittest
```
## Использование

Функция *get_financial_transactions_operations* выполняет следующие действия:

- Читает файл *Excel*, путь к которому передается в качестве аргумента.
- Извлекает данные из файла и преобразует каждую строку в словарь.
- Возвращает список словарей, где каждый словарь представляет собой транзакцию.

#### Параметры:

- path: строка, указывающая путь к файлу *Excel*.

#### Пример вызова:
*Не забудьте заменить *path* на свой путь, где находится ваш файл Excel*
```commandline
if __name__ == "__main__":
path = "C:/Users/zheba/AppData/Local/Programs/Python/Python312/homework_done_12_1/src/transactions_excel.xlsx"
operations = get_financial_transactions_operations(path)
print(operations)
```
### Тестирование

Тесты для функции *get_financial_transactions_operations* реализованы с помощью фреймворка *unittest*. Используются моки для имитации чтения данных из *Excel* и проверки работоспособности функции.

#### Запуск тестов

Чтобы запустить тесты, выполните команду:
```commandline
python -m unittest discover -s tests
```
Структура тестов:

- *test_get_financial_transactions_operations*: тестирует правильность обработки не пустого файла с транзакциями.
- *test_get_financial_transactions_operations_empty*: проверяет поведение функции при отсутствии данных.

## Логирование

В коде используется базовое логирование с помощью модуля *logging*, что позволяет отслеживать процесс выполнения функции и выявлять возможные ошибки при работе с файлами и данными.
