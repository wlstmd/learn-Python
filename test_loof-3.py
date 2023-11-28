# 반복문으로 문제 풀어보기 3

while True:
    print("[메뉴를 입력하세요]")
    a = int(input("1. 게임시작 2.랭킹보기 3.게임종료>>>"))

    if a == 1:
        print("->게임을 시작합니다")
    elif a == 2:
        print("->랭킹보기")
    elif a == 3:
        print("->게임을 종료합니다")
        break
    else:
        print("다시 입력해 주세요")