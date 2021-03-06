# Data-Structure
데이터를 구조적으로 표현하는 방식과 이를 구현하는 데 필요한 알고리즘에 대해 학습

1. [개요](#개요)
2. [자료구조의 효율성](#자료구조의-효율성)
3. [RAM : Random Access Memory](#ram--random-access-memory)
---

## **개요**
자료구조는 데이터의 효율적인 접근 및 조작을 간응하게 해주는 데이터 저장 및 관리방식이다.

다양한 성격의 데이터를 컴퓨터에 저장하고 저장한 내용을 가지고 올 수 있어야 한다. 마치 도서관 처럼 데이터를 쉽게 찾기 위해선 특정 구조를 만들어 관리해야 한다.

---

## **자료구조의 효율성**
1,000,000(백만) 이라는 숫자를 백만개의 원소에서 찾을 때 연산속도 차이가 약 3000배 정도 나오는 경우가 있다.

<br>

예시)

list 의 경우 0.016초의 시간이 소요된다.

반면 set 자료형은 lsit 보다 3000배 빠르다.

1,000번 반복되면 list는 16초가 걸려야 1,000,000(백만)이라는 정수를 찾을 수 있다. 반면 set은 훨씬 빠르게 찾는다.

각 자료구조마다 장단점이 있다. 모든 경우에 제일 좋은 자료 구조는 없다.

마치 도서관의 책이 장르와 제목별로 나뉘어 있을 때의 장점과 들어온 순서대로 정리된 책을 찾을 때의 장점이 다른 것 처럼 각 상황에 맞는 효율적인 자료구조가 있다.

## **RAM : Random Access Memory**
- 임의 접근 : 데이터가 어디 저장되어 있는지만 알면 접근하는데 항상 일정한 시간 O(1) 이 소요된다.
- 순차 접근 : 한 단계씩 거쳐야 해서 먼 주소로 갈 때 많은 시간을 써야 한다.
- 메모리는 임의 접근으로 동작하고 있다. 순차 접근 압도적으로 효율적이다.
 
---

## **메모리의 기본 단위 : 바이트(byte)**
- 1KB = 1,024 byte (2^10)
- 1kB = 1,000 byte (2^20)
- 1mB = 1,000,000 byte (2^30)
- 1gB = 1,000,000,000 byte (2^40)
- 1tB = 1,000,000,000,000 byte (2^50)

---

## **래퍼런스(reference)**

x = 95 일떄 x가 95에 담겨있는게 아니다. x는 95를 가리킨다. x는 95가 저장된 메모리 주소를 참조한다. x + 5 = 100 일 때 파이썬이 x에 있는 래퍼런스로 메모리 주소에 접근에 95를 받아와 95 + 5를 해서 100이 된다. 실제 래퍼런스와 더하진 않는다.

## **데이터의 주소**
<code>id()</code> 함수로 저장된 데이터의 메모리 주소를 정수로 표현할 수 있다.

```python
list1 = [1, 2]
list3 = [1, 2, 3]
list2 = list1  # Aliasing
print(id(list1))  # 14065...9160 
print(id(list2))  # 14065...9160 위와 같은 주소이다.

print(id(list3))  # 14065...9096 다른주소이다.

```

## **배열**

**배열이란?**
- 가장 기본적인 자료구조이다.
- C언어는 값 자체를 배열에 저장한다. 파이썬은 값 대신 가리키는 역할만 한다. 
  그래서 다양한 타입의 값을 저장할 수 있다.

배열이 시작하는 지점의 주소만 알면 어떤 인덱스든 주소를 쉽게 계산할 수 있다.
  
RAM은 임의 접근이다. 그 주소가 어디에 있든 O(1)으로 접근한다. 저장할 때도 O(1)
으로 접근한다. 이것이 배열의 큰 장점이다. 주소만 알면 한번에 접근하는 RAM의 특성을
효율적으로 이용하는 자료구조이다.

**배열 탐색**
- 접근은 인덱스를 통해 값을 찾는 것이며 탐색은 특정 조건을 만족하는 값을 찾는 것이다.
- 배열에서 탐색은 O(n)으로 비효율적이다. 하나씩 순서대로 데이터를 찾는 탐색법인 선형탐색이기 때문이다.
- 배열이 특정 순서로 정렬되어 있지 않을 때 선형탐색이 가장 효율적이다.
- 배열은 특정 인덱스에 접근/저장하는게 아주 효율적이나, 특정 조건을 만족하는 값을
탐색하는건 비교적 오래 걸린다.
  
**정적배열(Static Array)**
- C 배열처럼 처음 정의할 때 크기를 정해놓고 정해진 크기 이상 값을 추가할 수 없다.
- 보통 그냥 배열이라고 하면 정적배열을 뜻한다.
- 배열은 메모리 공간에 여백없이 쭉 이어진 공간이다.
- 덮어쓰는 위험성을 예방하려고 저장 공간을 고정시켜 둔다.
- 공간을 여유롭게 쓰려고 크게 정의해 메모리를 낭비하게 될 수도 있다. 

**동적 배열(Dynamic Array)**
- 상황에 맞게 크기가 바뀌는 배열
- 동적 배열이 꽉 차면 더 많은 값을 저장하기 위해 메모리 공간을 확보한다. 기존 배열의 2배 큰 배열을 만든다.
- 내부적으로는 정적배열을 이용해서 만들어진 것이다. 공간이 꽉 찰 때마다 알아서 적당한 크기로 늘려주게끔 미리 구현되어 있다. 개발자 입장에서 배열의 크기에 대해 신경쓸 필요가 없이 편리하게 사용할 수 있다.
- 피이썬의 list는 C배열을 이용해 동적 배열을 구현한 것이다.

**파이썬(Python) 리스트**
- 내부적으로 배열의 크기를 알 수 없다. 셀 수 있는 값/공간에 대해서만 알려주고 접근하려고 해도 오류가 난다.

**추가연산(append operation)**
- 배열의 가장 끝에 새 값을 넣는걸 추가 연산이라 한다.

*동적 배열의 시간복잡도*
- 경우1 : 정적 배열에 남는 공간이 있을 때 O(1)
- 경우2: 정적 배열이 꽉 찼을 때 O(n) <br>

경우2 는 왜 O(n) 일까?
  - 현재 사용 중인 배열보다 두 배로 큰 메모리 공간을 예약하고 일일이 하나씩 복사해야 한다. 접근은 O(1) 이지만 총 n번 해야 하며 추가도 O(1)이 있다. 따라서 O(n+1)에 1을 무시해서 O(n)이 된다.
  