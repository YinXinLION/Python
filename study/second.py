import first

for i in range(10):
    first.laugh()

# import a as b             # 引入模块a，并将模块a重命名为b
#
# from a import function1   # 从模块a中引入function1对象。调用a中对象时，我们不用再说明模块，即直接使用function1，而不是a.function1。
#
# from a import *           # 从模块a中引入所有对象。调用a中对象时，我们不用再说明模块，即直接使用对象，而不是a.对象。

# 模块的搜索路径应为：
# 1. 程序所在的文件夹
# 2. 环境变量PYTHONPATH所包含的路径
# 3. 标准库的安装路径

#模块包
#可以将功能相似的模块放在同一个文件夹（比如说this_dir）中，构成一个模块包。通过 import this_dir.module
#该文件夹中必须包含一个__init__.py的文件，提醒Python，该文件夹为一个模块包。__init__.py可以是一个空文件。

