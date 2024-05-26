import javalang


def is_syntactic_correct(code):
    """
    判断给定的代码是否语法正确。
    参数:
    code (str): 需要进行语法检查的代码字符串。
    返回:
    bool: 如果代码语法正确，则返回True；否则返回False。
    """
    try:
        javalang.parse.parse(code)
        return True
    except Exception as e:
        return False



