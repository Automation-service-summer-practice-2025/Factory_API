@echo off
:: Заголовок
cls
echo.
echo     Factory API — Скрипт управления контейнерами
echo     ---------------------------------------------
echo.

:: Меню
echo     [1] Запустить проект (docker-compose up)
echo     [2] Остановить проект (docker-compose down)
echo     [3] Проверить статус контейнеров
echo     [4] Пересобрать и запустить
echo     [5] Выход
echo.

:: Выбор действия
choice /C 12345 /M "Выберите действие:"

:: Обработка выбора
if errorlevel 5 goto exit
if errorlevel 4 goto rebuild
if errorlevel 3 goto status
if errorlevel 2 goto down
if errorlevel 1 goto up

:: Запуск контейнеров
:up
echo.
echo Запускаю контейнеры...
echo.
docker-compose up -d
goto end

:: Остановка и удаление контейнеров
:down
echo.
echo Останавливаю и удаляю контейнеры...
echo.
docker-compose down
goto end

:: Проверка статуса
:status
echo.
echo Проверяю статус контейнеров...
echo.
docker-compose ps
goto end

:: Пересборка и запуск
:rebuild
echo.
echo Пересобираю и запускаю проект...
echo.
docker-compose down --volumes
docker-compose build
docker-compose up -d
goto end

:: Выход
:exit
echo.
echo Выход...
exit

:: Конец
:end
echo.
pause