from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch-ad', methods=['GET'])
def fetch_ad():
    url = "https://api.ad.snaptube.app/v1/deliver/staticAd"
    
    params = {
        'ad_type': "1",
        'directDownload': "true",
        'latitude': "13.585546299999999",
        'imsi': "42101",
        'ad_pos': "download_popup",
        'reqid': "78853576-4b86-4732-b3af-f557503103b3",
        'local_time': "16:42",
        'recentIAds': "com.dywx.larkplayer,com.dywx.larkplayer,com.dywx.larkplayer",
        'local_timezone': "3",
        'model': "SM-G610F",
        'keyword': "[\"اغنيه sheesh بيبي مونستر\",\"اغنيه Iam آيف\",\"اغنيه wife جي ايدل\"]",
        'avr': "8.1.0",
        'networkType': "WIFI",
        'brand': "samsung",
        'longitude': "44.0060114",
        'ad_h': "50",
        'offset': "0",
        'count': "1",
        'ppi': "480",
        'advertisingID': "1856807d-8241-4306-8d9f-63380da88e79",
        'passThrough': "{\"request_type\":\"real_time\",\"ad_type_exp_direct_times\":3,\"ad_request_direct_times\":7,\"client_request_time\":1721569342245,\"ad_type_request_direct_times\":7,\"ad_exp_direct_times\":3,\"ad_pos_exp_direct_times\":0,\"ad_sub_provider\":\"MoAdx\",\"is_first_day\":false,\"waterfall_config_id\":\"332_1721568908\",\"layer_index\":2,\"is_config_pre_request\":true,\"server_waterfall_config\":\"<snaptube#download_popup_adx><snaptube#download_popup_dt><huawei#download_popup_native_opt><pangle#download_popup><vungle#download_popup_mrec>\",\"ad_pos_request_direct_times\":1}",
        'ad_w': "320",
        'imei': "",
        'location': "Yemen|Ta'izz Governorate|Al Mudhaffar|Taizz|",
        'placement': "download_popup_dt",
        'cache_flag': "all",
        'androidID': "47efe134a4ba6434",
        'ratio': "320*180",
        'ad_preview_mode': "false",
        'networkCountryIso': "YE",
        'test_ids': "null",
        'os': "27",
        'ch': "tube_huawei_as",
        'f': "phoenix2",
        'locale': "ar",
        'vc': "6184010",
        'u': "6f35533055d0a87c0dc505ef3d9ce54a",
        'v': "6.18.0.6184010",
        'random_id': "40",
        'net': "WIFI",
        'lang': "ar",
        'region': "YE",
        'pn': "com.snaptube.premium"
    }
    
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.143 Mobile Safari/537.36",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'x-requested-with-version': "6.18.0.6184010.6184010",
        'Cookie': ""
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
