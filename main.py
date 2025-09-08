weight_input = input()
unit = weight_input[-2:] 
value = float(weight_input[:-2]) 
if unit == 'kg':
    result = value * 2.2046
    print(f"对应的英制重量为{result:.3f}磅")
else
    result = value / 2.2046
    print(f"对应的公制重量为{result:.3f}公斤")

