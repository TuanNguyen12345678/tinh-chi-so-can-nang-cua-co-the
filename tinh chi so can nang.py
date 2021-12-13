import math
def chiso():
    try:
        cannang=float(input('nhập số cân nặng Kg: '))
        chieucao=float(input('nhập chiều cao m: '))
        bmi=cannang/chieucao
        if bmi>40:
            print('BÉO PHÌ')
        elif 35 <= bmi < 40 :
            print(' BÉO PHÌ CẤP ĐỘ II')
        elif 30 <= bmi < 35 :
            print('BÉO PHÌ CẤP ĐỘ I')
        elif 25 <= bmi < 30:
            print('THỪA CÂN')
        elif 18.5 <= bmi < 25:
            print('BÌNH THƯỜNG')
        elif 17 <= bmi < 18.5:
            print('GẦY CẤP ĐỘ I')
        elif 16 <= bmi < 17:
            print('GẦY CẤP ĐỘ II')
        elif bmi<16:
            print('GẦY CẤP ĐỘ III')
    except:
        print('NHẬP ĐẦU VÀO CHƯA ĐÚNG')
if __name__=="__main__":
    chiso()