# TPshop 自动化测试

> [!NOTE]
> 代码整体写得不是很完善，会在后续进行补充优化

---

## 📦 前置依赖

### 环境要求

- Python 3.8+ 环境
- Chrome 浏览器 100+ 版本
- ChromeDriver 与浏览器版本匹配
- PyCharm IDE 开发工具

### 依赖安装

```bash  
# 标准安装方式
pip install -r requirements.txt

# 使用清华镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```  

---

## 🏷️ Allure 测试报告配置

### 1. 下载 Allure 命令行工具

- 下载地址：[Allure Commandline 官方下载](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)
- 推荐选择 2.20.1 或更高版本

### 2. 解压工具包

```plaintext  
# Windows 推荐路径  
D:\Programs\allure-commandline\allure-2.20.1  

# Linux/macOS 推荐路径  
/opt/allure-commandline/allure-2.20.1  
```

### 3. 配置环境变量

- Windows 系统
    - 右键点击“此电脑” -> “属性” -> “高级系统设置” -> “环境变量”
    - 在“系统变量”中新建一个变量名为 `ALLURE_HOME`，变量值为 Allure 命令行工具的路径
    - 编辑 `Path` 变量，添加 `%ALLURE_HOME%\bin` 路径到系统环境变量中
- Linux/macOS 系统
  ```bash  
   # 编辑 shell 配置文件
   echo 'export PATH="$PATH:/opt/allure-commandline/allure-2.20.1/bin"' >> ~/.zshrc
   source ~/.zshrc
  ```
- 验证是否配置成功
  ```bash  
  allure --version
  # 预期输出示例
  # allure 2.20.1
  ```

---

## 🏷️ 测试执行与报告生成

### 方式一：通过 run.py 执行

```python
# test_case/run.py
import os
import pytest

if __name__ == '__main__':
	pytest.main(['-s', '-v', '--alluredir=../test_report'])
	os.system('allure serve ../test_report --clean')  
```

### 方式二：通过命令行执行

```bash  
# 进入测试用例目录
cd test_case/

# 执行测试并生成结果文件
pytest -s -v --alluredir=../test_report

# 生成并查看报告
allure serve ../test_report --clean
```

---

## 📌 项目结构说明

```plaintext
*  
├── Screenshot        ← 截图目录  
├── test_case         ← 代码目录  
│   └── run.py        ← 执行位置  
├── test_report       ← 结果目录  
└── README.md         ← 项目说明  
```

---

## ⚠️ 注意事项

### 版本兼容性：  

- Chrome 浏览器与 ChromeDriver 需要匹配
- Allure 2.x 需要对应 allure-pytest 2.x

### 常见问题排查：  

- 报错：'allure' 不是内部命令  
  - 请检查环境变量是否配置正确  
  - 检查 Allure 环境变量配置是否正确  
  - 重启 PyCharm 或终端窗口  
- 报错：No such file or directory  
  - 请检查路径是否正确  
  - 确认 test_report 目录已创建  
  - 检查是否有权限访问该目录  
- 报错：No matching distribution found  
  - 请检查 Python 版本是否符合要求  
  - 检查 requirements.txt 是否正确  
  - 使用清华镜像安装依赖  

---

**技术栈**：Python、Pytest、Requests、Selenium、Allure  
**项目地址**：[GitHub](https://github.com/HuIn2479/TPshop-Autotest)  
