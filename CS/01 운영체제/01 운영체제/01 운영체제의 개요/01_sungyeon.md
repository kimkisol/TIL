# 01_sungyeon

## <연습문제>

### 01.

운영체제

### 02.

임베디드 운영체제

### 03.

응용 프로그램

### 04. 

기존에 설정한 기능말고 다른 기능을 추가할 수 없다.

### 05.

인터페이스

### 06.

일괄작업 시스템

### 07.

대화형 시스템

### 08.

시분할 시스템

### 09.

일괄작업 시스템

### 10.

시분할 시스템, 다중 사용자 시스템

### 11.

실시간 시스템

### 12.

분산 시스템

### 13.

p2p시스템

### 14.

시스템 호출

###  15.

장치 드라이버

### 16.

단일형 구조 커널

### 17.

마이크로 구조 커널

### 18.

가상머신

## <심화문제>

### 01.

- 시스템 자원을 관리/보호
- 사용자와 컴퓨터간 커뮤니케이션을 원활히 하기 위해 인터페이스를 제공

- 응용프로그램도 관리/제어

### 02.

- 효율성, 안정성, 확장성, 편리성

### 03.

- CPU집중작업 : 계산위주의 작업으로 프로그램 실행동안 주로 CPU연산이 수행됨. 프로그램 실행동안은 입출력이 불가능하고, 데이터 수정이 불가능
- 입출력 집중작업 : 프로그램의 작업이 주로 주변장치와의 입출력, 프로그램 실행도중 입출력이 가능함

### 04.

정해진 시간내로의 작업 완료가 보장되는 시스템(응답시간 보장)

### 05.

자원을 직접 준비해서 사용하지 않고, 온라인을 이용해서 원하는 기능과 자원을 사용하고 사용한만큼 비용을 지불한다.

### 06.

- API(Application Programming Interface)  : 응용 프로그램 개발에서 사용할수 있도록 운영체제/프로그래밍 언어가 제공하는 함수집합. 운영체제의 시스템 호출도 운영체제가 제공하는 API이다.
- SDK(System Development Kit) : 개발자들이 사용할 수 있도록 API와 코드 편집기, 에뮬레이터를 함꼐 제공하여 편리한 개발을 할수 있도록 도와주는 툴. 대표적예는 안드로이드 SDK인 안드로이드 스튜디오

### 07.

커널의 모든 기능의 모듈들이 구분없이 하나로 되어있다. 모듈간 의존서잉 높아서 코드 수정이 어렵고, 발생한 에러에 대해서도 원인 파악이 쉽지 않다는 문제점이 있다.

하지만 모듈간 통신을 위한 비용이 발생하지 않는 다는 면에서는 효율적이라고 할 수 있다.

### 08.

프로세스 관리, 메로리 관리, 프로세스간 통신관리라는 커널의 기본적인 기능만 제공한다.

각 모듈은 독립적으로 작동한다. 때문에 가볍고 이식성이 높아 CPU용량이 작은 시스템에도 적용이 가능







