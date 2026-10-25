"""fire_expose.py — відкриває функції з utils.py для командного рядка через fire."""
import fire

from utils import greet, goodbye

if __name__ == "__main__":
    # Словник: назва команди в CLI -> функція, яку вона викликає
    fire.Fire({
        "greet": greet,
        "goodbye": goodbye,
    })