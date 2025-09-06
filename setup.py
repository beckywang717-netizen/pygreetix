from setuptools import setup,find_packages

with open('README.rst','r') as f:
  log_description=f.read()

setup(
    name = '发布包名称',
    version = '版本号',
    long_description = long_description,
    author = '项目作者',
    url = 'https://xxxxx.com',
    license = 'MIT Lincense',
    platform = ['all'],
    install_requires=[
      "requests" # 没指定版本号，安装的就是最新版本
      "click==2.0", # 指定版本号
      "faker>2.0,<3.0" # 指定版本区间
    ]
    python_requires=">=3.7"
    packages=find_packages() # 自动扫描当前目录（或指定目录）下的所有Python包
    entry_points = (
      "console_scripts":[xxxx]
    )
)
