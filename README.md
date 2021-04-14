# Data-Structure
데이터를 구조적으로 표현하는 방식과 이를 구현하는 데 필요한 알고리즘에 대해 학습

1. [개요](#개요)
2. [자료구조의 효율성](#자료구조의-효율성)
3. [RAM](#RAM-:-Random-Access-Memory)
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