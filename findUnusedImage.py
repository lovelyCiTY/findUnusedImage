#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个文件的目的就是查找项目中没有用到的图片  现在只有。m 文件的查找方式  关于 storyboard 和 xib 的方式 要看 xml 的格式在做尝试

def dirlist(path):
    filelist = os.listdir(path)
    for filename in filelist:
        fileabsoulutepath = os.path.join(path,filename)
        if os.path.isdir(fileabsoulutepath):
            dirlist(fileabsoulutepath)
        else:
            #这里只需要查找是 .m 后缀的文件 和 resource 文件 从 Resource 文件中读取出现在有的图片 （可能有@2x和@3x的问题需要去重 其实觉得更合理的方案是 截取前半部分）
            if matchFlle(fileabsoulutepath):
                findImage(fileabsoulutepath)
            else:
                retult = matchImage(fileabsoulutepath)
                if retult:
                    findimageSet.add(retult)



#这个是匹配 .m 文件
def matchFlle(fileName):
    list = re.match(matchFlie, fileName)
    if not list:
        return False
    if len(list.groups()):
        return True
    else:
        return False

#这个是匹配资源文件
def matchImage(filename):
    list = re.match(matchResourceFile, filename)
    if list:
        filenameArray = list.groups()[0].split('/')
        result = filenameArray[-1].split('@')[0]
        return result
    return None


#从文件中读取内容然后做一个正则匹配
def findImage(filename):
    print(filename)
    with open(filename,'rb') as file:
        for filecontent in file.readlines():
        #这里就需要根据项目的不同进行个性化的设置了
            file = filecontent.strip()
            results = re.findall(matchImageMatcher, file.decode('utf-8'))
            if len(results) == 0 :
                continue
            print(results)
            for imagesResult in results:
                print(imagesResult)
                for imageString in imagesResult:
                    if imagesResult:
                        assertimageSet.add(imageString)

#比较  找出没有被使用的图片
def getUnusedImage():
    print('资源图片集 %s' % assertimageSet)
    print('使用图片集 %s' % findimageSet)

    resultSet = findimageSet - assertimageSet
    print('未使用的图片集是 %s' % [x for x in resultSet])



def main():
    dirlist(projectfilepath)
    getUnusedImage()



if __name__ == '__main__':
    import re
    import os
    #在这里提前注入要需要处理的所有正则匹配

    assertimageSet = set()
    findimageSet = set()

    matchFlie = re.compile(r'(.+?)[\.]m$')
    matchResourceFile = re.compile(r'(.+?)[\.](jpg|png)$')
    # 根据个人项目传入正则匹配的方案 如果需要根据业务自定义正则匹配传入对应的 python 格式正则即可
    print('下边是设置图片超找方案的选项，如果项目中自定义了宏或者进行了封装，就需要自定义正则匹配规则')
    matchImageMatcher = ''
    imageSearchScheme = input('设置图片匹配原则，系统方法传入0，自定义方法或者宏传入1:')
    print(imageSearchScheme)
    if imageSearchScheme == 1:
        # 只有上一步传入的为 1 才会走这个方法
        print('接下来设置你的图片的正则匹配方案 PS:这里切记传入的正则一定是非贪婪的 否则查找结果不准确')
        otherSearchScheme = input('请输入你的正则匹配方案:')
        matchImageMatcher = re.compile(otherSearchScheme)
    else:
        #常见的系统方法匹配方案
        matchImageMatcher = re.compile(r'pathForResource:@"(.*?)"|imageNamed:@"(.*?)"')

    projectfilepath = input('请输入你项目的完整路径:').strip()

    # # 判断是否需要 bundle 的模式去检测  如果是 bundle 传入 1 否则传入 0
    # assertsIsInbundle = input('如果你的图片存储在 bundle 中 无法直接读取，如果在 bundle 中传 1 在 Asserts 或者 本地文件夹中传 0 即可')
    # if assertsIsInbundle == 1:
    #     assertsPath = input('请输入本地图片 bundle 的完整路径:').strip()
    #     dirlist(assertsPath)



    # 现在想到的一些新的需求
    # 1.增加黑白名单机制 增加速度

    main()
