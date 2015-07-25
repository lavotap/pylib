#!/usr/bin/env python
#-*-coding:utf-8-*-

import re
import os

class File(object):
    @classmethod
    def match_extend(self,path='',file_names=[],extend_names=[]):
        if type(file_names)!=list:
            exit('ERROR:<match_extend@File>:Argument file_names must be list!')

        if type(extend_names)!=list:
            exit('ERROR:<match_extend@File>:Argument extend_names must be list!')

        en=''
        if extend_names:
            for x in extend_names:
                en=en+x+'$|'
            en=en[0:-1]
        is_extend_name=re.compile('^.*?[.](?='+en+')')

        files=[]
        for file in file_names:
            if os.path.exists(path+'/'+file):
                if is_extend_name.match(file):
                    files.append(file)
            else:
                exit('ERROR:<match_extend@File>:File '+str(file)+' is not exists!')
        return files

    @classmethod
    def match_attrib(self,path='',file_names=[],attrib=''):
        if type(file_names)!=list:
            exit('ERROR:<match_attrib@File>:Argument file_names must be list!')

        files=[]
        for file in file_names:
            if os.path.exists(path+'/'+file):
                if attrib=='f' or attrib=='file':
                    if os.path.isfile(path+'/'+file):
                        files.append(file)
                elif attrib=='d' or attrib=='dir' or attrib=='direction':
                    if os.path.isdir(path+'/'+file):
                        files.append(file)
                elif attrib=='':
                    files.append(file)
                else:
                    exit('ERROR:<match_attrib@File>:Argument attrib is wrong!')
        return files

class Path(object):
    def __init__(self,work_path,store_path_length=0):
        if not os.path.exists(work_path):
            exit('ERROR:<__init__@Path>:Argument work_path '+str(work_path)+' is not exists!')
        elif not os.path.isabs(work_path):
            print('CAUTION:<__init__@Path>:Argument work_path '+str(work_path)+' is not a absolute path!')
        self.work_path=work_path
        self.store_paths=[]
        self.store_path_length=store_path_length
        self.front_paths=[]

    def get_path(self):
        return self.work_path

    def show_path(self):
        print(self.get_path())
        return True

    def change_path(self,path):
        if not os.path.exists(path):
            exit('ERROR:<change_path@Path>:Argument work_path '+str(path)+' is not exists!')
        elif not os.path.isabs(path):
            print('CAUTION:<change_path@Path>:Argument work_path '+str(path)+' is not a absolute path!')

        if self.store_path_length==0:
            self.store_paths.append(self.work_path)
        else:
            if len(self.store_paths)==self.store_path_length:
                self.store_paths.pop(0)
            elif len(self.store_paths)>self.store_path_length:
                exit('ERROR:<change_path>:Length of store path is out of range!')
            self.store_paths.append(self.work_path)

        self.work_path=path
        return True

    def back(self):
        if len(self.store_paths)==0:
            print('CAUTION:<back@Path>:Can not go back!')
            return False

        if self.store_path_length==0:
            self.front_paths.append(self.work_path)
        else:
            if len(self.front_paths)==self.store_path_length:
                self.front_paths.pop(0)
            elif len(self.front_paths)>self.store_path_length:
                exit('ERROR:<back@Path>:Length of store path is out of range!')
            self.front_paths.append(self.work_path)

        self.work_path=self.store_paths[-1]
        self.store_paths.pop(-1)
        return True

    def front(self):
        if len(self.front_paths)==0:
            print('CAUTION:<front@Path>:Can not go front!')
            return False

        path=self.front_paths[-1]
        self.change_path(path)
        self.front_paths.pop(-1)
        return True

    def get_all_files(self):
        files=os.listdir(self.work_path)
        files.sort()
        return files

    def show_all_files(self):
        files=self.get_all_files()
        for f in files:
            print(f)
        return True

    def get_attrib_files(self,extend_names=[],attrib=''):
        files=self.get_all_files()
        if extend_names:
            files=File.match_extend(self.work_path,files,extend_names)
        if attrib:
            files=File.match_attrib(self.work_path,files,attrib)
        files.sort()
        return files

    def show_attrib_files(self,extend_names=[],attrib=''):
        files=self.get_attrib_files(extend_names,attrib)
        for f in files:
            print(f)
        return True
    
