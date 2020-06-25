import requests,time,os
import simplejson
def Check_in(emaill, passwd):

    url = 'https://v2.ssaa.best/'
    login_url = 'https://v2.ssaa.best/auth/login'
    
    # 构建请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # 登录地址
    # 忽视verify = False的错误提示
    requests.packages.urllib3.disable_warnings()
    # 使用Session，利用session发送get请求获得cookie
    session = requests.Session()
    banornot = session.get(url,headers=headers,allow_redirects=False)
    if banornot.status_code == 200:
        html = session.get(login_url, verify=False, headers=headers).text 
        data = {
            "email": emaill,
            "passwd": passwd,
            "code": ""
        }
        requests.packages.urllib3.disable_warnings()
        #登录到该网页
        req = session.post(login_url, data=data, verify=False, headers=headers)
        print("用户 " + emaill + "登陆成功")
        # 签到地址
        check_in = 'https://v2.ssaa.best/user/checkin'
        req = session.post(check_in, headers=headers)
        #print(req.url,'\n',req.status_code)
        #print(simplejson.loads(req.text)['msg'])
        
        # 查询详细信息
        #try:
            #tryy = simplejson.loads(req.text)["traffic"]
            #print(simplejson.loads(req.text)['msg'])
            #print('总流量：' + simplejson.loads(req.text)["traffic"])
            #print('今日已用流量：' + simplejson.loads(req.text)["trafficInfo"]["todayUsedTraffic"])
            #print('过去已用流量：' + simplejson.loads(req.text)["trafficInfo"]["lastUsedTraffic"])
            #print('账户剩余流量：' + simplejson.loads(req.text)["trafficInfo"]["unUsedTraffic"])
        #except:
            #print(simplejson.loads(req.text)['msg'])
    else:
        print('当前无法签到',banornot.status_code)

if __name__=='__main__':
    email = os.environ["EMAIL"]
    passwd = os.environ["PWD"]
    users = [{
        "email": email,
        "passwd": passwd
    }]
    for user in users:
        print(user['email'], user['passwd'])
        Check_in(user['email'], user['passwd'])
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

