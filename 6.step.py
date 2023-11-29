# 리스트 생성하기

# 리스트 여러 값을 입력받기 위해 사용한다 변수로만 처리한다면 변수가 여러개 필요하지만 리스트를 사용하면 리스트 하나로 여러값을 저장한다
animals = ["사자", "호랑이", "고양이", "강아지"]

# 데이터 접근하기
name = animals[3]

# 데이터 추가하기
animals.append("하마")  # append()함수는 리스트 맨 끝에 값을 저장하는 역할을 한다
animals.append(1)

#데이터 삭제하기
del animals[-1]  # del 함수는 삭제를 담당한다

# 리스트 슬라이싱
slicing = animals[1:3]  # 슬라이싱함수는 값을 자르는데 사용한다 예제를 보면 1부터 3보다 작을때까지 자르고있다

# 리스트 길이
length = len(animals)  # len함수는 리스트의 길이를 반환하는 역할을 한다

# 리스트 정렬
animals.sort(reverse=True)  # sort함수는 정렬을 담당하는 함수이다

print(animals)