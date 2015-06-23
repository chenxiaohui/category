#!/usr/bin/python
#coding=utf-8
#Filename:category.py
import config
import sys,os
import shutil
import glob

def get_dir_list(basedir):
    """"""
    return [directory[len(basedir):] for directory in glob.glob(basedir + "/*" ) if os.path.isdir(directory)]

def print_result(word_result):
    """"""
    idx = 0
    for word in word_result:
        print idx, word
        idx+=1
    return word_result

def select_path(base_dir):
    """"""
    category=""
    result = get_dir_list(base_dir)
    if result:
        result.extend(config.extra)
        result = print_result(result)
        try:
            raw = raw_input("select a most probably one: \n")
            option = '.' if raw == '.' else int(raw)
        except Exception , e:
            print "Input data error"
            raise e

        if option >= 0 and option < len(result) or option == '.':
            category = '.' if option == '.' else result[option]

            if category == "自定义":
                print ("请输入："),
                category = raw_input()
            if config.prompt:
                print ("Sure to copy to category %s? (Y/n)"%category)
                confirm = raw_input()
                if confirm.upper() !='Y' and confirm !='':
                    return
    return category

def process_one_file(filepath):
    """"""
    fpath, fname = os.path.split(filepath)
    filename, ext=os.path.splitext(fname)
    category = select_path(config.base_dir)

    sub_category = select_path(config.base_dir + category + "/")
    try:
        category_file(filepath, category+"/"+sub_category)
    except Exception , e:
        print "failed to copy file to category"
        raise e

def detect_base_dir():
    """"""
    if not config.base_dir:
        raise config.ConfigException
    if not os.path.exists(config.base_dir):
        try:
            os.mkdir(config.base_dir)
        except Exception , e:
            print "failed to create dir"
            raise e

def category_file(file_path, dest_dir):
    """"""
    print file_path, dest_dir
    if not config.base_dir:
        raise config.ConfigException
    try:
        #dest_path = os.path.join(config.base_dir, dest_dir)
        dest_path = "%s/%s" %(config.base_dir, dest_dir)
    except Exception , e:
        print "failed to get dest path"
        raise e
    if not os.path.exists(dest_path):
        try:
            os.mkdir(dest_path)
        except Exception , e:
            print "failed to create dir"
            raise e

    ln_cmd = "ln -s  '%s/%s' '%s'"% (dest_path, filepath, filepath)

    if config.del_after_copy:
        copy_cmd = "mv '%s' %s"% (file_path, dest_path)
        try:
            shutil.move(filepath, dest_path)
            os.system(ln_cmd)
        except Exception , e:
            print "Error" + str(e)
    else:
        copy_cmd = "cp '%s' %s"% (file_path, dest_path)
        try:
            shutil.copy(filepath, dest_path)
        except Exception:
            print "Error"+ str(e)


    print copy_cmd
    print ln_cmd

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Help: python category.py <filename|filelist>"
    else:
        try:
            detect_base_dir()
        except Exception , e:
            print "failed to dected base dir"
        del sys.argv[0]
        for filepath in sys.argv:
            print "----------------------%s----------------------"%filepath
            process_one_file(filepath)
