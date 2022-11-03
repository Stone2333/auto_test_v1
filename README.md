# 接口自动化代码
实现主流程接口自动化测试,生成测试报告
python+pytest+allure

### 环境准备
- 使用pip命令一键安装所有依赖库  
`pip install -r requirements.txt`
  
### 准备数据

### 目录结构

    │  .gitignore                        # 忽略文件配置
    │  push.sh                           # git脚本
    │  README.md                         # 描述文件
    │  requirements.txt                  # 依赖库一键安装文件
    │  run.py                            # 执行自动化测试主程序
    │  
    ├─business                           - 业务代码
    │      public.py                     # 公共业务代码
    │      __init__.py
    │          
    ├─casesdata                          - 用例
    │      login.yaml                    # 登录用例
    │      __init__.py
    │      
    ├─common                             - 公共方法
    │      aes.py                        # aes加密
    │      captcha_identify.py           # 验证码识别
    │      DB.py                         # 数据库
    │      delete.py                     # 删除sql
    │      faker_data.py                 # 假数据
    │      log.py                        # 日志模块
    │      query.py                      # 查询sql
    │      sm4.py                        # sm4加密
    │      tool.py                       # 通用工具
    │      update.py                     # 更新sql
    │      __init__.py
    │          
    ├─config                             - 设置
    │      setting.py                    # 公共参数配置
    │      __init__.py
    │      
    ├─logs                               - 日志存储
    │      __init__.py
    │      
    ├─testcases                          - 测试代码
    │      conftest.py                   # 测试代码通用条件
    │      login.py                      # 登录测试代码
    │      __init__.py
    │
    └─testreport                         - 测试报告数据存储
           __init__.py
