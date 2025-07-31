from dataclasses import asdict
from langchain_core.prompts import ChatPromptTemplate




class AIoptions:
    def __init__(self, model,template: str,opt_keys,message: str):
        self.model = model
        self.template = template
        self.opt_keys = opt_keys
        self.message = message
        self.opts = self.call_tools()
    def chat_model(self):
        default_template = """
        你是图表配置解析工具，请根据用户输入的图表配置，生成图表配置，
        可以配置的参数有："""+self.template+"""
        返回一个字符串，将所有参数的值值用|分隔，如果有十个参数就应该有九个|分隔它们，如果用户没有提供相关信息，用默认值填充，如果用户提供了，就用用户提供的信息。
        然后调用图表解析工具opt_tool
        输入信息为：{input}，
        不要返回多余的字符，不要返回思考过程
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
        opts = {i:j for i,j in zip(self.opt_keys.keys(),opts)}
        return opts

    def call_tools(self):
        model_output = self.chat_model().invoke({"input": self.message})
        content = model_output.content
        opts = self.opt_tool(content)
        return opts
    
    
