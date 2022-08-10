
from dataclasses import dataclass


@dataclass
class Node:
    prev:str = None
    next:str = None

def solution(n, k, cmd):
    root = Node()

    answer = ""
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]    
result = solution(n, k, cmd)
answer = "OOOOXOOO"
print(f"result: {result}")
