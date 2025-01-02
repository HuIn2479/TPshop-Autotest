# TPshop-Autotest
期末项目：TPshop 自动化测试  

~~随便写的，仅供参考~~

## 配置 allure 报告
1. 下载 allure 命令行工具  
   - [链接](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)


2. 解压到本地  
   - 随便放个地方，比如：`D:\allure-commandline`
   - 也可以其他路径，只要配置环境变量时填写正确即可


3. 配置环境变量  
   - 新建系统变量：`ALLURE_HOME`，值为解压后的路径，比如：`D:\allure-commandline\allure-xxx` 
   - 编辑系统变量：`Path`，添加 `%ALLURE_HOME%\bin`


4. 验证是否配置成功  
   - 打开命令行，输入 `allure --version`，显示版本号即为成功


5. 生成 allure 报告
   - 运行测试用例，生成测试结果