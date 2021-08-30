import requests
import json
import time

prev_dist=0
curr_dist=0

jsondata = {
  "gps_info": [37.59125708084185 , 127.02036963828073]
  # 실제 gps 값을 여기에 넣으면 된다.
  # gps 값은 계속 갱신되어야 함
}

def update_gps(jsondata):
    #jsondata['gps_info'][1] -= 0.000004
    jsondata['gps_info'][0] -= 0.000004
    # 이 부분은 더미gps데이터가 움직이는것을 표현하기 위해서 만들어짐

def api_call(jsondata):
  while(1):
    update_gps(jsondata)

    #print(jsondata)
    requestData = requests.post('https://z13hnwl436.execute-api.us-east-1.amazonaws.com/firefly/apis' , data =  json.dumps(jsondata))
    #print(requestData.json())

    print(" 보이스 : ",int(requestData.json()['dist']))

    time.sleep(0.1)
    # 시간텀을 바꾸거나 남은 거리 값을 계산해서 ?미터마다 알림을 하게 만들어도 된다
    
    '''

    '''

    if(requestData.json()['time'] < 1):
        break
    # 시간이 얼마 안남으면 루프 빠져나옴

    # 여기 부분에 횡단보도 끝부분 인식시 loop 빠져나오는 코드
    

prev_dist=0
curr_dist=0

print("blue? answer 'blue' or 'red'")
a = input()
if a == 'blue':
  api_call(jsondata)


