from itertools import product


low = "test "
up = low.upper()
m = zip(low, up)


db_enabled = False
aiohttp_enabled = False
prefix = set("".join(m) for m in product(*m))
