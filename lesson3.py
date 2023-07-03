def three_args(*, var1, var2=None, var3=None):
    arguments = ','.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

three_args(var1=221)
three_args(var1=5, var3=11)
three_args(var1='Nine', var3=None, var2='fsdfsdf')