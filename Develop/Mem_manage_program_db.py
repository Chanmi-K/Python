'''
회원 DB 테이블명 : memberT01
01.	메인 : memTitle()
		회원가입 : memIns() 함수		DB연결 Insert		OK
		로그인 : memLog() 함수			DB연결 Select		OK
		회원목록 : memSel() 함수		DB연결 Select		OK
		정보수정 : memUpd() 함수	DB연결 Update		OK
		회원탈퇴 : memDel() 함수		DB연결 Delete		OK
02. while True:
'''

import cx_Oracle

'''데이터'''
menu = ['1.회원가입', '2.로그인', '3.회원목록','4.정보수정','5.회원탈퇴', '9.메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk  = ["1","2","3","4","5","9"]

'''함수 생성'''
def memTitle():		#메인
	print(""); print(f'{"메뉴선택":=^110}')
	for i in menu:		#menu list 출력 (구분 'tab')
		print(f'{i:^15}', end='')
	print(""); print(f'{"":=^114}', end='\n\n')

def memIns():			#1.회원가입
	connection = cx_Oracle.connect("hr/hr@localhost:1521/XE")		#DB와 연동
	
	print(f'{"^SignUp!":^114}', end='\n\n')
	input_signup = [0]*len(itemList)		#itemList 길이만큼 리스트 초기화
	for idx in range(len(itemList)):
		input_signup[idx] = input(f'\t\t{itemList[idx]}\t:  ')	#리스트에 input 값 넣어주기
	
	print(f'{"":<45}*** {input_signup[0]} 님 회원가입 성공! ***{"":>45}')

	cursor = connection.cursor()
	cursor.execute("""
				INSERT INTO memberT01 
				VALUES(:mId, :mPwd, :mName, :mEmail, :mPhone, :mAddr)""",
				mId = input_signup[0],
				mPwd = input_signup[1],
				mName = input_signup[2],
				mEmail = input_signup[3],
				mPhone = input_signup[4],
				mAddr = input_signup[5])		#memberT01 테이블에 데이터 삽입

	connection.commit()
	cursor.close()		#Insert cursor 닫기
	connection.close()

def memLog():			#2.로그인
	connection = cx_Oracle.connect("hr/hr@localhost:1521/XE")		#DB와 연동

	cursor = connection.cursor()
	
	print(f'{"Log In!":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")

	cursor.execute("""
				SELECT mem_id, mem_pwd 
				FROM memberT01
				WHERE mem_id = :mId AND mem_pwd = :mPwd""",
				[input_id, input_pwd])		#memberT01 테이블 중 ID와 PWD 조회

	mem_IP = cursor.fetchone()		#한줄 가져오기
	if mem_IP is None:						#ID와 PWD가 DB에 일치하는게 없다면
		print(f'{"":<45}===ID 또는 PWD 확인해주세요==={"":>45}')
	else:												#일치
		print(f'{"":<45}***{input_id} 님 로그인 성공!***{"":>45}')
	
	connection.commit()
	cursor.close()		#Select cursor 닫기
	connection.close()

def memSel():		#3.회원목록
	connection = cx_Oracle.connect("hr/hr@localhost:1521/XE")		#DB와 연동

	cursor = connection.cursor()
	cursor.execute("""SELECT * FROM memberT01""")		#memberT01 테이블 전체 조회 SELECT

	print(f'{"<User List>":^114}', end='\n\n'); print(' '*4,"="*100)
	for i in itemList:		#itemList 출력
		print(f'\t{i}\t', end = '')
		if i == "EMAIL":	#Email 이 길어서 길이를 맞추기 위해 Email 만 한번 더 tab함
			print('\t', end='')
	print(""); print(' '*4,"="*100,"\n")
	
	for mem in cursor:
		for i in range(len(mem)):
			print(f'\t{mem[i]}\t', end='')			#memberT01 테이블 출력
		print()

	connection.commit()
	cursor.close()		#Select cursor 닫기
	connection.close()

def memUpd():		#4.정보수정
	connection = cx_Oracle.connect("hr/hr@localhost:1521/XE")		#DB와 연동

	cursor = connection.cursor()
	
	print(f'{"^Update!":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")
	
	cursor.execute("""
				SELECT *
				FROM memberT01
				WHERE mem_id = :mId AND mem_pwd = :mPwd""",
				[input_id, input_pwd])		#memberT01 테이블 조회, ID와 PWD가 일치하는 데이터만

	mem_data = cursor.fetchone()	#ID와 PWD가 일치하는 한 줄 가져오기
	connection.commit()
	cursor.close()		#Select cursor 닫기
	if mem_data is None:					#일치하는 데이터가 없다면
		print(f'{"":<45}===ID 또는 PWD 확인해주세요==={"":>45}')
	else:												#일치
		print(f'{"":<45}***{input_id} 님 회원정보 수정 가능합니다.***{"":>45}')
		print(f'{"":<25}# 수정 전 내용 확인 : ', end='')		
		for i in mem_data:			#수정 전 내용 출력
			print(i, end=' ')
		print()
			
		update_yn = [0]*len(itemList) 			#수정 여부 데이터 리스트 초기화 (y,n 입력 받을 것)
		input_update = [0]*len(itemList)		#수정 데이터 리스트 초기화
		input_update[0] = mem_data[0]		#ID는 수정하지 않기 때문에 미리 넣어놓기
		for idx in range(1,len(itemList)):		#ID 빼고 수정 시작
			while True:
				update_yn[idx] = input(f'\t\t{itemList[idx]}\t"수정 (y/n)"  :  ').lower()		#수정 여부 y, n 입력 받기 (대/소문자 상관 X)
				if update_yn[idx] == "y":			#y 입력 시 수정데이터 리스트에 새로운 input 값 입력
					input_update[idx] = input(f'\t\t{itemList[idx]}\t :  ')
					break
				elif update_yn[idx] == "n":		#n 입력시 수정데이터 리스트에 기존 데이터 그대로 입력
					input_update[idx] = mem_data[idx]
					break
				else:			# 그외 입력시 다시 입력하세요 출력
					print("\t\t\t---다시 입력하세요(y/n)---")
			
		print(); print(f'{"":<25}# 수정 후 내용 확인 : ', end='')		
		for i in input_update:		#수정 후 내용 출력
			print(i, end=' ')
		print()
	
		cursor = connection.cursor()
		cursor.execute("""
					UPDATE memberT01 
					SET mem_pwd = :mPwd, mem_name = :mName, mem_email = :mEmail, 
					mem_phone = :mPhone, mem_addr = :mAddr
					WHERE mem_id = :mId""",
					mId = input_update[0],
					mPwd = input_update[1],
					mName = input_update[2],
					mEmail = input_update[3],
					mPhone = input_update[4],
					mAddr = input_update[5])		#memberT01 테이블 수정 UPDATE
				
		connection.commit()
		cursor.close()		#Update cursor 닫기	
		print(); print(f'{"":<45}@@@ {input_id} 님 회원정보 수정 성공! @@@{"":>45}')
	
	connection.close()

def memDel():		#5.회원탈퇴
	connection = cx_Oracle.connect("hr/hr@localhost:1521/XE")		#DB와 연동
	
	cursor = connection.cursor()

	print(f'{"Unregister":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")
	
	cursor.execute("""
				SELECT mem_id, mem_pwd 
				FROM memberT01
				WHERE mem_id = :mId AND mem_pwd = :mPwd""",
				[input_id, input_pwd])		#memberT01 테이블 중 ID와 PWD 조회

	mem_IP = cursor.fetchone()		#한줄 가져오기
	if mem_IP is None:						#ID와 PWD가 DB에 일치하는게 없다면
		print(f'{"":<45}===ID 또는 PWD 확인해주세요==={"":>45}')
	else:												#일치
		print(f'{"":<45}***{input_id} 님 회원 탈퇴 가능합니다.***{"":>45}')
		while True:
			input_delete = input('\t\t정말 탈퇴 하시겠습니까? (y/n)  :  ').lower()		#탈퇴 여부 y,n 입력 받기 (대/소문자 상관 X)
			if input_delete == 'y':			#y 입력 시 해당 정보 삭제
				cur = connection.cursor()
				cur.execute("""
						DELETE FROM memberT01 
						WHERE mem_id = :mId""",
						mId = input_id)		#memberT01 테이블에서 해당 정보 삭제
				connection.commit()
				cur.close()		#Delete cursor 닫기
				print(); print(f'{"":<45}--- {input_id} 님 회원 탈퇴 되었습니다. ---{"":>45}')
				break
			elif input_delete == 'n':		#n 입력시 탈퇴 실패
				print(); print(f'{"":<45}--- 회원 탈퇴 실패 ---{"":>45}')
				break
			else:		#그외 입력시 다시 입력하세요 출력
				print("\t\t\t---다시 입력하세요(y/n)---")

	connection.commit()
	cursor.close()		#Select cursor 닫기
	connection.close()

'''시스템'''
while True:
	memTitle()
	inputMenu = input(f'{"메뉴의 번호를 입력해주세요 : ":>55}')	; print()	#메뉴 번호 입력
	
	if inputMenu in menuChk:
		if inputMenu == '1':			#1.회원가입
			memIns()
		elif inputMenu == '2':		#2.로그인
			memLog()
		elif inputMenu == '3':		#3.회원목록
			memSel()
		elif inputMenu == '4':		#4.정보수정
			memUpd()
		elif inputMenu == '5':		#5.회원탈퇴
			memDel()
		elif inputMenu == '9':		#9.메뉴종료
			print(f'\n{"<<시스템을 종료합니다>>":^105}\n')
			break
	else:		#메뉴 번호 외 입력시 Error
		print(f'\n{"---잘못된 접근입니다---":^90}')


