# 用自然语言快速生成图表
基于langchain与pyecharts实现

```python
from AIpyecharts import ChatModel,AIplot

# 连接大模型，没加api_key就是用环境变量"OPENAI_API_KEY"
model = ChatModel("qwen-turbo", "https://dashscope.aliyuncs.com/compatible-mode/v1")
```
目前支持图表：
## 柱状图（条形图）Bar

```python
data = {'x_axis' :['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'], 
        'y_axis': {'1':[114, 55, 27, 101, 125, 27],
                   '2':[1,2,3,4]} # 可设置多个数据
        # ‘render’: 'bar.html' # 可指定保存路径，如不指定，保存至当前工作区文件夹中
        }
plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二,x轴标题为x轴，y轴标题为y轴,使用滑块')
print(plt.get_chart("生成柱状图"))
```

配置支持：
* 主标题
* 副标题
* x轴名称
* y轴名称
* 图例横向位置，默认居中
* 图例纵向位置，默认顶层
* 是否开启工具箱（可保存图片、放大图表，堆叠转换，折线图转换等）
* x轴名称是否旋转,如果名称太长可以设置改参数，名称会旋转15度
* 是否进入选择模式,开启后可以进行框选、圈选等操作
* 是否开启滑块，开启后可调节x轴显示范围

## 折线图Line

```python
data = {'x_axis' :['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'], 
        'y_axis': {'1':[114, 55, 27, 101, 125, 27],
                   '2':[1,2,3,4]} # 可设置多个数据
        # ‘render’: 'line.html' # 可指定保存路径，如不指定，保存至当前工作区文件夹中
        }
plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二,x轴标题为x轴，y轴标题为y轴,开启工具箱')
print(plt.get_chart("生成折线图"))
```

配置支持：
* 主标题
* 副标题
* x轴名称
* y轴名称
* 图例横向位置，默认居中
* 图例纵向位置，默认顶层
* 是否开启工具箱（可保存图片、放大图表，堆叠转换，折线图转换等）

## 饼图（扇形图）Pie

```python
data = {'name':'饼图', # 饼图的名称
        'value':{'1':1,'2':2} # key为扇形的名称，按照值分配大小
        # ‘render’: 'pie.html' # 可指定保存路径，如不指定，保存至当前工作区文件夹中
        }
plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二')
print(plt.get_chart("生成饼图"))
```

配置支持：
* 主标题
* 副标题

## 漏斗图Funnel

```python
data = {'name':'漏斗图', # 漏斗图的名称
        'value':{'1':1,'2':2} # key为每层的名称，按照值分配大小
        # ‘render’: 'funnel.html' # 可指定保存路径，如不指定，保存至当前工作区文件夹中
        }
plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二，颠倒漏斗图')
print(plt.get_chart("生成漏斗图"))
```

配置支持：
* 主标题
* 副标题
* 是否颠倒漏斗图，颠倒后就是金字塔图

## 地理图Geo

```python
data = {'maptype':'浙江', # 选择地图
        'value':{'loc_name':'111', # 数据名称
                'loc_values':[('杭州',100),('宁波',200)], # 散点键值对
                'loc_pairs':[('杭州','宁波')]}} # 两个地区的连线键值对
plt = AIplot(model,plot_args=data,options='主标题为表一，副标题为表二,使用响应式散点')
print(plt.get_chart("生成地理图"))
```

配置支持：
* 主标题
* 副标题
* 是否使用响应式的散点

## 箱线图Boxplot

```python
v1 = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
        ]
v2 = [
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
        ]
data = {
        'x_axis': ['1', '2'],
        'y_axis': [{'name': '箱线图1', 'value': v1},
                        {'name': '箱线图2', 'value': v2}],
        'render': './AIpyecharts/example/boxplot.html'
}
plt = AIplot(model,plot_args=data,options='主标题为箱线图示例')
print(plt.get_chart("生成箱线图"))
```

配置支持：
* 主标题
* 副标题

## 3D柱状图Bar3D

```python
data = {
        'data':{
            'value':[(1,2,3),(4,5,6)],
            'x_label': [1,2,3,4,5,6],
            'y_label': [1,2,3,4,5,6]
        },
        'render': './AIpyecharts/example/bar3d.html'
    }
plt = AIplot(model,plot_args=data,options='主标题为3D柱状图示例')
print(plt.get_chart("生成3D柱状图"))
```

配置支持：
* 主标题
* 副标题

## 关系图Graph

```python
nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
        {"name": "结点5", "symbolSize": 50},
        {"name": "结点6", "symbolSize": 40},
        {"name": "结点7", "symbolSize": 30},
        {"name": "结点8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    data = {
        'data':{
            'nodes': nodes,
            'links': links,
            'repulsion': 8000
        },
        'render': './AIpyecharts/example/graph.html'
    }
plt = AIplot(model,plot_args=data,options='主标题为关系图示例')
print(plt.get_chart("生成关系图"))
```

配置支持：
* 主标题
* 副标题

## 散点图

```python
data = {
        'x_axis': [1,2,3,4,5,6],
        'y_axis':[{'name':'散点图1','value':[1,2,3,4,5,6]},
                {'name':'散点图2','value':[2,2,3,6,4,6]}],
        'render': './AIpyecharts/example/scatter.html'
        }
plt = AIplot(model,plot_args=data,options='主标题为散点图示例')
print(plt.get_chart("生成散点图"))
```

配置支持：
* 主标题
* 副标题

## 树图

```python
data = {
        'name': '树图',
        'data': [
                {
                    "children": [
                        {"name": "B"},
                        {
                            "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
                            "name": "C",
                        },
                        {
                            "children": [
                                {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                                {"name": "H"},
                            ],
                            "name": "D",
                        },
                    ],
                    "name": "A",
                }
            ],
        'render': './AIpyecharts/example/tree.html'
    }
plt = AIplot(model,plot_args=data,options='主标题为树图示例')
print(plt.get_chart("生成树图"))
```

配置支持：
* 主标题
* 副标题

## 词云图

```python
data = {
        'name': '词云图',
        'data':[
            ('关键词1', 10),
            ('关键词2', 20),
            ('关键词3', 30),
            ('关键词4', 40)
        ],
        'render': './AIpyecharts/example/wordcloud.html'
    }
plt = AIplot(model,plot_args=data,options='主标题为词云图示例')
print(plt.get_chart("生成词云图"))
```

配置支持：
* 主标题
* 副标题

## 20250806更新
增加散点图、树图、词云图

## 20250804更新
增加箱线图、3D柱状图、关系图

## 20250731更新
增加饼图和漏斗图，修改配置逻辑

## 20250730更新
增加折线图和柱状图，增加配置
