openwrt2ru.github.io
====================

For local build

Установка для win машины:

### Установка Python

Скачиваем дистрибутив Python: https://www.python.org/downloads/
(тестировалось под 2.7)

Установить менеджер пакетов `pip` или `easy_install`.

### Установка easy_install

Информация https://pypi.python.org/pypi/setuptools#windows-simplified

* скачиваем файл https://bootstrap.pypa.io/ez_setup.py
* запускаем `python ez_setup.py`

#### Установка pelican через easy_install

    easy_install pelican

### Установка pip

Информация http://pip.readthedocs.org/en/latest/installing.html#install-pip

* скачиваем файл https://bootstrap.pypa.io/get-pip.py
* запускаем "python get-pip.py"

#### Установка pelican через pip

    pip pelican

#### Установка плагина "vimeo" для pelican

    pip install pelican-vimeo

#### Получение исходного кода сайта

Склонировать этот репозиторий

    git clone git@github.com:openwrt2ru/openwrt2ru.github.io.git
    
Или скачать zip архив со страницы github

#### Генерация статических страниц

Запускаем консольную команду:

    _generate.bat

Файлы создаются в папке `output`.

#### Запуск веб-сервера

Для просмотра страниц запускаем веб-сервер:

    _start_server.bat

(можно поправить в bat-файле PYTHON_EXE - на python.ext)

#### Просмотр результата

Открываем в браузере `http://localhost:8000`