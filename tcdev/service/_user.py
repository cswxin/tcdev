#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group

import logging
logger = logging.getLogger('logger')

#===============================================================================
# Model的直接操作方法，get_or_create、get、filter 等。
#===============================================================================
def create_user_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: 元组(obj,boolean)
    @note: 获取或创建  对象
    '''
    return User.objects.create(**kwargs)


def get_or_create_user_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: 元组(obj,boolean)
    @note: 获取或创建  对象
    '''
    return User.objects.get_or_create(**kwargs)

def get_user_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: obj或None
    @note: 获取  对象
    '''
    try:
        return User.objects.get(**kwargs)
    except User.DoesNotExist:
        logger.error(u"Account对象不存在（%s）" % kwargs)
    except User.MultipleObjectsReturned:
        logger.error(u"Account对象存在多条记录（%s）" % kwargs)
    return None

def get_users_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: [obj,]
    @note: 获取  对象列表
    '''
    return User.objects.filter(**kwargs)

#===============================================================================
# Model的直接操作方法，get_or_create、get、filter 等。
#===============================================================================
def create_group_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: 元组(obj,boolean)
    @note: 获取或创建  对象
    '''
    return Group.objects.create(**kwargs)


def get_or_create_group_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: 元组(obj,boolean)
    @note: 获取或创建  对象
    '''
    return Group.objects.get_or_create(**kwargs)

def get_group_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: obj或None
    @note: 获取  对象
    '''
    try:
        return Group.objects.get(**kwargs)
    except Group.DoesNotExist:
        logger.error(u"Group对象不存在（%s）" % kwargs)
    except Group.MultipleObjectsReturned:
        logger.error(u"Group对象存在多条记录（%s）" % kwargs)
    return None

def get_groups_by_params(**kwargs):
    '''
    @param kwargs: key=value 的键值对
    @return: [obj,]
    @note: 获取  对象列表
    '''
    return Group.objects.filter(**kwargs)