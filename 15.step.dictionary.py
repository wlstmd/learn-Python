# 파이썬 딕셔너리 배워보기
play_data = {  # 딕셔너리는 리스트랑 비슷 하게 여러 값을 저장 하지만 key : value 형태를 갖고 여러 값을 저장 한다
    'result': 'win',
    'champ_name': '비에고',
    'kill': 13,
    'death': 9,
    'assist': 13
}

print(play_data['result'])

# 기존 값 변경
play_data['result'] = 'lose'

# 새로운 키, 값 추가
play_data['level'] = 18

# 데이터 삭제
del play_data['champ_name']

# 딕셔너리 관련 함수

# keys() 키 이름 가져오기
for key in play_data.keys():
    print(key)

# values() 키의 값 가져오기
for value in play_data.values():
    print(value)

# items() 둘다 가져오기
for key, value in play_data.items():
    print(key, value)
