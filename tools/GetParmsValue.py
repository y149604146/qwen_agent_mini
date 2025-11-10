import json5
from qwen_agent.tools.base import BaseTool, register_tool
import ResultBuilder

@register_tool("get_parms_value", allow_overwrite=True)
class GetParmsValue(BaseTool):

    parameters = [
        {
            'name' : 'sec_assess_tool',
            'type' : 'string',
            'description' : '基本工具。执行安全评估工具的参数获取：提供安全评估工具名称作为参数，该工具将检索调用安全评估工具时所需的参数。',
            'required' : True
        }
    ]

    def call(self, params: str, **kwargs) -> str:
        # try:
        #     params = self._verify_json_format_args(params)
        #     sec_assess_tool_name = params["sec_assess_tool"]
        # except:
        #     return ResultBuilder.error("[GetParmsValue] Invalid request format: Input must be a JSON object containing 'sec_assess_tool' field")

        sec_assess_tool_name = json5.loads(params)['sec_assess_tool']

        if sec_assess_tool_name == "boiler_assessment":
            # TODO: get parms actual values: could from existed sensors, could from llm, also could be the hard code default value.
            default_param_values = ''' 
                {
                    "boiler_temp":"35℃",
                    "water_level":"100cm",
                    "pressure":"13.7MPa"
                } '''
            param_values = default_param_values
            return param_values
        else:
            return ResultBuilder.error(f"{sec_assess_tool_name} was not supported, only support 'boiler_assessment' currently.")




if __name__ == "__main__":
    print(GetParmsValue().call('''{"sec_assess_tool": "boiler_assessment"}'''))
