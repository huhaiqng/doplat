from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging
import time
import mysql.connector
from dingtalkchatbot.chatbot import DingtalkChatbot
from django.core.management import call_command
logger = logging.getLogger('django')


def dingding(mobile, text):
    webhook = 'https://oapi.dingtalk.com/robot/send?' \
              'access_token=da5e3827feba9cb2eed57dfb2a4d6272d92c6a331f377931f6e801a97b3f55ae'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title='禅道通知', text=text, at_mobiles=[mobile])


@shared_task
def notice_bug():
    logger.info('通知未解决的bug')
    cnx = mysql.connector.connect(user='root', password='JFwlkj2018!', buffered=True,
                                  host='192.168.40.159', database='zentaopms')
    users = cnx.cursor()
    bugs = cnx.cursor()

    users_sql = "SELECT u.realname, b.assignedTo, u.mobile, count(*) num FROM zt_bug b  \
                LEFT JOIN zt_product p ON b.product = p.id \
                LEFT JOIN zt_user u ON b.assignedTo = u.account \
                WHERE b.deleted = '0' AND b.status = 'active' AND p.status='normal' \
                      AND p.deleted='0' AND u.deleted = '0' \
                GROUP BY u.realname \
                ORDER BY num DESC"
    users.execute(users_sql)

    report_text = '# 禅道 bug 统计 \n------\n'
    i = 0
    for u in users:
        i = i + 1
        realname = u[0]
        account = u[1]
        mobile = u[2]
        count = u[3]

        report_text = report_text + '%s. %s: %s \n' % (i, realname, count)

        bug_sql = "SELECT b.title, b.assignedTo FROM zt_bug b LEFT JOIN zt_product p ON b.product = p.id \
                   WHERE b.deleted = '0' \
                   AND b.`status` = 'active'  \
                   AND p.`status` = 'normal' \
                   AND p.deleted = '0' \
                   AND b.assignedTo = '%s'" % account
        bugs.execute(bug_sql)

        bug_text = '# %s %s 个 bug 未解决 \n------\n' % (realname, count)
        for b in bugs:
            bug_text = bug_text + '- %s \n' % b[0]

        dingding(mobile, bug_text)
        time.sleep(3)

    dingding('18682077880', report_text)
    users.close()
    bugs.close()
    cnx.close()


@shared_task
def check_schedule():
    logger.info('定时器运行中 ...')


@shared_task
def clear_token():
    logger.info('从数据库中删除过期 token')
    call_command('cleartokens')
