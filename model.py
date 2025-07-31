from charts.basic_charts import *
from tools import Tools
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional


class ChatModel:
    def __init__(self, model_name: str, base_url: str, api_key: Optional[str] = None):
        self.model_name = model_name
        self.base_url = base_url
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ["OPENAI_API_KEY"]
        self.model = ChatOpenAI(
            model=self.model_name,
            base_url=self.base_url,
            api_key=self.api_key
        )

class AIplot:
    def __init__(self, model:ChatModel,template: str = "", plot_args: dict = {},options: str = ''):
        self.model = model.model
        self.template = template
        self.plot_args = plot_args
        self.options = options
        self.chain = self.chat_model()

    def chat_model(self):
        default_template = """
        你是图表生成工具，请根据用户输入的图表类型，选择合适的工具来生成图表。
        可以选择的工具有
        折线图生成工具、
        柱状图生成工具、
        饼图生成工具。
        输入信息为：{input}
        """
        prompt = ChatPromptTemplate.from_template(default_template+self.template)
        model_with_tools = self.model.bind_tools(Tools.values())
        chain = prompt | model_with_tools
        return chain

    def call_tools(self, model_output):
        tool_call = model_output.tool_calls[0]
        if tool_call['name'] == 'line': response = plot_line(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'bar': response = plot_bar(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'pie': response = plot_pie(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'funnel': response = plot_funnel(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'geo': response = plot_geo(self.model,self.plot_args,self.options)
        else: raise('无法解析图表')
        return response

    def get_chart(self, input_str):
        model_output = self.chain.invoke({"input": input_str})
        print(model_output)
        return self.call_tools(model_output)
    
    def set_opts(self, options):
        self.options = options

if __name__ == "__main__":
    # data = {'x_axis' :['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'], 
    #         'y_axis': {'1':[114, 55, 27, 101, 125, 27],'2':[1,2,3,4]}}
    
    # data = {'name':'饼图','value':{'1':2000,'2':3050}}
    data = {'maptype':'浙江','value':{'loc_name':'111','loc_values':[('杭州',100),('宁波',200)],'loc_pairs':[('杭州','宁波')]}}
    model = ChatModel("deepseek-v3", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二,使用响应式散点')
    print(plt.get_chart("生成地理图"))


