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
        # ‘render’: 'pie.html' # 可指定保存路径，如不指定，保存至当前工作区文件夹中}
```

配置支持：
* 主标题
* 副标题

## 20250730更新
增加折线图和柱状图，增加配置
