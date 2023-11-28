# 조건문 2
price = int(input("삼성전자의 현재가격을 입력해주세요. >>> "))

if price >= 90000:
    print("매도 합니다.")
elif price >= 80000:
    print("대기중 입니다.")
else:
    print("매수합니다.")

# 응용해서 실습하기
# 합계금액 10만원 이상 할인률 30% 5 ~ 10만원 할인률 20% 5만원 미만 할인률 15%
bag_price = int(input("가방의 금액을 입력해주세요 >>> "))
watch_price = int(input("시계의 금액을 입력해주세요 >>> "))

total_price = bag_price + watch_price

if total_price >= 100000:
    total_price = total_price * 0.7
elif total_price >= 50000:
    total_price = total_price * 0.8
else:
    total_price = total_price * 0.9

print("합계금액은 : ", total_price)
