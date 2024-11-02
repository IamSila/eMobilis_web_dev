"""annotations on variables"""
#how to declare the type of variable
age: int = 1
#you don't need to initialize a variable to annote it
age: int #ok




#####USEFUL BUILT-IN TYPES
x: int = 1
y: float = 1.0
z: bytes = b"test"


#for collections on python 3.9, the type of collections is in brackets
i: list[int] = [1]
j: set[int] = {3, 5}

#for mappings we need the types of both keys and values
h: dict[str, int]

#for tuples of fixed size, we specify the types of all elements
g: tuple[int, str, float]

#for tuples of variable types, we use one type and elipses
t: tuple[int, ...] = (1, 2, 3)

# On Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
from typing import List, Set, Dict, Tuple
x1: List[int] = [1]
x2: Set[int] = {6, 7}
x3: Dict[str, float] = {"field": 2.0}
x4: Tuple[int, str, float] = (3, "kenya", 7.6)
x5: Tuple[int, ...] = (1, 2, 3)

#on python 3.10+, use the | operator when something could be one of a few types
x6: list[int | str] = [3, 5, "test", "fun"]

#on earlier versions we can use Union
from typing import Union, Optional
t1: list[Union[int, str]] = [3, 5, "test", "fun"]

# Use X | None for a value that could be None on Python 3.10+
# Use Optional[X] on 3.9 and earlier; Optional[X] is the same as 'X | None'
t2: Optional[int] = 10


####FUNCTIONS
from collections.abc import Callable, Iterator
from typing import Union, Optional

#this is how you annote a function definition
def stringify(num: int) -> str:
    return str(num)
#and here is how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2
# If a function does not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)
# Note that arguments without a type are dynamically typed (treated as Any)
# and that functions without any annotations are not checked
def untyped(x):
    x.anything() + 1 + "string"  # no errors
#A generator function that yields ints is secretly just a function that
#returns an iterator of ints, so that's how we annote it
def gen(n: int) -> Iterator[int]:
    pass
#You can of course split function annotation over multiple lines
def send_email(
    address: str | list[str],
    sender: str,
    cc: list[str] | None,
    bcc: list[str] | None,
    subject: str = '',
    body: list[str] | None = None,
) -> bool:
    ...
#this says that each postional argument and each keyword argument is a "str"
def call(self, *args: str, **kwargs: str) -> str:
    pass


#####CLASSES
from typing import ClassVar

class BankAccount(object):
    #the __init__ method doesn't return anything so it gets
    #a return type of None just like any other method that doesn't return anything
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

        #for instance methods, omit types for "self"
        def deposit(self, amount: int) -> None:
            self.balance += amount
# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 400)
def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)
#You can use ClassVar annotations to declare class variables
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]


####When you’re puzzled or when things are complicated
#use any if you don't know the type of something or it's too dynamic to write a type fo
s: any =mystery_function()


####Standard "duck types"
from collections.abc import Mapping, MutableMapping, Sequence, Iterable
# or 'from typing import ...'(required in python 3.8)

#Use Iterable for generic iterables (anything usable in for)
# and a Sequence where a sequence (supporting "len" and "__getitem__") is required

def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]


#Mapping describes a dict-like object (with "__getitem__") that we won't 
#mutate, and MutableMapping one (with "__setitem__") that we might
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = 'maybe'  # mypy will complain about this line...
    return list(my_mapping.keys())

f({3: 'yes', 4: 'no'})

def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = 'maybe'  # ...but mypy is OK with this.
    return set(my_mapping.values())

f({3: 'yes', 4: 'no'})
