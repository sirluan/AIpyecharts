from langchain_core.tools import tool
from pyecharts.charts import Bar
@tool
def bar():
    '''
    柱状图生成工具，生成柱状图
    '''
def plot_bar(plot_args):
    bar = Bar()
    bar.add_xaxis(plot_args['x_axis'])
    bar.add_yaxis(plot_args['total'],plot_args['y_axis'])
    if 'render' in plot_args: bar.render(plot_args['render'])
    else: bar.render("bar.html")