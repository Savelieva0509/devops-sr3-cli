"""fire_expose.py — відкриває функції з utils.py для командного рядка через fire.

Команди для запуску (Git Bash, з папки devops-sr3-cli):

python src/fire_expose.py greet Alice
python src/fire_expose.py goodbye Bob
python src/fire_expose.py greet --name=Olena
python src/fire_expose.py --help
"""
import fire

from utils import greet, goodbye

if __name__ == "__main__":
    # Словник: назва команди в CLI -> функція, яку вона викликає
    fire.Fire({
        "greet": greet,
        "goodbye": goodbye,
    })