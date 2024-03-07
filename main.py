def suma(num_1: int, num_2: int) -> int:
    return num_1 + num_2

def resta(num_1: int, num_2: int) -> int:
    return num_1 - num_2

def gato(animal: str):
    if animal == 'cat':
        return True
    else:
        return False



if __name__ == "_main__":
    print(suma(num_1=5, num_2=10))
    print(resta(num_1=10, num_2=8))
    print(gato(animal= 'cat'))