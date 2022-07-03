'''
회원 DB 파일 : MemV01.txt
01.	메인 : memTitle()
		회원가입 : memIns() 함수
		로그인 : memLog() 함수
		회원목록 : memSel() 함수
		정보수정 : memUpd() 함수
		회원탈퇴 : memDel() 함수
02. while True:
'''

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
	print(f'{"^SignUp!":^114}', end='\n\n')
	input_signup = [0]*len(itemList)		#itemList 길이만큼 리스트 초기화
	for idx in range(len(itemList)):
		input_signup[idx] = input(f'\t\t{itemList[idx]}\t:  ')	#리스트에 input 값 넣어주기
	f = open("MemV01.txt","a")		#txt 파일에 input 값 저장
	User_data = ""
	for idx, i in enumerate(input_signup):		#데이터 사이마다 ',' 넣어주기 마지막 데이터 빼고
		if idx != len(input_signup)-1:
			User_data += (i + ',')
		else:
			User_data += i
	#User_data = ','.join(input_signup)
	f.write(User_data)
	f.write('\n')
	f.close()

def memLog():			#2.로그인
	print(f'{"Log In!":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")
	
	id_ok = 0    #id 확인 변수 정의
	
	f = open('MemV01.txt','r')      #User 파일 읽기모드로 열기
	User_data = f.readlines()		#파일의 모든 줄 읽어서 각각의 줄을 리스트로 반환
	for line in User_data:
		User_log = line.split(',')      #','를 기준으로 나누기
		
		if input_id == User_log[0]:     #입력 id와 DB id 와 같다면
			id_ok = 1
			break
	
	if id_ok:		#id_ok가 1로 True 일때 (id가 같을 때)
		if input_pwd == User_log[1]:		#입력 pwd와 DB pwd 가 같다면
			print(f'{"":<45}***{input_id} 님 로그인 성공!***{"":>45}')
		else:			#id는 같으나 입력 pwd와 DB pwd가 다를 때
			print(f'{"":<45}---Pwd 확인해주세요---{"":>45}')
	else:				#id_ok가 0으로 False 일때 (id가 같지 않을 때)
		print(f'{"":<45}===등록되지 않은 회원입니다==={"":>45}')
	f.close()

def memSel():		#3.회원목록
	print(f'{"<User List>":^114}', end='\n\n'); print(' '*4,"="*100)
	for i in itemList:		#itemList 출력
		print(f'\t{i}\t', end = '')		
		if i == "EMAIL":	#Email 이 길어서 길이를 맞추기 위해 Email 만 한번 더 tab함
			print('\t', end='')
	print(""); print(' '*4,"="*100,"\n")
	
	f = open('MemV01.txt','r')			#open('MemV01Bak.txt','r',encoding = "utf-8")
	User_data = f.readlines()		#User 파일 읽어오기
	for line in User_data:		#줄 별로 가져오기
		User_list = line.split(',')	#줄 별로 ',' 기준으로 나누기
		for i in User_list:		#줄 별로 출력
			x = i.strip()			#strip 사용해서 공백 없애기
			print(f'\t{x}\t',end ='')		#tab으로 칸 맞추기
		print("")
	f.close()
	print(' '*4,"-"*100)

def memUpd():		#4.정보수정
	print(f'{"^Update!":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")
	
	id_ok = 0    #id 확인 변수 정의
	idxChk = -1		#id의 idx 값 체크 변수 정의
	
	f = open('MemV01.txt','r')      #User 파일 읽기모드로 열기
	User_data = f.readlines()		#파일의 모든 줄 읽어서 각각의 줄을 리스트로 반환
	for line in User_data:
		idxChk += 1
		User_log = line.split(',')      #','를 기준으로 나누기
		
		if input_id == User_log[0]:     #입력 id와 DB id 와 같다면
			id_ok = 1
			break
	
	if id_ok:       #id_ok가 1로 True 일때 (id가 같을 때)
		if input_pwd == User_log[1]:		#입력 pwd와 DB pwd 가 같다면
			print(f'{"":<45}***{input_id} 님 회원정보 수정 가능합니다.***{"":>45}')
			print(f'{"":<25}# 수정 전 내용 확인 : {User_data[idxChk]}')		#수정 전 내용 출력
			
			input_update = [0]*len(itemList)		#수정 여부 데이터 리스트 초기화 (y,n 입력 받을 것)
			for idx in range(1,len(itemList)):		#Id 빼고 수정 시작
				while True:
					input_update[idx] = input(f'\t\t{itemList[idx]}\t"수정 (y/n)"  :  ').lower()		#수정 여부 y, n 입력 받기 (대/소문자 상관 X)
					if input_update[idx] == 'y' or input_update[idx] == 'n':
						if input_update[idx] == "y":			#y 입력 시 User_log를 input 값으로 수정
							User_log[idx] = input(f'\t\t{itemList[idx]}\t :  ')
							break
						elif input_update[idx] == "n":		#n 입력시 pass
							break
					else:			# 그외 입력시 다시 입력하세요 출력
						print("\t\t\t---다시 입력하세요(y/n)---")
			
			User_Str =""
			for idx, i in enumerate(User_log):		#데이터 사이마다 ',' 넣어주기 마지막 데이터 빼고
				if idx != len(User_log)-1:
					User_Str += (i + ',')
				else:
					User_Str += i
			User_data[idxChk] = User_Str			#id가 같은 idxChk에 해당하는 데이터에 새로운 데이터 넣어주기

			print(); print(f'{"":<25}# 수정 후 내용 확인 : {User_data[idxChk]}')		#수정 후 내용 출력

			f = open("MemV01.txt","w")			#수정 후 데이터 파일에 입력
			for i in User_data:
				f.write(i)
			f.close()

			print(); print(f'{"":<45}@@@ {input_id} 님 회원정보 수정 성공! @@@{"":>45}')

		else:		#id는 같으나 입력 pwd와 DB pwd가 다를 때
			print(f'{"":<45}---Pwd 확인해주세요---{"":>45}')
	else:			#id_ok가 0으로 False 일때 (id가 같지 않을 때)
		print(f'{"":<45}===등록되지 않은 회원입니다==={"":>45}')

def memDel():		#5.회원탈퇴
	print(f'{"Unregister":^114}', end='\n\n')
	input_id = input(f'\t\t{itemList[0]}\t:  ') # id 입력
	input_pwd = input(f'\t\t{itemList[1]}\t:  ') # pwd 입력
	print("")
	
	id_ok = 0    #id 확인 변수 정의
	idxChk = -1		#id의 idx 값 체크 변수 정의
	
	f = open('MemV01.txt','r')      #User 파일 읽기모드로 열기
	User_data = f.readlines()		#파일의 모든 줄 읽어서 각각의 줄을 리스트로 반환
	for line in User_data:
		idxChk += 1
		User_log = line.split(',')      #','를 기준으로 나누기
		
		if input_id == User_log[0]:     #입력 id와 DB id 와 같다면
			id_ok = 1
			break
	
	if id_ok:       #id_ok가 1로 True 일때 (id가 같을 때)
		if input_pwd == User_log[1]:		#입력 pwd와 DB pwd 가 같다면
			print(f'{"":<45}***{input_id} 님 회원 탈퇴 가능합니다.***{"":>45}')
			
			while True:
				input_delete = input('\t\t정말 탈퇴 하시겠습니까? (y/n)  :  ').lower()		#탈퇴 여부 y,n 입력 받기 (대/소문자 상관 X)
				if input_delete == 'y':			#y 입력 시 User_log를 삭제
					
					del User_data[idxChk]		#탈퇴 회원 삭제
					f = open("MemV01.txt","w")			#데이터 파일에 입력
					for i in User_data:
						f.write(i)
					f.close()
					
					print(); print(f'{"":<45}--- {input_id} 님 회원 탈퇴 되었습니다. ---{"":>45}')
					break
				elif input_delete == 'n':		#n 입력시 탈퇴 실패
					print(); print(f'{"":<45}--- 회원 탈퇴 실패 ---{"":>45}')
					break
				else:		#그외 입력시 다시 입력하세요 출력
					print("\t\t\t---다시 입력하세요(y/n)---")

		else:		#id는 같으나 입력 pwd와 DB pwd가 다를 때
			print(f'{"":<45}---Pwd 확인해주세요---{"":>45}')
	else:			#id_ok가 0으로 False 일때 (id가 같지 않을 때)
		print(f'{"":<45}===등록되지 않은 회원입니다==={"":>45}')

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


