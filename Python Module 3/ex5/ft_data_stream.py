import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["ana", "bob", "charlie", "dylan"]
    actions = ["move", "grab", "use", "run",
               "climb", "release", "swim", "sleep", "eat"]
    while True:
        random_name = random.choice(names)
        random_action = random.choice(actions)
        tuple_event = (random_name, random_action)
        yield (tuple_event)


def consume_event(
    ten_tuple_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(ten_tuple_list) > 0:
        index_in_list = random.randrange(len(ten_tuple_list))
        event_to_remove = ten_tuple_list.pop(index_in_list)
        yield event_to_remove 


def main() -> None:
    gen = gen_event()
    ten_tuple_list: list[tuple[str, str]] = []
    for i in range(0, 1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    for i in range(10):
        event = next(gen)
        ten_tuple_list = ten_tuple_list + [event]
    print(f"Built list of 10 events: {ten_tuple_list}")
    for event_removed in consume_event(ten_tuple_list):
        print(f"Got event from list: {event_removed}")
        print(f"Remains in list: {ten_tuple_list}")


if __name__ == "__main__":
    main()
