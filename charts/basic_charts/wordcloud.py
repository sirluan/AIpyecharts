from langchain_core.tools import tool
from pyecharts.charts import WordCloud
from pyecharts import options as opts
from dataclasses import dataclass,asdict
from ..options import AIoptions
@tool
def wordcloud():
    '''
    词云图生成工具，生成词云图
    '''

@dataclass
class WordCloud_opts:
    title: str = ""
    sub_title: str = ""

template = """
        1. title: 主标题,默认为空字符串
        2. subtitle: 副标题,默认为空字符串"""
def plot_wordcloud(model,plot_args,options):
    chart = WordCloud()
    wordcloud_opts = WordCloud_opts()
    options = AIoptions(model,template=template,opt_keys=asdict(wordcloud_opts),message=options).opts
    chart.add(plot_args['name'],plot_args['data'],word_size_range=[6,66])
    if options:
        chart.set_global_opts(
            title_opts=opts.TitleOpts(title=options['title'], subtitle=options['sub_title']))
        
    
    if 'render' in plot_args: chart.render(plot_args['render'])
    else: chart.render("wordcloud.html")
    return '词云图生成成功'
