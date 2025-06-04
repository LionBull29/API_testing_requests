@echo off
REM Сначала переходим в папку проекта (где находится pytest.ini)
cd /d "%~dp0"

REM Создаем папку logs, если ее нет (относительно текущей папки)
if not exist logs mkdir logs

REM Запускаем тесты pytest с указанием конфигурационного файла и записью логов
pytest -v --color=yes --log-file=logs/test_results.log --log-level=INFO

REM Если нужно остановить выполнение при ошибке (один из тестов не прошел)
if %errorlevel% neq 0 (
  echo Один или несколько тестов не прошли!
  pause
  exit /b %errorlevel%
)

echo Все тесты прошли успешно!
pause