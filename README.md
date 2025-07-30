# 用自然语言快速生成图表
基于langchain与pyecharts实现

```python
data = {'x_axis' :['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'], 
        'y_axis': {'1':[114, 55, 27, 101, 125, 27],'2':[1,2,3,4]}}

# 连接大模型，没加api_key就是用环境变量"OPENAI_API_KEY"
model = ChatModel("qwen-turbo", "https://dashscope.aliyuncs.com/compatible-mode/v1")

# 可以设置图表配置
options = AIoptions(model).call_tools('主标题为表一，副标题为表二,x轴标题为x轴，y轴标题为y轴,使用工具箱')
plt = AIplot(model,plot_args=data,options=options)

# 用自然语言生成图表，会生成html文件，可交互
print(plt.get_chart("生成柱状图"))
```
目前支持图表：
* 柱状图（条形图）
* 折线图

配置支持：
* 主标题
* 副标题
* x轴名称
* y轴名称
* 图例横向位置，默认居中
* 图例纵向位置，默认顶层
* 是否开启工具箱（可保存图片、放大图表，堆叠转换等）

## 20250730更新
增加折线图和柱状图，增加配置
