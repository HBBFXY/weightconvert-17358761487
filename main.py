# 在这个文件下编写代码，题目具体要求见README.md文件
s = input("请输入重量")
if s.endswith('kg'):
    num = float(s[:-2])
    result = num*2.2046
    print(f"对应的英制重量为{result:.3f}磅")
elif s.endswith('pd'):
    num = float(s[:-2])
    result = num /2.2046
    print(f"对应的公制重量为{result:.3f}磅")
else:
    print("输入的格式错误，请以kg或pd结尾")    
