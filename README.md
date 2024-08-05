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
  




  
     

 




  



