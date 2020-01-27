import json
import time
from collections import defaultdict
from datetime import datetime

data_store={}
flag=True
def init_data():
    f= json.load(open('dingxiangyuan.json'))
    for i in f['data']['getAreaStat']:
        data_store[i['provinceName']] = defaultdict(str)
        data_store[i['provinceName']]['确诊']=i['confirmedCount']
        data_store[i['provinceName']]['疑似']=i['suspectedCount']
        data_store[i['provinceName']]['治愈']=i['curedCount']
        data_store[i['provinceName']]['死亡']=i['deadCount']
        for j in i['cities']:
            data_store[j['cityName']] = defaultdict(str)
            data_store[j['cityName']]['确诊']=j['confirmedCount']
            data_store[j['cityName']]['疑似']=j['suspectedCount']
            data_store[j['cityName']]['治愈']=j['curedCount']
            data_store[j['cityName']]['死亡']=j['deadCount']
    
    data_store['general']= f['data']['getStatisticsService']['countRemark']
    return data_store




def get_detail_info(address):
    ds = {}
    if len(ds) == 0:
        ds=init_data()
    a = int(time.time())    #当前时间
    c = datetime.fromtimestamp(a+43200).strftime('%H:%M')    #格式转换
    
    if c.split(':')[1][-1]=='0':
        ds = init_data()
    if address=='general':
        try:
            return "整体的情况是：确诊：{}, 疑似：{}, 治愈：{}, 死亡：{}。请不要紧张，一切都会好的".format(ds[address]['确诊'], ds[address]['疑似'], ds[address]['治愈'],ds[address]['死亡'])
        except:
            return "暂时没有你所查找的信息，请换一种说法说出你要查询的城市名称"

    try:
        return "{} 的情况是：确诊：{}, 疑似：{}, 治愈：{}, 死亡：{}。请不要紧张，一切都会好的".format(address, ds[address]['确诊'], ds[address]['疑似'], ds[address]['治愈'],ds[address]['死亡'])
    except:
        return "暂时没有你所查找的信息，请换一种说法说出你要查询的城市名称"

if __name__ == '__main__':
    
    d = get_detail_info('武汉')
    print(d)