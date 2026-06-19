import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        calc = end - start
        print(f"Spell completed in {calc:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    print("Testing spell timer...")
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable | str:
            power = args[-1]  # Last argument
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(50)
def ice_ray(power: int) -> str:
    return "Ice ray cast!"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable | str:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f"Spell failed, retrying..."
                          f" (attempt {attempt}/{max_attempts})")
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def unstable_spell():
    raise Exception()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for character in name:
                if not character.isalpha() and not character.isspace():
                    return False
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    result = fireball()
    print(f"Result: {result}")
    print()
    print(ice_ray(50))
    print()
    print(unstable_spell())
    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
