'''
java
try{
    예외가 발생할 것 같은 코드
}catch(IndexOutOfRangeException){
    예외처리하는 코드
}catch{
    예외처리하는 코드(catch구문 여러개 가능)
}finally{
    꼭 실행해야 하는 코드
}

python
try:
    예외가 발생할 것 같은 코드
except IndexError as e: #특정 예외
    예외처리하는 코드
except:
    예외처리하는 코드
else:
    예외가 발생하지 않았을 떄 실행하는 코드
finally:
    꼭 실행해야 하는 코드
'''

