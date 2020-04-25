# selenium+PhantomJS+scrapy混合抓取动态渲染后的数据
### Target: QQ音乐流行指数排行Top20
### Output: JSON格式，web/app/微信小程序的数据源，公开API的数据源等
### 抓包截图:
![img1](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424164028.png)
### 关键说明:
##### 1，输出为json，为避免中文乱码问题，scrapy中的settings添加以下字段来修正:
![img2](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424163906.png)
##### 2, 创建main入口，快速运行scrapy项目，注意参数"-o qq.json"
![img3](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424163919.png)
##### 3, 关键代码截图:
![img4](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424164403.png)
###### a, 时长部份不在json字段里，故以selenium驱动phantomJS来抓取，抓取前，将item中的time字段设为默认00:00，也可以不赋值，之后遍历时可以再添加
###### b, 将json数据赋给item后，另建item_list列表，原item对象非标准字典，以dict(item)转成dict后再添加至list，最终为"嵌套字典的列表"
###### c, 最后以selenium抓取时长数据，循环取出item_list内的字典后，再以xpath取出来的文本数据赋值给字典内的time字段，再yield给scrapy引擎
##### 4，输出:
![img5](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424164329.png)

