<파이썬을 이용한 컴퓨터 과학 입문>의 소스 코드입니다.

* 북사이트 https://introcs.cs.princeton.edu/python/home/
* 예제 소스 https://introcs.cs.princeton.edu/python/code/
* 길벗 예제 소스 https://github.com/gilbutITbook/006793


이 책의 실습에는 다음 프로그램이 필요합니다.

* 파이썬 3.x
* NumPy
* Pygame
* 이 책의 전용 모듈

부록 D에 윈도, 리눅스, macOS에 따른 환경 구성이 설명되어 있습니다.
윈도 환경에서는 python 명령어를 실행하면 설치된 파이썬 3.x 버전이 실행되지만, 리눅스와 macOS에서 python 명령어는 
파이썬 2.x를 실행합니다. 리눅스와 macOS 환경에서는 파이썬 2.x가 시스템 관리를 위해 기본으로 설치되어 있으며 삭제할 
수 없는 경우가 많습니다. 파이썬 3를 설치한 이후에 파이썬 3를 실행하려면 반드시 python3 명령어를 사용해야 합니다.
이 책에서는 입출력을 위해 파이썬의 print 대신 stdio 공통 모듈을 사용해서 처리합니다. 공통 모듈을 사용하면 파이썬 버전이
나 언어의 변화에 중립적일 수 있습니다. 이 책의 자매서인 <Introduction to Programming in Java>에서도 입출력 공통 모듈
을 사용해서 프로그래밍 언어의 구분 없이 입출력에는 같은 인터페이스를 사용하게 되어 있습니다.


이 책의 예제 파일 구조는 다음과 같습니다.

파일명                          설명
introcs-1.0.zip                 이 책에서 사용하는 표준 입출력 모듈(stdio)과 라이브러리 설치 스크립트
stdlib-python.zip               표준 입출력 모듈의 소스 코드
introcs-python                  이 책의 예제 코드
introcs-data.zip                이 책의 예제에 사용하는 데이터
introcs-PartialSolutions.zip    연습문제 중 일부 해법

*  이 책의 실습에 필요한 모듈은 introcs-1.0.zip을 설치하면 됩니다. 설치법과 모듈 목록에 대해서는 부록 D를 참조하세요.
*  이 책의 예제는 장별로 분류되어 있지 않고, 주제별 파일명으로 되어 있습니다. 각 절의 프로그램 목록은 부록 D.1을 참조하세요.
