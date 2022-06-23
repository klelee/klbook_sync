#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import time

# 全局常量
BOOK_PATH = "/root/klbook_sync/"
BOOK_NAME = "klbook"

# 全局变量
dircount_kl = 1
new_sync_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
Author = "klelee"
Email = "klelee@outlook.com"
os.chdir(BOOK_PATH)
readme_kl = open("./README.md", "w")

def deal_dir(df):
    global dircount_kl
    dircount_kl = dircount_kl + 1

    readme_kl.write("#" * dircount_kl + " " + df + "   \n")

    os.chdir(df)
    temp_list = os.listdir("./")
    temp_list.sort()
    for temp in temp_list:

        if os.path.isdir(temp):
            deal_dir(temp)
        elif os.path.isfile(temp):
            deal_file(temp)
        else:
            print("can't palse this file or dir:")
    os.chdir("../")
    dircount_kl = dircount_kl - 1


def deal_file(df):

    readme_kl.write("-" + " " +
                    "[" + df + "](" + os.path.abspath(df) + ")" + "   \n")


def main():
    readme_kl.write("# klbook index   \n")
    readme_kl.write(Author + "   \n")
    readme_kl.write(Email + "   \n")
    readme_kl.write(new_sync_time + "   \n")
    
    dirlist_kl = os.listdir(BOOK_NAME)
    dirlist_kl.sort()

    for i in dirlist_kl:
        os.chdir(BOOK_PATH + BOOK_NAME)
        type_kl = os.path.isdir(i)

        if i == "images" or i == ".git":
            continue

        if type_kl:
            deal_dir(i)
        else:
            deal_file(i)


main()
readme_kl.close()
