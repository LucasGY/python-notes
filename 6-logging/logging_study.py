#%%
#日志级别的顺序是这样的：
# `CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET `
#
import logging
logging.basicConfig(level=logging.INFO, # 大于等于logging.INFO级别的都可以打印出来
                    format='%(asctime)s %(levelname)s: %(message)s' # 日期 时间|log级别|打印内容|
                    )
logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

#%% 创建一个新的logger，不是root
# 创建一个新的apps 的logger， 如果logger不设置，就会用root logger那套（打印到屏幕和上面的格式）
# 因为它是会默认传播到祖先logger
logger = logging.getLogger('apps')
logger.setLevel(logging.DEBUG)
# 是否传播这个日志到祖先logger, 如果设置了False 就不会传到root logger(祖先Logger)的
# 默认StreamHandler那里， 也就是不会打印在页面上
logger.propagate = False
# 添加handler, 决定日志落地到哪里，可以多个
# 这个是记录在文件的Handler
apps_handler = logging.FileHandler(filename="apps.log")
# 设置这个handler的处理格式， 实例化一个Formatter对象
apps_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
apps_handler.setFormatter(apps_formatter)
logger.addHandler(apps_handler)
# 日志会打印到apps.log, 并且不会输出到屏幕（如果logger.propagate=True就会）
logger.debug('shit')
#%%--------------------------------------------------------
logger = logging.getLogger('try_demo')
logger.setLevel(logging.DEBUG)
logger.propagate = False
file_handler = logging.FileHandler(filename='try_demo.log')
apps_formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')

file_handler.setFormatter(apps_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(apps_formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.debug('shit')