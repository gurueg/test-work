"""
  + проще в понимании
  - медленнее
"""
# def isEven(value: int) -> bool:
#     return value%2 == 0

"""
 + работает быстрее
"""
def isEven(value: int) -> bool:
    return value&1 == 0


def main():
    print isEven(1)
    print isEven(2)


if __name__ == "__main__":
    main()