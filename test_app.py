from app import add

'''
# assert
    - 코드의 특정 조건이 참(True)임을 '주장(assert)'하고 확인하는 구문
    - 조건이 거짓(False)일 경우 AssertionError를 발생시켜 프로그램 실행을 중단
'''
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, 1) == -1