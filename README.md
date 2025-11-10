# qwen_agent_mini
Help you build your agent with qwen_agent framework, which is based on you local deployed LLM followed OpenAI API(E.g.,  this project is using ollama delpoyed qwen3:4b). 
This project use 2 tools to do the demo, please note that all these 2 tools are hardcoded, just help you to learn how to use qwen_agent framework.

# Environment preparation
conda create -n qwen_agent python=3.12
pip install -U "qwen-agent[rag,code_interpreter,gui,mcp]"
pip install uv
pip install sqlglot

# Project explaination
Follow the steps below to use this project.
1. create a tool as `boiler_assessment.py`/`GetParmsValue.py`, copy codes of `boiler_assessment.py`/`GetParmsValue.py`, and then modify the content to customize functions you want to implement in your agent.
2. create agent as `test_agent`, copy codes and then modify the content to use your tools, customize your prompt and your local deployed LLM.
3. run the agent python file to run your agent.

# Result exmaple
1. run `python test_agent.py`
2. server will be upped, input your requrest after `用户请求` in console, then it will return the tools function calling.

> 用户请求: 当前锅炉安全分数
> 机器人回应:
> 2025-11-10 11:23:13,980 - base.py - 780 - INFO - ALL tokens: 4, Available tokens: 57912
> [TOOL_CALL] get_parms_value
> {"sec_assess_tool": "boiler_assessment"}
> [TOOL_RESPONSE] get_parms_value
>  
>                 {
>                     "boiler_temp":"35℃",
>                     "water_level":"100cm",
>                     "pressure":"13.7MPa"
>                 } 2025-11-10 11:25:04,737 - base.py - 780 - INFO - ALL tokens: 62, Available tokens: 57912
> 
> [TOOL_CALL] boiler_assessment
> {"boiler_temp": "35℃", "water_level": "100cm", "pressure": "13.7MPa"}
> [TOOL_RESPONSE] boiler_assessment
> According to the conditions that boiler's temperature is 35℃, water lever is 100cm, and the pressure is 13.7MPa, the ultimate result is 89.2025-11-10 11:25:52,756 - base.py - 780 - INFO - ALL tokens: 149, Available tokens: 57912
> 
> [ANSWER]
> 根据当前锅炉的温度35℃、水位100cm和压力13.7MPa，安全评估分数为89。
> 用户请求: 