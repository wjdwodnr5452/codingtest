# 코팅테스트 정리
- 해당 정리 글은 강의 이코테 2021 강의를 보고 정리 한 것입니다.
- 출처 : 이코테 2021 강의

##### 복잡도는 알고리즘의 성능을 나타내느 척도
- 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
- 공간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 메모리 사용량 분석

##### 시간제한이 1초인 문제를 만났을 때
- N의 범위가 500인 경우 : 시간 복잡도가 O(N3)인 알고리즘 설계
- N의 범위가 2,000인 경우 : 시간 복잡도가 O(N2)인 알고리즘 설계
- N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘 설계
- N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계

##### 일반적인 알고리즘 문제 해결 과정
1. 지문 읽기 및 컴퓨터적 사고
2. 요구사항(복잡도) 분석
3. 문제 해결을 위한 아이디어 찾기
4. 소스코드 설계 및 코딩

##### 자료형
- 파이썬의 자료형으로는 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전 등이 있다
  - 파이썬의 자료형은 필수적으로 알아 두어야 한다.

##### 정수형
 - 정수를 다루는 자료형
   - 양의 정수, 음의 정수, 0의 포함

##### 실수형 
- 실수형은 소수점 아래의 데이터를 포함하는 수 자료형
  - 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리
  - 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성 가능
- 파이썬에서는 e나 E를 이용한 지수 표현 방식을 이용 가능
  - 예를 들어 1e9라고 입력하게 되면 10의 9제곱이 된다.
- 실수형을 저장하기 위해 4바이트, 혹은 8바이트의 고정된 크기의 메모리를 할당하므로, 컴퓨터 시스템은 실수 정보를 표현하는 정확에 한계를 가진다.
  - 예를 들어 10진수 체계에서는 0.3과 0.6을 더한 값이 0.9로 정확이 떨어진다.
    - 하지만 2진수에서는 0.9를 정확히 표현할 수 있는 방법이 없다.
- 개발 과정에서 실수 값을 제대로 비교하지 못해서 원하는 결과를 얻지 못해서 round() 함수를 이용 하면 된다.
   
##### 수 자료형의 연산
- 수 자료형에 대하여 사칙연산과 나머지 연산자가 많이 사용된다.
- 나누기 연산자(/)를 주의해서 사용해야 한다.
   - 파이썬에서 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환한다.
- 다양한 로직을 설계할 때 나머지 연산자(%)를 이용해야 할 때가 많다.
   - 예시 : a가 홀수인지 체크해야 하는 경우
- 파이썬에서는 몫을 얻기 위해 몫 연산자(//)를 사용한다.
- 이외에도 거든 제곱 연산자(**)를 비롯해 다양한 연산자들이 존재한다.

##### 리스트 자료형
- 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
  - 사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 연결 리스트와 유사한 기능을 지원

##### 리스트 초기화
- 리스트는 대괄호([])안에 원소를 넣어 초기화하며, 쉼표(,)로 원소를 구분한다.
- 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []를 이용할 수 있다.
- 리스트의 원소에 접근할 때는 인덱스(Index) 값을 괄호에 넣는다.

##### 리스트의 인덱싱과 슬라이싱
- 인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱이라고 한다.
  - 파이썬의 인덱스 값은 양의 정수와 음의 정수를 모두 사용할 수 있다.
  - 음의 정수를 넣으면 원소를 거꾸로 탐색하게 된다.

##### 리스트의 인덱싱과 슬라이싱
- 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용한다.
  - 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있다.
  - 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정 한다.

##### 리스트 컴프리헨션
- 리스트를 초기화하는 방법 중 하나
   - 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있다.


##### _ 사용
- 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용

##### 튜플 자료형
- 튜플 자료형은 리스트와 유사하지만 다음과 같은 문법적 차이가 있음
  - 튜플은 한 번 선언된 값을 변경할 수 없습니다.
  - 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용합니다.
- 튜플은 리스트에 비해 상대적으로 공간 효율적

##### 사전 자료형
- 사전 자료형은 키와 값의 쌍을 데이터로 가지는 자료형이다.

##### 집합 자료형
- 집합의 특징
  - 중복을 허용하지 않음
  - 순서가 없음
- 집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있음
  - 이때 set() 함수를 이용
- 혹은 중괄호({})안에 각 원소를 콤마를 기준으로 구분하여 삽입함으로써 초기화 할 수 있음
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있음

##### 사전 자료형과 집합 자료형의 특징
- 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
- 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
  - 사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.
  
# 문제 풀다가 참고
##### 입력
- sys.stdin.readline() - input()은 비교적으로 느려서 sys.stdin.readline()이 빠르다.
- sys.stdin.readline().strip() - 맨 앞과 맨 끝에 공백을 제거하고 입력됨 보통 문자열을 입력할 때 사용

##### 리스트 
1. 리스트 값 길이에 따라 정렬 시켜줌
```
  list.sort(key=len) 
```
2. n번째 까지 받아서 2차 배열 만들기
```
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
``` 


##### 소수점
```
# 참고 사이트 - https://jsikim1.tistory.com/223
print("기존 값 : ", num)
print("1 의 자리에서 반올림 : ", round(num, -1))
print("10 의 자리에서 반올림 : ", round(num, -2))
print("100 의 자리에서 반올림 : ", round(num, -3))
print("1000 의 자리에서 반올림 : ", round(num, -4))
print("소수 첫번째 자리에서 반올림 : ", round(num))
print("소수 두번째 자리에서 반올림 : ", round(num, 1))
print("소수 세번째 자리에서 반올림 : ", round(num, 2))
print("소수 네번째 자리에서 반올림 : ", round(num, 3))
```

# 알고리즘 분류

## 그리디 알고리즘
- 그리디 알고리즘 은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미 합니다.
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구 합니다.
- 그리디 해법은 그 정당성 분석이 중요합니다.
  - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토 합니다.
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많습니다.
- 하지만 코딩 테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제 됩니다.

## 구현 : 시뮬레이션과 완전 탐색

##### 많은 연습 필요

#### 구현이란 머릿속에 있는 알고리즘을 소스코드롤 바꾸는 과정 입니다.
- 흔히 알고리즘 대회에서 구현 유형의 문제랑 무엇을 의미 할까
  - 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기는 어려운 문제를 지칭 한다.
- 구현 유형의 예시는 다음과 같습니다.
  - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
  - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
  - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
  - 적절한 라이브러리를 찾아서 사용해야 하는 문제
- 일반적으로 알고리즘 문제서의 2차원 공간은 행렬의 의미로 사용됩니다.
- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용 됩니다.

## 그래프 탐색 알고리즘 : DFS/BFS
- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있습니다.
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지 해야 합니다.

##### 스택 자료구조
- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조 입니다.
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.

##### 스택 동작 예시
- 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
- 위 예시) 5,2,3,1
```
# 스택 알고리즘은 리스트 형태에서 진행
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

##### 큐 자료구조
- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

##### 큐 동작 예시
- 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
- 먼저 들어온 데이터는 오른쪽에 배치되어 있고 가장 늦게 들어온 데이터는 왼쪽에 배치되어 있다.
- 위 예시) 4,1,4,7,3
```
from collections import depue

 # 큐 자료구조는 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

##### 재귀 함수
- 재귀 함수란 자기 자신을 다시 호출하는 함수를 의미합니다.
- 단순한 형태의 재귀 함수 예제
    - '재귀 함수를 호출합니다.' 라는 문자열을 무한히 출력합니다.
    - 어느 정도 출력하다가 최대 재귀 깊이 초과 메시가 출력됩니다.
```
def recursive_function():
  print("재귀 함수를 호출합니다.")
  recursive_function()

recursive_function()
```

##### 재귀 함수의 종료 조건
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 합니다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있습니다.
  - 종료 조건을 포함한 재귀 함수 예제
- 스택 자료구조 처럼 선입후출
```
def recursive_function(i) :
  # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
  if i == 100:
      return
  print(i, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출합니다.")
  recursive_function(i+1)
  print(i, "번째 재귀함수를 종료합니다.")

recursive_function(1)
```

##### 팩토리얼 구현 예제
- n! = 1 x 2 x 3 ··· x (n-1) x n
- 수학적으로 0! 과 1!의 값은 1입니다.
```
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1 : # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1) !를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print("반복적으로 구현 : " , factorial_iterative(5))
print("재귀적으로 구현 : " , factorial_recursive(5))

```





 




  



