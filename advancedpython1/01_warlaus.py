from typing import List, Tuple, Dict, Union

n: int = 5
name: str = " Sarthak"


def sum(a: int, b: int) -> int:
    return a + b


print(sum(5, 6))

num: List[int] = [5, 10, 15, 20, 25]
numb: Dict[str, int] = {"Sarthak": 152006, "Unknown": 2006}
numb1: Dict[str, str] = {"Sarthak": "Patil", "Unknown": "2006"}
numbe: Tuple[str, int] = ("Sarthak", 15)
numbe1: Tuple[str, bool] = ("Sarthak", True)

print(num)
print(numb)
print(numb1)
print(numbe)
print(numbe1)

