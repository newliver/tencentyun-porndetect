#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import hmac
import hashlib
import binascii
import base64

import requests


class TencentYunPornDetect(object):

    def __init__(self, appid, secret_id, secret_key, bucket):
        """
        APP_ID和BUCKET，在http://console.qcloud.com/image/bucket查看.
        SECRET_ID和SECRET_KEY，在https://console.qcloud.com/image/project查看.
        """

        self.api_url = 'http://service.image.myqcloud.com/detection/pornDetect'
        self.appid = appid
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.bucket = bucket

    def get_porn_detect_sign_v2(self, image_url, current_time, expired):
        """
        签名算法文档：http://www.qcloud.com/wiki/万象优图黄图鉴别文档#2_.E9.89.B4.E9.BB.84CGI
        """

        plain_text_temp = 'a={appid}&b={bucket}&k={secret_id}&t={curren_time}&e={expired_time}&l={image_url}'
        plain_text = plain_text_temp.format(appid=self.appid,
                                            bucket=self.bucket,
                                            secret_id=self.secret_id,
                                            curren_time=current_time,
                                            expired_time=expired,
                                            image_url=image_url)
        bin = hmac.new(self.secret_key, plain_text, hashlib.sha1)
        s = bin.hexdigest()
        s = binascii.unhexlify(s)
        s = s + plain_text.encode('ascii')
        signature = base64.b64encode(s).rstrip()  # 生成签名
        return signature

    def dumps_http_body(self, url):
        return json.dumps({'appid': self.appid, 'bucket': self.bucket, 'url': url})

    def porn_detect(self, url, expired=10):
        """
        正确返回结果说明：
        result int    供参考的识别结果，0正常，1黄图
        confidence    double  识别为黄图的置信度，范围0-100；是normal_score, hot_score, porn_score的总和评分
        normal_score  double  图片为正常图片的评分
        hot_score     double  图片为性感图片的评分
        porn_score    double  图片为色情图片的评分

        例如：
            {
                'message': 'success',
                'code': 0,
                'data': {
                    'confidence': 14.737,
                    'hot_score': 100.0,
                    'porn_score': 0.0,
                    'result': 0,
                    'normal_score': 0.0
                }
            }


        错误返回说明：http://www.qcloud.com/wiki/万象优图黄图鉴别文档#2.3_.E9.94.99.E8.AF.AF.E7.A0.81
        错误码  含义
        1       错误的请求
        2       签名为空
        3       签名串错误
        4       appid/bucket/url不匹配
        5       签名编码失败（内部错误）
        6       签名解码失败（内部错误）
        7       签名过期
        8       appid不存在
        9       secretid不存在
        10      appid不匹配
        11      重放攻击
        12      签名失败
        13      错误的检测类型
        14      CGI错误
        15      请求包body错误
        16      请求处理失败（内部错误）
        17      处理过程中出现错误（内部错误）
        18      处理错误
        """

        now = int(time.time())
        expired = now + expired
        sign = self.get_porn_detect_sign_v2(url, now, expired)

        headers = {'Host': 'service.image.myqcloud.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Authorization': sign
                   }
        body = self.dumps_http_body(url)
        r = requests.post(self.api_url, data=body, headers=headers)
        return r.json()


def test():
    # APPID，在http://console.qcloud.com/image/bucket查看
    TENCENTYUN_APPID = ''
    TENCENTYUN_SECRET_ID = ''
    TENCENTYUN_SECRET_KEY = ''

    TENCENTYUN_BUCKET = ''

    url = 'http://img.xiuren.com/upload/image/201511/13/11/1447386277619799.jpg'
    prondetect = TencentYunPornDetect(TENCENTYUN_APPID,
                                      TENCENTYUN_SECRET_ID,
                                      TENCENTYUN_SECRET_KEY,
                                      TENCENTYUN_BUCKET)
    print prondetect.porn_detect(url)


if __name__ == '__main__':
    test()
