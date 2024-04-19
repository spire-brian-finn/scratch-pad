from typing import Any, cast, Dict

foo: Dict[str, int] = {}
# ohhhh cast is not side-effecting. I can't just cast or foo = cast(something, foo) - I need a new var
bar = cast(Dict[str, Any], foo)
bar["yee"] = {"haw": "buddy"}