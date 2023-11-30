# 10명의 성적을 입력 받아 평균을 내는 프로그램을 만든다
# 반복문과 조건문을 사용한다
# 변수는 total, counter, grade, average

total =  0          # 변수 total을 0으로 선언
counter = 1             # 변수 counter는 1로 선언
while counter  <= 10 :      # 반복문 wilhe을 사용하여 counter가 10보다 작거나 같을때 다음 내부문장으로 넘어간다
    grade = int(input("성적을 입력하시오. : "))         #변수 grade에 int(정수형 변환)와 사용자로부터 입력을 받는 input을 사용하여 점수를 받는다
    total = grade+total             # 변수 total에 성적 grade와 total을 합한 값을 선언
    counter = counter + 1           # 변수 counter는 초기 선언한 counter의 값에 실행할때마다 1씩 추가된다
average = total/10          # 변수 average에 반복문에서 계산한 total 값을 10으로 나눈다
print(average)          #평균값을 출력

#write by 이가예
주어진 코드는 10명의 성적을 입력받아 평균을 내는 프로그램입니다. 먼저 total이라는 변수를 0으로 초기화하고, counter라는 변수를 1로 초기화합니다. total은 성적의 총합을 저장하는 변수이고, counter는 입력받은 성적의 개수를 세는 변수입니다.위의 코드는 while 반복문을 사용하여 성적을 10번 입력받습니다. grade 변수에 input() 함수를 사용하여 사용자로부터 성적을 입력받습니다. 입력받은 성적은 total 변수에 더해져 누적됩니다. 그리고 counter 변수를 1 증가시켜 다음 성적을 입력받을 수 있도록 합니다.마지막으로, 입력받은 성적의 총합인 total을 10으로 나누어 평균을 계산하고, 이를 average 변수에 저장합니다. 그리고 print() 함수를 사용하여 평균값을 출력합니다.이렇게 주어진 코드는 반복문과 조건문을 사용하여 10명의 성적을 입력받고, 평균을 계산하여 출력하는 프로그램입니다.
