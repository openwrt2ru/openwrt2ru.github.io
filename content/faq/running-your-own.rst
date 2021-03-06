Как сгенерить HTML на своем компьютере
######################################

:author: dim
:date: 2014-12-01 23:41
:slug: running-your-own

Процедура сборки HTML страниц сайта на своем компьютере очень проста.

**ВНИМАНИЕ!** *Пока что описываемый процесс подходит только для Linux.*

Итак, по шагам.

1.	Выписать локально репозиторий:

.. code-block:: console

	$ git clone https://github.com/openwrt2ru/openwrt2ru.github.io
..

2.	Установить pip:

.. code-block:: console

	$ sudo apt-get install pip
..

3.	Зайти в каталог репозитория и собрать virtualenv:

.. code-block:: console

	$ make venv
..

4.	Подредактировать нужные страницы сайта (в ветке content). Разумеется, если хотим просто сгенерить локально HTML то этот шаг можно пропустить.

5.	Запустить локальный сервер:

.. code-block:: console

	$ make serve
..

6.	Открыть http://127.0.0.1:8000 и посмотреть что получилось.

7.	Остановить сервер можно просто нажав <Ctrl>-C в консоли, где он был запущен.
