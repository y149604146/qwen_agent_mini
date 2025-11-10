import json5
from qwen_agent.tools.base import BaseTool, register_tool


@register_tool("boiler_assessment", allow_overwrite=True)
class BoilerAssessment(BaseTool):

    description = '安全评估方法的一种，用于评估锅炉的安全。执行锅炉安全评估：提供锅炉的温度、水位、压力三项必填参数及其他可选参数，该工具将返回锅炉的安全评估结果。'
    parameters = [
        {
            'name' : 'boiler_temp',
            'type' : 'string',
            'description' : '锅炉的温度',
            'required' : True
        },
        {
            'name': 'water_level',
            'type': 'string',
            'description': '锅炉的水位',
            'required': True
        },
        {
            'name': 'pressure',
            'type': 'string',
            'description': '锅炉的气压',
            'required': True
        },
        {
            'name': 'opt_parm',
            'type': 'string',
            'description': '锅炉的一个可选参数',
            'required': False
        }
    ]

    def call(self, params: str, **kwargs) -> str:
        # try:
        #     params = self._verify_json_format_args(params)
        #     boiler_temp = params["boiler_temp"]
        #     water_level = params["water_level"]
        #     pressure = params["pressure"]
        #     opt_parm = params["opt_parm"]
        # except:
        #     # will not enter this part, because will catched by function self._verify_json_format_args(params)
        #     return ResultBuilder.error("[BoilerAssessment] Invalid request format: Input must be a JSON object containing 'boiler_temp'、'water_level'、'pressure' field")

        boiler_temp = json5.loads(params)['boiler_temp']
        water_level = json5.loads(params)['water_level']
        pressure = json5.loads(params)['pressure']

        # TODO: get parms actual values: could from existed sensors, could from llm, also could be the hard code default value.
        fake_score = "89"
        result = f"According to the conditions that boiler's temperature is {boiler_temp}, water lever is {water_level}, and the pressure is {pressure}, the ultimate result is {fake_score}."
        return result

if __name__ == "__main__":
    print(BoilerAssessment().call('''{"boiler_temp": "60℃", "water_level": "220cm", "pressure":"27.3MPa", "opt_parm":"test"}'''))
