if len(weight_input) < 2:
    print("输入格式错误，请使用'kg'或'lb'作为单位（如10kg、5lb）")
else:
    if weight_input[-2:] == 'kg':
        try:
            value = float(weight_input[:-2])
            result = value * 2.2046
            print(f"对应的英制重量为{result:.3f}磅")
        except ValueError:
            print("数值格式错误，请输入有效的数字")
    
    elif weight_input[-2:] == 'pd':
        try:
            value = float(weight_input[:-2])
            result = value / 2.2046
            print(f"对应的公制重量为{result:.3f}公斤")
        except ValueError:
            print("数值格式错误，请输入有效的数字")
    
    else:
        print("输入格式错误，请使用'kg'或'pd'作为单位（如10kg、5lb）")
