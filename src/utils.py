"""utils.py — прості функції, які ми «експортуємо» в CLI через fire."""


def greet(name):
    """Повертає привітання для name."""
    return f"Привіт, {name}!"


def goodbye(name):
    """Повертає прощання для name."""
    return f"До побачення, {name}!"