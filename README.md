# 万象优图智能鉴黄Python SDK（非官方）

本程序基于腾讯云万象优图智能鉴黄服务

* 地址：(http://www.qcloud.com/event/pd)

## Install

	
	pip install tencentyun-porndetect

or

	# download package	
	python setup install	
	
## Example

	>>> from tencentyun_porndetect.porndetect import TencentYunPornDetect
	>>> appid = ''
	>>> secret_id = ''
	>>> secret_key = ''
	>>> bucket = ''
	>>> img_url = 'http://<public_url>'
	>>> pd = TencentYunPornDetect(appid, secret_id, secret_key, bucket)
	>>> # default expired: 10
	>>> pd.porn_detect(img_url, expired)
	>>> {u'message': u'success', u'code': 0, u'data': {u'confidence': 14.737, u'hot_score': 100.0, u'porn_score': 0.0, u'result': 0, u'normal_score': 0.0}}
	
## Response

### Ok
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

### error code

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
	
## License
MIT 

