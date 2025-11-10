import json

from sqlglot.expressions import JSONObject

def error(error_content:str) -> str:
    """

    :param error_content: the error content to show when error happen.
            E.g. "Invalid request format: Input must be a JSON object containing 'sec_assess_tool' field"

    :return:
            E.g.
                {
                    "Error":"Invalid request format: Input must be a JSON object containing 'sec_assess_tool' field"
                }
    """
    error_obj = f'''{"Error":"{error_content}"} '''
    return error_obj




