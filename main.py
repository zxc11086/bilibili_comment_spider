import requests
import json
import search


headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

#视频id
# oid = 'BV1794y1B7n1'
#评论页数
# pn = 1
#排序种类 0是按时间排序 2是按热度排序
sort = 2

comment = []
key = input("请输入话题")
ids = search.search(key)
for id in ids:
    pn = 1
    while True:
        url =f'https://api.bilibili.com/x/v2/reply?pn={pn}&type=1&oid={id}&sort={sort}'
        reponse = requests.get(url,headers=headers)
        a = json.loads(reponse.text)
        if pn==1:
            try:
                count = a['data']['page']['count']
                size = a['data']['page']['size']
                page = count//size+1
                print(page)
            except:
                break
        try:
            for b in a['data']['replies']:
                comment.append(b["content"]["message"])
        except:
            break
        if pn!=page:
            pn += 1
        else:
            break

    with open(key+".txt", "w", encoding="utf-8") as fp:
        for c in comment:
            fp.write(c + "\n")
