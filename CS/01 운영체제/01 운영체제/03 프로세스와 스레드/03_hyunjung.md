1. 프로세스 제어블록
2. 준비상태
3. 대기상태
4. 디스패치
5. 휴식상태
6. 문맥교환
7. fork()
8. exec()
9. 고아 프로세스
10.  스레드
11.  exit(), return()
12.  garbage collection
13. 프로세스의 계층 구조





1. 생성 상태 -> 준비 상태 -> 실행 상태 -> 대기 상태 -> 완료 상태 (이미지 업로드 예정)

2. 휴식 상태 : 프로세스가 작업을 일시적으로 쉬고 있는 상태

   보류 상태 : 프로세스가 메모리에서 잠시 쫓겨난 상태

   - 차이점 : 보류 상태는 '일시 정지 상태', 활성 상태

3. 프로세스 제어 블록의 구성
   - 포인터
   - 프로세스 상태
   - 프로세스 구분자
   - 프로그램 카운터
   - 프로세스 우선순위
   - 각종 레지스터 정보
   - 메모리 관리 정보
   - 할당된 자원 정보
   - 계정 정보
   - 부모 프로세스 구분자와 자식 프로세스 구분자

4. CPU를 차지하던 프로세스가 나가고 새로운 프로세스를 받아들이는 작업

5. 프로세스의 구조
   1. 코드 영역 : 프로세스의 본문이 기술
   2. 데이터 영역 : 변수나 파일 등의 각종 데이터
   3. 프로세스를 실행하기 위해 부수적으로 데이터를 모아놓은 곳
   
6. fork() 장점
   1. 프로세스의 생성 속도가 빠르다
   2. 추가 작업 없이 자원을 상속할 수 있다.
   3. 시스템 관리를 효율적으로 할 수 있다.

7. 프로세스의 구조체를 재활용하기 위함(이미 만들어진 프로세스 제어 블록, 메모리 영역, 부모 - 자식 관계 그대로 사용 가능)

8. 동시에 여러 작업을 처리하고 종료된 프로세스의 자원을 회수하는데 유용
   1. 여러 작업의 동시 처리
   2. 용이한 자원 회수
   
9. 멀티... 비교하기

   - 멀티스레드 : 프로세스 내 작업을 여러 개의 스레드로 분할함으로써 작업의 부담을 줄이는 프로세스 운영 기법
   - 멀티태스킹 : 운영체제가 CPU에 작업을 줄 때 시간을 잘게 나누어 배분하는 기법
   - 멀티프로세싱 : CPU를 여러 개 사용하여 여러개의 스레드를 동시에 처리하는 작업 환경
   - CPU 멀티스레드 : 한 번에 하나씩 처리해야 하는 스레드를 파이프라인 기법을 이용하여 동시에 여러 스레드를 처리하도록 만든 병렬 처리 기법