import requests

def get_proxy():
    try:
        # 这里填写大象代理api地址，num参数必须为1，每次只请求一个IP地址
        token=get_token()
        url = 'https://api.getproxylist.com/proxy?country[]=US&lastTested=600&maxConnectTime=1&apiKey='+token
        response = requests.get(url)
        response.close()
        protocol=str(response.json()['protocol'])
        ip = response.json()['ip']
        port=str(response.json()['port'])
        result=protocol+'://'+ip+':'+port
        print(result)
        return result
    except:
        print('no ip available')
        return ''
    finally:
        pass