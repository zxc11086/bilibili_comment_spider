import requests  # 发送请求
import re  # 数据清洗

# 请求头
headers = {
    'cookie': "buvid3=5D0779F8-99A2-C9F3-C573-8A7DD7E777F122201infoc; b_nut=1701850722; i-wanna-go-back=-1; b_ut=7; _uuid=4FE110F77-D131-A258-7459-EF5A10392C10AD22314infoc; enable_web_push=DISABLE; buvid4=C35F96B5-3F80-F945-66AA-DD2D150792FA22720-023120608-; header_theme_version=CLOSE; CURRENT_FNVAL=4048; rpdid=|(k|))Yl~|mJ0J'u~|JJJ)lm|; DedeUserID=457802961; DedeUserID__ckMd5=77b220d69524a5e7; home_feed_column=5; hit-dyn-v2=1; buvid_fp_plain=undefined; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW2; LIVE_BUVID=AUTO5417093004472843; CURRENT_QUALITY=80; PVID=1; fingerprint=cf16344ea1ec02b2436d9b67037f26f3; buvid_fp=cf16344ea1ec02b2436d9b67037f26f3; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEzMzk5NjMsImlhdCI6MTcxMTA4MDcwMywicGx0IjotMX0.J2sgmm2MkVixCh-zOJZFxAtQ2Z74W7aj2oRMTHzw2iM; bili_ticket_expires=1711339903; SESSDATA=d3e4e9e2%2C1726719037%2Ca5047%2A32CjDMSpKmO2oXaQgoWuI2V58BqRbS2xI00zCt6GbUSukJtiCWs3sSzs9737g4KxFhyPYSVjcycU1QQWgydlhJTFE5TU16SFdocnVIbzE1ZGtkeU8yM1dDTG1VZDMxWGw4M0Z0bmJ6OEJWUkl4dDhJczl1dXRQT0Mta2VRTWtwNXJPUDRXSzBWZDdRIIEC; bili_jct=caff2decf5042d7c5fb5c76459200464; bp_video_offset_457802961=911941863287554081; browser_resolution=2274-1294; bsource=search_google; b_lsid=B645EC6E_18E6F2A627D; sid=7h94vf7r",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

def search(key):
    v_keyword = key
    url = 'https://search.bilibili.com/all?keyword={}&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=24'.format(v_keyword)

    # 获取搜索的视频id
    r = requests.get(url, headers=headers)
    data = r.text
    a = re.findall('BV\w*',data)
    a = list(set(a))
    return a 

# with open("info.txt", "w", encoding="utf-8") as fp:
#     fp.write(data)