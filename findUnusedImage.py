#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个文件的目的就是查找项目中没有用到的图片  现在只有。m 文件的查找方式  关于 storyboard 和 xib 的方式 要看 xml 的格式在做尝试

import os

def dirlist(path):
    filelist = os.listdir(path)
    for filename in  filelist:
        fileabsoulutepath = os.path.join(path,filename)
        if os.path.isdir(fileabsoulutepath):
            # 这里就是是文件夹的路径的情况 需要递归的向下继续寻找
            dirlist(fileabsoulutepath)
        else:
            #这里只需要查找是 .m 后缀的文件 和 resource 文件 从 Resource 文件中读取出现在有的图片 （可能有@2x和@3x的问题需要去重 其实觉得更合理的方案是 截取前半部分）
            if matchFlle(fileabsoulutepath):
                findImage(fileabsoulutepath)
            elif assertsIsInbundle == 0:
                if matchImage(fileabsoulutepath):
                    findimageSet.add(fileabsoulutepath)


import re
#这个是匹配 .m 文件
def matchFlle(fileName):

    if re.match(matchFlie,fileName):
        return True
    else:
        return False

#这个是匹配资源文件
def matchImage(filename):
    return re.match(matchResourceFile,filename)


#从文件中读取内容然后做一个正则匹配
def findImage(filename):
    with open(filename,'r') as file:
        filecontent = file.read()
        #这里就需要根据项目的不同进行个性化的设置了
        results = re.findall(matchImageMatcher, filecontent)
        if results.count() > 0:
            for imageName in results:
                # 找到的时候的情况
                assertimageSet.add(imageName)

#比较  找出没有被使用的图片
def getUnusedImage():
    resultSet = assertimageSet - findimageSet
    print('未使用的图片集是 %s' % [x for x in resultSet])

assertimageSet = set()
findimageSet = set()

def main():
    dirlist(projectfilepath)



if __name__ == '__main__':
    import re
    import os
    #在这里提前注入要需要处理的所有正则匹配
    matchFlie = re.compile(r'[.]m$')

    # 这个是查找资源文件的方案
    # print('如果你的项目中加入时候加入 png 或者 jpg 传入1 如果不带传入 0')
    # searchType = input('please input you project search wheather with suffix png or jpp:')
    # matchResourceFile = ''
    # if searchType :
    #     matchResourceFile = re.compile(r'[\.](png|jpg)$')
    # else:
    matchResourceFile = re.compile(r'([*]+)[\.](png|jpg)$')

    # 根据个人项目传入正则匹配的方案 如果需要根据业务自定义正则匹配传入对应的 python 格式正则即可

    print('if you need extra config image match scheme based on your project ，you need input 1 otherwise input 0')

    matchImageMatcher = ''
    imageSearchScheme = input('please input you image match config:')
    if imageSearchScheme :
        print('next you need input image match scheme as r\'*.img\'')
        otherSearchScheme = input('please input your image match scheme:')
        matchImageMatcher = re.compile(otherSearchScheme)
    else:
        #常见的系统方法匹配方案
        matchImageMatcher = re.compile(r'pathForResource:@"([*])"|imageWithNamed:@"([*]+)"');

    projectfilepath = input('please input your project absoulute path:').strip()

    # 判断是否需要 bundle 的模式去检测  如果是 bundle 传入 1 否则传入 0
    assertsIsInbundle = input('if you asserts in bundle please input 1 else input 0:')

    if assertsIsInbundle == 1:
        assertsPath = input('please input in you bundle or imageResource absolute path:')
        dirlist(assertsPath)

    main()
