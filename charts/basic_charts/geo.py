from langchain_core.tools import tool
from pyecharts.charts import Geo
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
from pyecharts.globals import ChartType
@tool
def geo():
    '''
    地理图生成工具，生成地理图
    '''

@dataclass
class Geo_opts:
    title: str = ""
    sub_title: str = ""
    is_effect: bool = False
    legend_pos: str = None


template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串
        3. is_effect: 是否使用响应式的散点,布尔值,默认为False
        4. legend_pos: 图例位置,str类型,默认为None,表示居中,如果是left表示靠左,如果是right表示靠右"""
def plot_geo(model,plot_args,options):
    chart = Geo()
    geo_opts = Geo_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(geo_opts),message=options).opts
    chart.add_schema(maptype=plot_args['maptype'])
    if 'value' in plot_args:
        chart.add(series_name=plot_args['value']['loc_name'] if 'loc_name' in plot_args['value'] else '',
                    data_pair = plot_args['value']['loc_values'],
                    type_= ChartType.EFFECT_SCATTER if options and options['is_effect'] != 'False'  else 'scatter')
        if 'loc_pairs' in plot_args['value']:
            chart.add(series_name=plot_args['value']['line_name'] if 'line_name' in plot_args['value'] else '',data_pair = plot_args['value']['loc_pairs'],type_=ChartType.LINES)
        
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']),
            legend_opts=opts.LegendOpts(pos_left=options['legend_pos'],pos_top='center',orient='vertical')if options['legend_pos'] != 'None' else opts.LegendOpts())
    
    return chart
