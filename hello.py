Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello,World")                      # "Hello, World"를 출력하는 코드입니다.
Hello,World
"Hello,World"                             # 큰 따옴표로 둘러싼 "Hello, World" 문자열입니다
'Hello,World'                             # 작은 따옴표로 둘러싼 "Hello, World" 문자열입니다
Hello,World                               # 변수를 정의하지 않고 "Hello"라는 변수를 사용하여 발생한 오류입니다.
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Hello,World                           # 문법적으로 올바르지 않은 "Hello World" 문자열입니다.
NameError: name 'Hello' is not defined
Hello World
SyntaxError: incomplete input
4+4                                       # 4와 4를 더하는 코드입니다.
8
해당 줄은 "Hello, World"를 출력하는 코드입니다. print() 함수를 사용하여 괄호 안에 있는 문자열을 화면에 출력합니다.이 줄은 주석이 아닌 문자열 그 자체입니다. 큰 따옴표로 둘러싸인 문자열은 파이썬에서 문자열로 취급됩니다.이 줄은 작은 따옴표로 둘러싸인 문자열입니다. 작은 따옴표로 둘러싸인 문자열도 파이썬에서 문자열로 취급됩니다.이 줄은 변수를 정의하지 않고 문자열을 그대로 사용하려고 했기 때문에 오류가 발생합니다. 변수를 사용하기 위해서는 변수를 정의해야 합니다.이 줄은 문법적으로 올바르지 않은 코드입니다. 파이썬은 문자열을 출력할 때에는 따옴표로 둘러싸야 합니다. 따라서 Hello World와 같이 따옴표로 둘러싸지 않은 문자열은 문법 오류(SyntaxError)가 발생합니다.해당 줄은 두 개의 숫자인 4와 4를 더하는 코드입니다. + 연산자를 사용하여 두 숫자를 더한 결과인 8이 출력됩니다.
