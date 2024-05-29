print(' **** 좌석 예매 프로그램 ****')

좌석_수 = int(input('총 좌석 수는? :'))
seat = []  #make list
for i in range(0,좌석_수) :
    seat.append( 0 ) #append to list '0' for 좌석_수
print('총 좌석수 =' , seat.count( 0 ))
while 1 :
    예약 = input('좌석 예매? (Y or N)')
    if 예약 == 'Y' or 예약 == 'y' :
        print('1~{} 에서 원하는 좌석 선택' .format(좌석_수))
        선택 = int(input())
        if 선택 >= 1 and 선택 <=좌석_수 :
            if (seat[선택 - 1]) == 0 : #선택한 숫자가 리스트내에서 '0'의 상태인지 확인
                seat[선택 - 1] = 'X' #'0'의 상태를 1로 변경
                print(선택,'번 좌석이 예매되었습니다') 
                print('-' * 40)
                print('좌석현황 :' , seat)
                print('-' * 40)
            else :
                print('{}번 좌석은 이미 예약된 자리입니다' .format(선택))
        elif 예약 == 'N' or 예약 == 'n' :
            print('\n*** 좌석 예매를 종료합니다 ***')
            break
        else :
            continue

                