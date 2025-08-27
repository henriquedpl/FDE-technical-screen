import re


def sort(width, height, length, mass):
    for dim in [width, height, length]:
        if re.search(r"^(\d)+(\.\d+)?(cm)?$", str(dim)) is None:
            raise ValueError(f"Unrecognized dimension: {dim}")
    if re.search(r"^(\d)+(\.\d+)?(kg)?$", str(mass)) is None:
        raise ValueError(f"Unrecognized mass: {mass}")

    width = float(str(width).replace("cm", ""))
    height = float(str(height).replace("cm", ""))
    length = float(str(length).replace("cm", ""))
    mass = float(str(mass).replace("kg", ""))

    if mass >= 20:
        is_heavy = True
    else:
        is_heavy = False

    is_bulky = False
    if (
        width >= 150 or height >= 150 or length >= 150
    ) or width * height * length >= 1_000_000:
        is_bulky = True

    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"


assert sort("100", 100.5, "150cm", "10kg") == "SPECIAL"
assert sort("100.80", 40.1, "0cm", "10kg") == "STANDARD"
assert sort("50", "50cm", "50.0cm", 40) == "SPECIAL"


try:
    sort("50", "50cm", "50.", 40)
    raised = False
except ValueError:
    raised = True
assert raised


try:
    sort("cm", "50cm", "1200km", 40)
    raised = False
except ValueError:
    raised = True
assert raised
