"""sys_tool.py — сценарій, що працює тільки при прямому запуску з командного рядка.

Команди для запуску (Git Bash, з папки devops-sr3-cli):

python src/sys_tool.py
python src/sys_tool.py --help
python src/sys_tool.py hello world
python -c "import src.sys_tool"
"""
import sys

HELP_TEXT = """Використання: python src/sys_tool.py [--help] [аргументи...]

Друкує рядок «командна строка», якщо скрипт запущено напряму.
При імпорті як модуля (import src.sys_tool) нічого не друкує.

Опції:
  -h, --help   показати цю підказку
"""


def main(argv):
    """argv — список аргументів після назви скрипта (sys.argv[1:])."""
    if "-h" in argv or "--help" in argv:
        print(HELP_TEXT)
        return
    print("командна строка")
    if argv:
        print("Отримані аргументи:", " ".join(argv))


if __name__ == "__main__":
    main(sys.argv[1:])