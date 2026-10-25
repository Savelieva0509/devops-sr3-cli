# Самостійна робота 3 — CLI-інструменти на Python

Набір невеликих утиліт командного рядка, що демонструє три підходи:

1. **sys_tool.py** — базовий запуск сценарію та `sys.argv`;
2. **click_tool.py** — утиліта на бібліотеці `click`;
3. **fire_expose.py** — «миттєвий» інтерфейс через бібліотеку `fire`.

## Структура

```
devops-sr3-cli/
├── src/
│   ├── __init__.py
│   ├── sys_tool.py
│   ├── click_tool.py
│   ├── utils.py
│   └── fire_expose.py
├── requirements.txt
└── README.md
```

## Встановлення

```bash
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash)
python -m pip install -r requirements.txt
```

На Windows у Git Bash для коректної кирилиці у виводі:

```bash
export PYTHONUTF8=1
```

## 1. sys_tool.py

Друкує «командна строка» тільки при прямому запуску. При імпорті як модуля нічого не друкує
(перевірка `if __name__ == "__main__":`).

```bash
python src/sys_tool.py              # командна строка
python src/sys_tool.py --help       # підказка
python src/sys_tool.py hello world  # командна строка + Отримані аргументи: hello world
python -c "import src.sys_tool"     # нічого не друкує
```

## 2. click_tool.py

Команда `say` з обов'язковою опцією `--name`. Виводить ім'я, якщо воно не починається з літери p/P,
інакше — повідомлення про відмову. Довідку `--help` click генерує автоматично.

```bash
python src/click_tool.py --help
python src/click_tool.py say --help
python src/click_tool.py say --name Alice   # Alice
python src/click_tool.py say --name peter   # Ім'я «peter» не підходить: воно починається з літери P.
```

## 3. fire_expose.py

Функції `greet(name)` і `goodbye(name)` з `src/utils.py` відкриті для командного рядка через
`fire.Fire(...)` без ручного розбору аргументів.

```bash
python src/fire_expose.py greet Alice          # Привіт, Alice!
python src/fire_expose.py goodbye Bob          # До побачення, Bob!
python src/fire_expose.py greet --name=Olena   # Привіт, Olena!
python src/fire_expose.py --help               # список команд
python src/fire_expose.py greet --help         # довідка по команді
```

## Автор

Людмила Бабенко