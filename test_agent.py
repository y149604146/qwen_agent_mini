from qwen_agent import Agent
from qwen_agent.agents import Assistant
from qwen_agent.tools import TOOL_REGISTRY
from qwen_agent.utils.output_beautify import typewriter_print

from tools.GetParmsValue import GetParmsValue
from tools.boiler_assessment import BoilerAssessment

# 工具元数据
tools_metadata = [
    {
        "name": GetParmsValue.name,
        "description": GetParmsValue.description,
        "parameters": GetParmsValue.parameters
    },
    {
        "name": BoilerAssessment.name,
        "description": BoilerAssessment.description,
        "parameters": BoilerAssessment.parameters
    }
]
# 1. 查看已注册的工具（验证注册是否成功）
print("已注册的工具：", TOOL_REGISTRY.keys())  # 应输出 ['get_parms_value', 'boiler_assessment']

# 2. 初始化 Agent（自动加载所有注册的工具）
# agent = Agent(
#     function_list=list(TOOL_REGISTRY.values()),  # 传入所有工具类
#     system_prompt="你是一个锅炉安全评估助手，可调用工具回答问题。"
# )

# 步骤 1：配置所使用的模型服务
llm_cfg={
    #'model': 'qwen3-235b-a22b', #可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    'model' : 'qwen3:4b',
    'model_server': 'http://localhost:11434/v1',
    'api_key': 'yuanyuan',
    'generate_cfg':{
        'top_p': 0.8 # top_p越高生成的文本越多样, 范围在0-1.0之间
    }
}

#  步骤 2：创建一个智能体对象
# bot = Assistant(
#     llm=llm_cfg,
#     system_message='你是一位安全评估专家',
#     name='安全评估专家'
# )

# 步骤 3：创建一个智能体。这里我们以 `Assistant` 智能体为例，它能够使用工具并读取文件。
system_instruction = '''在收到用户的请求后，你应该：
- 首先得到评估对象需要用到的方法名，
- 然后运行工具`get_parms_value(评估方法名)`以得到对应评估对象在评估过程中需要用到的参数，
- 最后从给定的评估方法名和评估方法参数，运行工具如`boiler_assessment(参数对象)`得到最终的安全评估分数。
你总是用中文回复用户。'''
tools = ['get_parms_value', 'boiler_assessment']  # `code_interpreter` 是框架自带的工具，用于执行代码。
# files = ['./examples/resource/doc.pdf']  # 给智能体一个 PDF 文件阅读。
bot = Assistant(llm=llm_cfg,
                system_message=system_instruction,
                function_list=tools,
                #files=files
                )

# 步骤 4：作为聊天机器人运行智能体。
messages = []  # 这里储存聊天历史。
while True:
    # 例如，输入请求 "绘制一只狗并将其旋转 90 度"。
    query = input('\n用户请求: ')
    # 将用户请求添加到聊天历史。
    messages.append({'role': 'user', 'content': query})
    response = []
    response_plain_text = ''
    print('机器人回应:')
    for response in bot.run(messages=messages):
        # 流式输出。
        response_plain_text = typewriter_print(response, response_plain_text)
    # 将机器人的回应添加到聊天历史。
    messages.extend(response)