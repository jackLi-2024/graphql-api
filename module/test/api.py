#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import sys
import json
import graphene

try:
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/../../" % cur_dir)

from module.test.model import M
from module.test.deal import deal_result


class Search(graphene.ObjectType):
    testResult = graphene.Field(M, description="查询测试样例名称")

    def resolve_testResult(self, info):
        if info.context.get("headers", {}).get("token"):
            token = info.context.get("headers", {}).get("token")
        else:
            token = None
        # raise Exception("错误")
        print(token)
        return deal_result()


class Operate(graphene.ObjectType):
    testResult = graphene.Field(M, description="查询测试样例名称")

    def resolve_testResult(self, info):
        if info.context.get("headers", {}).get("token"):
            token = info.context.get("headers", {}).get("token")
        else:
            token = None
        print(token)
        return deal_result()
