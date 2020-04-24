# selenium+scrapy混合抓取动态渲染后的数据
### Target: QQ音乐流行指数排行Top20
### Output: JSON
### 抓包截图:
![img1](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424164028.png)
### 关键说明:
##### 1，输出为json，为避免中文乱码问题，scrapy中的settings添加以下字段来修正:
![img2](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424163906.png)
##### 2, 创建main入口，快速运行scrapy项目，注意参数"-o qq.json"
![img3](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424163919.png)
##### 3, 关键代码截图:
![img4](https://github.com/ziliang-wang/qq/blob/master/images/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200424164403.png)

