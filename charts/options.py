from dataclasses import asdict
from langchain_core.prompts import ChatPromptTemplate

class AIoptions:
    def __init__(self, model,template: str,opt_keys,message: str):
        self.model = model
        self.template = template
        self.opt_keys = opt_keys
        self.message = message
        self.opts = self._call_tools()
    def chat_model(self):
        default_template = """
        你是图表配置解析工具，请根据用户输入的图表配置，生成图表配置，
        可以配置的参数有："""+self.template+"""
        返回一个字符串，将所有参数的值值用|分隔，开头和末尾不需要添加
        如果用户没有提供相关信息，用默认值填充，如果用户提供了，就用用户提供的信息。
        输入信息为：{input}，
        其中的序号不是输出数组中的索引，按顺序排列输出即可
        不要返回多余的字符，不要返回思考过程
        """
        prompt = ChatPromptTemplate.from_template(default_template)
        chain = prompt | self.model
        return chain
    
    def _opt_tool(self,opts:str):
        '''
        图表解析工具
        '''
        opts = opts.strip('\"')
        opts = opts.split("|")
        opts = [i.strip('\"') for i in opts]
        opts = {i:j for i,j in zip(self.opt_keys.keys(),opts)}
        return opts

    def _call_tools(self):
        model_output = self.chat_model().invoke({"input": self.message})
        content = model_output.content
        opts = self._opt_tool(content)
        return opts
    