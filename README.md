# Альтаир — лаборатория прикладных вычислений

Демонстрационный репозиторий для проектного курса квантового программирования. Основная идея — изучать конкретные инструменты Python и переносить их в школьные проекты.

## Быстрый запуск (Windows, VS Code)

1. Распакуйте архив и откройте папку `altair-python-lab` через File → Open Folder.
2. Установите расширение Python (Microsoft), если его нет. Рекомендуется Python 3.11 или 3.12.
3. Откройте Terminal → New Terminal. Выполните:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe 01_environment/01_hello.py
```

Если Python 3.12 отсутствует, используйте `python -m venv .venv` при наличии совместимой версии Python. Активировать окружение необязательно: команды выше обращаются к интерпретатору напрямую. В VS Code выберите Python: Select Interpreter → `.venv`.

## Запуск примеров

```powershell
.\.venv\Scripts\python.exe 02_graphs/02_shortest_path.py
.\.venv\Scripts\python.exe 03_optimization/02_knapsack.py
.\.venv\Scripts\python.exe 04_quantum/04_topology.py
.\.venv\Scripts\python.exe 05_signals/02_fft.py
.\.venv\Scripts\python.exe -m streamlit run 06_web/app.py
```

Закрывайте окно Matplotlib, чтобы вернуть управление терминалу. Для остановки Streamlit нажмите Ctrl+C.

## Содержание

| Папка | Содержание |
|---|---|
| 01_environment | Интерпретатор, массивы, графики |
| 02_graphs | Граф, кратчайший путь, Дейкстра, обход всех точек |
| 03_optimization | Бинарные решения, рюкзак, MaxCut, QUBO |
| 04_quantum | Гейты, Белл, метрики, транспиляция, Гровер, шум, QAOA |
| 05_signals | Синусоида, FFT, признаки шумного сигнала |
| 06_web | Веб-маршрутизатор с отдельным engine.py и визуализатор кубита |
| 07_debugging | Отладчик, измерение времени и CSV |

План занятия: [TEACHER.md](TEACHER.md). Задания: [STUDENT.md](STUDENT.md). Статус проверки: [VERIFICATION.md](VERIFICATION.md).

## Проверка

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Если Qiskit недоступен, классические примеры можно установить отдельно:

```powershell
.\.venv\Scripts\python.exe -m pip install numpy matplotlib networkx
```

## Git (по желанию)

```powershell
git init
git add .
git commit -m "Initial Altair teaching lab"
```

Архив не является опубликованным GitHub-репозиторием; это готовая локальная структура. Не добавляйте `.venv` в Git. Все примеры учебные: не предполагают реального квантового ускорения или подключения к физическому квантовому компьютеру.
