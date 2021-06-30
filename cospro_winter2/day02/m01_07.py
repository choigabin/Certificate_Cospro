#파일 업로드를 위한 파일 정보를 확인하는 함수의 빈칸 채우기
def solution(file_info):
    sucess = 0
    fail = 0
    for f in file_info:
        splited = f.split(".") #리스트로 분리
        print(splited)
        if splited[0] == 'jpeg' and int(splited[2]) < 1000:
            sucess += 1
        else:
            fail += 1
    return sucess, fail

files_info = ["jpeg.all.jpg.1500", "mpeg.all.mp3.500"]
sucess, fail = solution(files_info)
print(sucess, fail, sep=".")

string = "this is string constant"
splited = string.split(" ") #공백 문자로 나누기
print(type(splited).splited)