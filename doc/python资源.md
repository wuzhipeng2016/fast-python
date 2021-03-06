1.Sanic  
Sanic的概念非常简单：提供一套基于Flask语法的Web框架，但同时将Python 3.5及更高版本中的极速异布事件处理程序纳入其中。结果就是，这款框架能够将Flask原本的每秒4988项请求处理能力瞬间提升至33000项以上，而延迟亦削减至原本的十分之一。其中亦包含路由与中间件。我们还不清楚现有应用是否已经开始大规模利用Sanic替代Flask，但只要亲身尝试，大家就会发现其可观的速度提升效果。  
2.Eve  
如果大家希望构建Web服务，并利用快速方法使用各类已知组件，那么Eve正是为此而生。其利用Flask作为Web框架，同时可接入MongoDB、SQL-Alchemy、Elasticsearch或者Neo4js后端以实现数据访问。该项目的开发者反复强调其部署简易性：要实现在线API，您只需要一套数据库、一个配置文件（默认为settings.py）以及一套启动脚本。  
3.Morepath  
Morepath宣称其是一套“超级强大”的Python Web框架，且仅需要最低设置空间。其设计目标在于让各类典型用例得以快速启动与运行，其中包括将常见Python数据结构转换为RESTful Web服务。其还拥有一项特殊功能：它能够自动将Morepath中定义的路径转换为链接，从而创建出具备简洁URL的应用。  
4.ButterflyNet  
如果大家希望拥有一套能够默认实现异步性与安全性的网络库，那么ButterflyNet绝对值得一试。其仅支持Python 3.5及更高版本，因为其使用asyncio库以实现自身功能，但能够仅利用十余行代码即设置起服务器并为其提供必要的证书与密钥。感兴趣的朋友可以点击此处查看一套聊天室示例，仅需75行代码即可实现。  
5.Uvloop        
凭借着“迅如闪电的Python网络”这一宣传口号，我们实在很难忽视Uvloop的存在。Uvloop属于asyncio事件循环的替代性方案，因此其既可作为全新基于asyncio应用的运行基础，亦可在现有应用中直接替代asyncio。它还获能够与Python加速机制Cython进行协作，因此其关键部分代码实际上是由C语言编写的。其缔造者声称，它“在速度上至少比Node.js、gevent以及其它任何Python异步框架快2倍”，不过大家最好实际测试以了解其具体效果。        

flask资源：  
http://www.pythondoc.com/flask-mega-tutorial/index.html  

Python是目前最流行、最易学最强大的编程语言之一（学习Python的五大理由），无论你是新手还是老鸟，无论是用于机器学习还是web开发（Pinterest就是案例），Python都是一件利器。此外，Python不但人气日益高涨，而且Python程序员的薪酬行情也是水涨船高，北美Python程序员的平均年薪高达10万美元。
对于有志学习Python的开发者来说，Python吸引人的地方不仅是有一个优秀的社区，而且还有大量的精品免费资源可用。连环创业家，Code（Love）创始人Roger Huang近日分享了11个优秀的Python学习资源，IT经理网编译如下：
一、Python优秀书籍
《Learn Python the Hard Way》的作者将书中的内容制作成网络教程免费提供，包括很多值得花时间完成的习题，只有多写代码，你才能从菜鸟变成老鹰。
二、Python教学视频
如果你习惯视频学习，那么可以考虑选择Udacity的Python for the Web免费课程，通过学习该课程，你将对web数据的流转有着更深入的认识。
三、Github上的Python资源库
Github上有大量优质的Python资源库，例如这个。
四、Anaconda与iPython Notebook
Anaconda和iPython Notebook可以看作是Python的“Excel”。通常Python的代码很难通过HTML等web格式分享，尤其是展示涉及不同脚本中的图表做成的结构化flow。Anaconda和iPython Notebook可以直观可视化的方式组织关联不同Python软件模块，在nbviewer中轻松展示结果，并且还能生成HTML版本的Notebook文件便于在Github上分享。
五、用Pandas处理大数据
Pandas的开发基于前面提到的iPython Notebook，Python只能帮你处理加载到内存中的数据，Pandas可以让你高效读取更大规模数据，例如海量的CSV文件，进行数据清洗并用于数据透视或者可视化。
六、用Flask开发小型程序
Flask是一个微框架，你可以用它来开发一些小型web项目，Flask包含了互动网站项目常用的一些可复用的数据通讯模块，只需要几行代码，你就能生成一个互动功能。
七、用Django开发大型项目
如果你想开发一个完整的web框架，那么就试试Django吧，很多Pinterests和Instagram这样的超大规模网站都是用Django开发的。
八、用Python玩转API
API是web经济的支柱之一，这里介绍一个Python 第三方API精华列表，你可以用Python调用那些很酷的数据，让你的应用与众不同。
九、Python的机器学习资源库
这个Github上的Python机器学习库提供大量优秀资源，让你快速入门。
十、Plotly帮你用数据讲故事
柴静的雾霾演讲为什么火？因为她用数据讲故事呗。只需几行代码，你就能用Plot.ly生成各种常见数据图表。
十一、测试你的Python段位
当你自以为学得差不多了，开始膨胀的时候，就可以考虑去HackerRank测试一下你的“段位”，高段位的还有可能值得获得工作机会哟。
https://wiki.wxpython.org/AnotherTutorial
