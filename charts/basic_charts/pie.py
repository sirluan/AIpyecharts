from langchain_core.tools import tool
from pyecharts.charts import Pie
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def pie():
    '''
    饼图/扇形图生成工具，生成饼图
    '''

@dataclass
class Pie_opts:
    title: str = ""
    sub_title: str = ""
    is_radius: bool = False
    legend_pos: str = None

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. is_radius: 是否改为圆环状,默认为False
        4. legend_pos: 图例位置,str类型,默认为None,表示居中,如果是left表示靠左,如果是right表示靠右"""
def plot_pie(model,plot_args,options):
    chart = Pie()
    pie_opts = Pie_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(pie_opts),message=options).opts
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos'],pos_top='center',orient='vertical')if options['legend_pos'] != 'None' else opts.LegendOpts())
    chart.add(plot_args['name'], [list(i) for i in plot_args['value'].items()],radius=['40%', '75%'] if options['is_radius'] != 'False' else None)
    
    return chart
