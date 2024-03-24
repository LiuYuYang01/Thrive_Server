class ProjectModel(object):
    title = "Thrive"  # 网站标题
    subhead = "花有重开日, 人无再少年"  # 网站副标题
    logo = "https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640"  # 网站图标
    description = "记录前端、Python、Java点点滴滴"  # 网站描述
    keyword = ['Thrive', '前端', 'Python', 'Java']  # 网站SEO关键词


class LayoutModel(object):
    isTheme = False
    isArticleLayout = "classics"
    rightSidebar = ["author", "hotArticle", "randomArticle", "newComments"]
    swiperImage = "https://liuyuyang.net/img/20ac414805e3491098df678d3d9f100f_KJCPUs.jpg"
    swiperText = ['System.out.print("有些梦虽然遥不可及，但并不是不可能实现!");',
                  'print(" 互联网从不缺乏天才, 而努力才是最终的入场券!")',
                  'console.log("再渺小的星光，也有属于他的光芒!")']
