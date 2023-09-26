"""
패키지 설치 : pip install parse
"""
#from parse import compile,parse
import parse

""" example1 """
mystring = "It's spam, I love it!"

if "It's" in mystring:
    """ 성공적으로 문자열로 부터 값 또는 데이터를 추출하면,  추출된 값이 리턴
        추출하지 못했을 경우 None 값을 리턴 """
    result = parse.parse("It's {}, I {} it!", mystring)
    print("\nExample1")    
    print (result)
    print(result[0])
    print(result.fixed)

""" example2 """
mystring = "Bring out the holy hand grenade"
if 'Bring out the holy' in mystring:
    result = parse.parse("Bring out the holy {item}", "Bring out the holy hand grenade")
    print("\nExample2")    
    print (result)
    print (result.named)
    print (result["item"])

""" example3 """
p = parse.compile("It's {}, I love it!")
print("\nExample3")    
print(p)

result = p.parse("It's spam, I love it!")
print (result)
print (result[0])