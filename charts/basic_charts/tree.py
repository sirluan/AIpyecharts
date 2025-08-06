from langchain_core.tools import tool
from pyecharts.charts import Tree
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def tree():
    '''
    树图生成工具，生成树图
    '''

@dataclass
class Tree_opts:
    title: str = ""
    sub_title: str = ""

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_tree(model,plot_args,options):
    chart = Tree()
    tree_opts = Tree_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(tree_opts),message=options).opts
    chart.add(plot_args['name'],plot_args['data'])
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("tree.html")
    return '树图生成成功'
