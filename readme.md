### 说明：
    1.框架运行
        本地运行: python3 lambda_function.py
        物理机部署: sh bin/start.sh
        aws-serverless运行: 入口为lambda_function.lambda_handler
    2.开发者需知
        开发者只需要在module下定义自己的功能模块
        例如实例中给出了test模块
            a.api.py  定义接口模型
            b.model.py 定义数据接口模型
            c.deal.py 逻辑处理函数
            
            # 备注（重要）:开发者可以按文档全部调试自己的代码，也可以仅仅定义自己业务模块（例如test）,但是本机调试注意加上以下代码表示模块的查找路径
            `
            cur_dir = os.path.split(os.path.realpath(__file__))[0]
            sys.path.append("%s/" % cur_dir)
            `    
    3.备注
        为防止接口被覆盖
        建议每个模块下Search,Operate下的接口采用统一形式，例如test模块下定义的接口应该为testResult(以防止其他模块有result接口被相互覆盖)
            
            
            
    