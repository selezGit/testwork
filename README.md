# Test work

## Usage:


#### Install depencies:
```shell
pip install -r requirements.txt 
```

#### Set environmetns:

`SMTP_SERVER` - address your smtp email server

`SMTP_PORT` - your email server port (465 by default)

`EMAIL_LOGIN` - your login to enter the mail

`EMAIL_PASSWORD` - your password to enter the mail

<details><summary>Examples popular SMTP servers</summary><p>

![Screenshot](https://shorturl.at/hwFNV)
</p></details>

#### Run script:
```python
python3 main.py
```

#### Run tests:
```python
ENVIRONMENT='test' py.test
```

<details><summary>Task</summary>

Ниже описано тестовое задание, его необходимо выполнить с помощью средств Python и предоставить результат 20.08

Открыть https://www.moex.com Нажать на кнопку Меню, выбрать Срочный рынок, далее выбрать Индикативные курсы. В выпадающем списке выбирать валюты: USD/RUB - Доллар США к российскому рублю.

Когда откроется динамика курса, скопировать в excel курс за последний текущий месяц. В excel шапка (A) Дата, (B) Курс, (C)Изменение. Повторить для Евро (EUR/RUB - Евро к российскому рублю), записать в ячейки (D), (E), (F) дату евро, курс, изменение. Для каждой строки полученного файла поделить курс евро на доллар и полученное значение записать в ячейку (G). Выровнять – автоширина. Формат чисел – финансовый. Проверить, чтобы автосумма в excel опознавала ячейки как числовой формат. Послать итоговый файл отчета себе на почту. В письме указать количество строк в excel в правильном склонении. Код выложите на GitHub, или архивом в облачное хранилище (Google Drive, Yandex Disk и т.д.) и пришлите ссылку.

</details>
