from .charts.basic_charts import *
from .tools import Tools
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
        elif tool_call['name'] == 'boxplot': response = plot_boxplot(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'bar3d': response = plot_bar3d(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'graph': response = plot_graph(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'scatter': response = plot_scatter(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'tree': response = plot_tree(self.model,self.plot_args,self.options)
        elif tool_call['name'] == 'wordcloud': response = plot_wordcloud(self.model,self.plot_args,self.options)
        else: raise('无法解析图表')
        return response

    def get_chart(self, input_str):
        model_output = self.chain.invoke({"input": input_str})
        return self.call_tools(model_output)
    
    def set_opts(self, options):
        self.options = options

if __name__ == "__main__":
    model = ChatModel("deepseek-v3", "https://dashscope.aliyuncs.com/compatible-mode/v1")

    # 饼图
    # data = {'name':'饼图','value':{'类别一':2000,'类别二':3050}}
    # plt = AIplot(model,plot_args=data,options='主标题为饼图示例，使用圆环状展示，图例靠左')
    # plt.get_chart("生成饼图").render('./AIpyecharts/example/pie.html')

    # 箱线图
    # v1 = [
    #     [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
    #     [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
    # ]
    # v2 = [
    #     [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
    #     [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
    # ]
    # data = {
    #     'x_axis': ['1', '2'],
    #     'y_axis': [{'name': '箱线图1', 'value': v1},
    #                {'name': '箱线图2', 'value': v2}]
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为箱线图示例')
    # plt.get_chart("生成箱线图").render('./AIpyecharts/example/boxplot.html')

    # 3D 柱状图
    # data = {
    #     'data':{
    #         'value':[(1,2,3),(4,5,6)],
    #         'x_label': [1,2,3,4,5,6],
    #         'y_label': [1,2,3,4,5,6]
    #     }
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为3D柱状图示例')
    # plt.get_chart("生成3D柱状图").render('./AIpyecharts/example/bar3d.html')

    # 关系图
    # nodes = [
    #     {"name": "结点1", "symbolSize": 10},
    #     {"name": "结点2", "symbolSize": 20},
    #     {"name": "结点3", "symbolSize": 30},
    #     {"name": "结点4", "symbolSize": 40},
    #     {"name": "结点5", "symbolSize": 50},
    #     {"name": "结点6", "symbolSize": 40},
    #     {"name": "结点7", "symbolSize": 30},
    #     {"name": "结点8", "symbolSize": 20},
    # ]
    # links = []
    # for i in nodes:
    #     for j in nodes:
    #         links.append({"source": i.get("name"), "target": j.get("name")})
    # data = {
    #     'data':{
    #         'nodes': nodes,
    #         'links': links,
    #         'repulsion': 8000
    #     }
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为关系图示例')
    # plt.get_chart("生成关系图").render('./AIpyecharts/example/graph.html')

    # 散点图
    # data = {
    #     'x_axis': [1,2,3,4,5,6],
    #     'y_axis':[{'name':'散点图1','value':[1,2,3,4,5,6]},
    #               {'name':'散点图2','value':[2,2,3,6,4,6]}]
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为散点图示例,开启工具箱，开启选择模式，开启滑块')
    # plt.get_chart("生成散点图").render('./AIpyecharts/example/scatter.html')

    # 树图
    # data = {
    #     'name': '树图',
    #     'data': [
    #             {
    #                 "children": [
    #                     {"name": "B"},
    #                     {
    #                         "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
    #                         "name": "C",
    #                     },
    #                     {
    #                         "children": [
    #                             {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
    #                             {"name": "H"},
    #                         ],
    #                         "name": "D",
    #                     },
    #                 ],
    #                 "name": "A",
    #             }
    #         ]
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为树图示例')
    # plt.get_chart("生成树图").render('./AIpyecharts/example/tree.html')

    # 词云图
    # data = {
    #     'name': '词云图',
    #     'data':[
    #         ('关键词1', 10),
    #         ('关键词2', 20),
    #         ('关键词3', 30),
    #         ('关键词4', 40)
    #     ]
    # }
    # plt = AIplot(model,plot_args=data,options='主标题为词云图示例')
    # plt.get_chart("生成词云图").render('./AIpyecharts/example/wordcloud.html')