#this is the test file 

test = True

if not test:
    print("the test is not true!!!")
else:
    print('hi')

#new line 


'''new lines '''

'''new new '''


class costumer():
    def __init__(self) -> None:
        pass 

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __getattribute__(self, __name: str) -> Any:
        pass


class product():
    def __init__(self) -> None:
        pass

    def __new__(cls: type[Self]) -> Self:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __str__(self) -> str:
        pass

    