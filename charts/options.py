from dataclasses import dataclass
from langchain_core.prompts import ChatPromptTemplate

@dataclass
class Init_opts:
    title: str = ""
    sub_title: str = ""
    x_axis_label: str = ""
    y_axis_label: str = ""
    legend_pos_left: str = "center"
    legend_pos_top: str = "top"
    toolbox_opts:bool = False


class AIoptions:
    def __init__(self, model):
        self.model = model.model
    def chat_model(self):
        default_template = """
        你是图表配置解析工具，请根据用户输入的图表配置，生成图表配置，
        可以配置的参数有：
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. x轴名称,默认为空字符串
        4. y轴名称,默认为空字符串
        5. lengend_pos_left:图例横向位置, 默认为'center'
        6. lengend_pos_top: 图例纵向位置，默认为'top'
        7. toolbox_ops: 工具箱配置,布尔型，默认为False
        返回一个字符串，将所有值用'|'分隔，如果用户没有提供相关信息，用默认值填充，如果用户提供了，就用用户提供的信息。
        然后调用图表解析工具opt_tool
        输入信息为：{input}
        """
        prompt = ChatPromptTemplate.from_template(default_template)
        chain = prompt | self.model
        return chain
    
    def opt_tool(self,opts:str):
        '''
        图表解析工具
        '''
        opts = opts.strip('\"')
        opts = opts.split("|")
        opts = [i.strip('\"') for i in opts]
        return opts

    def call_tools(self, message):
        model_output = self.chat_model().invoke({"input": message})
        content = model_output.content
        opts = self.opt_tool(content)
        return opts
    
    
