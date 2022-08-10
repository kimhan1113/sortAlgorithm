
from dataclasses import dataclass


if "b" < "a":
    print("대수비교")


@dataclass
class test:

    b: int


c = test(b=1)
print(c)
