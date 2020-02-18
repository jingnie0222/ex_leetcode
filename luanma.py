import requests
from urllib.parse import quote
import urlhandle

url = "https://wap.sogou.com/web/searchList.jsp?keyword=" + quote("西藏的别名")

query = ""
queryFrom = "wap"

params = {'query': query,
          'queryFrom': queryFrom}

params_utf16 = urlhandle.urlencode(params, 'utf-16le', 'ignore')
headers = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}

data = "queryType=%71%00%75%00%65%00%72%00%79%00&parity=%32%00%32%00%66%00%63%00%31%00%63%00%35%00%32%00%2d%00%63%00%37%00%65%00%37%00%2d%00%34%00%35%00%34%00%66%00%2d%00%39%00%63%00%37%00%64%00%2d%00%39%00%66%00%64%00%63%00%39%00%39%00%30%00%32%00%37%00%64%00%33%00%39%00&dump=%30%00&forceQuery=%31%00&rankType=%30%00&fromTime=%30%00&debug=%30%00&timeRankOnly=%30%00&urlFilterLevelGovernment=%30%00&logLevel=%30%00&urlFilterEndTime=%30%00&keepFiltered=%32%00&maxNumPerSite=%32%00&end=%31%00%30%00&urlFilterStartTime=%30%00&userArea=%17%53%ac%4e%02%5e&fileType=%30%00&userIP=%31%00%30%00%2e%00%31%00%32%00%39%00%2e%00%31%00%35%00%32%00%2e%00%37%00%33%00&hash=%37%00%62%00%31%00%34%00%31%00%64%00%31%00%66%00%34%00%62%00%30%00%61%00%38%00%33%00%32%00%66%00%64%00%62%00%39%00%66%00%61%00%62%00%32%00%33%00%38%00%66%00%66%00%30%00%64%00%64%00%37%00%30%00&queryFrom=%77%00%61%00%70%00&qoxml=%3c%00%44%00%4f%00%43%00%55%00%4d%00%45%00%4e%00%54%00%3e%00%3c%00%69%00%64%00%3e%00%37%00%62%00%31%00%34%00%31%00%64%00%31%00%66%00%34%00%62%00%30%00%61%00%38%00%33%00%32%00%66%00%64%00%62%00%39%00%66%00%61%00%62%00%32%00%33%00%38%00%66%00%66%00%30%00%64%00%64%00%37%00%30%00%56%00%4d%00%3c%00%2f%00%69%00%64%00%3e%00%3c%00%73%00%71%00%6c%00%3e%00%3c%00%21%00%5b%00%43%00%44%00%41%00%54%00%41%00%5b%00%53%00%45%00%4c%00%45%00%43%00%54%00%20%00%22%00%49%00%4e%00%46%00%4f%00%42%00%4f%00%58%00%5f%00%7e%76%a6%5e%5f%00%2b%52%f0%79%22%00%20%00%57%00%48%00%45%00%52%00%45%00%20%00%4e%00%41%00%4d%00%45%00%20%00%3d%00%20%00%22%00%7f%89%cf%85%22%00%20%00%41%00%4e%00%44%00%20%00%49%00%4e%00%4e%00%45%00%52%00%49%00%44%00%20%00%3d%00%20%00%22%00%31%00%31%00%31%00%31%00%31%00%31%00%30%00%34%00%33%00%36%00%22%00%5d%00%5d%00%3e%00%3c%00%2f%00%73%00%71%00%6c%00%3e%00%3c%00%65%00%6e%00%74%00%69%00%74%00%79%00%69%00%64%00%3e%00%31%00%31%00%31%00%31%00%31%00%31%00%30%00%34%00%33%00%36%00%3c%00%2f%00%65%00%6e%00%74%00%69%00%74%00%79%00%69%00%64%00%3e%00%3c%00%70%00%72%00%6f%00%70%00%3e%00%49%00%4e%00%46%00%4f%00%42%00%4f%00%58%00%5f%00%7e%76%a6%5e%5f%00%2b%52%f0%79%3c%00%2f%00%70%00%72%00%6f%00%70%00%3e%00%3c%00%71%00%63%00%3e%00%3c%00%2f%00%71%00%63%00%3e%00%3c%00%71%00%63%00%6c%00%3e%00%2d%00%37%00%3c%00%2f%00%71%00%63%00%6c%00%3e%00%3c%00%2f%00%44%00%4f%00%43%00%55%00%4d%00%45%00%4e%00%54%00%3e%00&trafficSign=&forbidRequery=%30%00&toTime=%30%00&queryString=%7f%89%cf%85%84%76%2b%52%f0%79&interOnly=%30%00&sql=%53%00%45%00%4c%00%45%00%43%00%54%00%20%00%22%00%49%00%4e%00%46%00%4f%00%42%00%4f%00%58%00%5f%00%7e%76%a6%5e%5f%00%2b%52%f0%79%22%00%20%00%57%00%48%00%45%00%52%00%45%00%20%00%4e%00%41%00%4d%00%45%00%20%00%3d%00%20%00%22%00%7f%89%cf%85%22%00%20%00%41%00%4e%00%44%00%20%00%49%00%4e%00%4e%00%45%00%52%00%49%00%44%00%20%00%3d%00%20%00%22%00%31%00%31%00%31%00%31%00%31%00%31%00%30%00%34%00%33%00%36%00%22%00&start=%30%00&userGroup=%30%00&urlFilterLevel=%31%00%32%00%37%00&summaryFilter=%31%00&clusterFilter=%31%00"
#data1 = "queryType=%71%00%75%00%65%00%72%00%79%00&parity=%34%00%36%00%39%00%32%00%38%00%39%00%65%00%35%00%2d%00%66%00%34%00%34%00%35%00%2d%00%34%00%33%00%61%00%33%00%2d%00%38%00%64%00%33%00%64%00%2d%00%37%00%37%00%36%00%34%00%34%00%34%00%39%00%39%00%39%00%66%00%65%00%62%00&dump=%30%00&query=%18%52%b7%5f%4e%53%84%76%01%80%46%5a&tag=%18%52%b7%5f%4e%53%3c%00%50%00%45%00%52%00%53%00%4f%00%4e%00%3e%00%01%80%46%5a%3c%00%50%00%5f%00%41%00%5f%00%50%00%45%00%52%00%53%00%4f%00%4e%00%5f%00%34%00%3e%00&forceQuery=%30%00&rankType=%30%00&fromTime=%30%00&debug=%30%00&timeRankOnly=%30%00&urlFilterLevelGovernment=%30%00&logLevel=%30%00&urlFilterEndTime=%30%00&keepFiltered=%32%00&maxNumPerSite=%32%00&end=%31%00%30%00&urlFilterStartTime=%30%00&userArea=%17%53%ac%4e%02%5e&fileType=%30%00&userIP=%31%00%30%00%2e%00%31%00%32%00%39%00%2e%00%31%00%35%00%32%00%2e%00%37%00%33%00&hash=%33%00%32%00%64%00%35%00%33%00%38%00%31%00%63%00%34%00%63%00%31%00%34%00%64%00%30%00%31%00%39%00%66%00%31%00%61%00%64%00%63%00%61%00%34%00%32%00%33%00%36%00%66%00%38%00%35%00%31%00%37%00%62%00&queryFrom=%77%00%61%00%70%00&qoxml=%3c%00%44%00%4f%00%43%00%55%00%4d%00%45%00%4e%00%54%00%3e%00%3c%00%69%00%64%00%3e%00%33%00%32%00%64%00%35%00%33%00%38%00%31%00%63%00%34%00%63%00%31%00%34%00%64%00%30%00%31%00%39%00%66%00%31%00%61%00%64%00%63%00%61%00%34%00%32%00%33%00%36%00%66%00%38%00%35%00%31%00%37%00%62%00%56%00%4d%00%3c%00%2f%00%69%00%64%00%3e%00%3c%00%73%00%71%00%6c%00%3e%00%3c%00%21%00%5b%00%43%00%44%00%41%00%54%00%41%00%5b%00%53%00%45%00%4c%00%45%00%43%00%54%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%ba%4e%22%00%20%00%57%00%48%00%45%00%52%00%45%00%20%00%4e%00%41%00%4d%00%45%00%20%00%3d%00%20%00%22%00%18%52%b7%5f%4e%53%22%00%20%00%41%00%4e%00%44%00%20%00%22%00%54%00%59%00%50%00%45%00%22%00%20%00%3d%00%20%00%22%00%ba%4e%22%00%20%00%41%00%4e%00%44%00%20%00%28%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%73%51%fb%7c%0d%54%f0%79%22%00%20%00%4c%00%49%00%4b%00%45%00%20%00%22%00%4d%91%76%50%22%00%20%00%4f%00%52%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%73%51%fb%7c%0d%54%f0%79%22%00%20%00%3d%00%20%00%22%00%bb%59%50%5b%22%00%20%00%29%00%5d%00%5d%00%3e%00%3c%00%2f%00%73%00%71%00%6c%00%3e%00%3c%00%74%00%61%00%67%00%3e%00%3c%00%21%00%5b%00%43%00%44%00%41%00%54%00%41%00%5b%00%18%52%b7%5f%4e%53%3c%00%50%00%45%00%52%00%53%00%4f%00%4e%00%3e%00%01%80%46%5a%3c%00%50%00%5f%00%41%00%5f%00%50%00%45%00%52%00%53%00%4f%00%4e%00%5f%00%34%00%3e%00%5d%00%5d%00%3e%00%3c%00%2f%00%74%00%61%00%67%00%3e%00%3c%00%71%00%75%00%65%00%72%00%79%00%3e%00%3c%00%21%00%5b%00%43%00%44%00%41%00%54%00%41%00%5b%00%18%52%b7%5f%4e%53%84%76%01%80%46%5a%5d%00%5d%00%3e%00%3c%00%2f%00%71%00%75%00%65%00%72%00%79%00%3e%00%3c%00%6c%00%61%00%73%00%74%00%74%00%61%00%67%00%3e%00%3c%00%21%00%5b%00%43%00%44%00%41%00%54%00%41%00%5b%00%3c%00%50%00%45%00%52%00%53%00%4f%00%4e%00%3e%00%3a%00%3c%00%50%00%5f%00%41%00%5f%00%50%00%45%00%52%00%53%00%4f%00%4e%00%5f%00%34%00%3e%00%5d%00%5d%00%3e%00%3c%00%2f%00%6c%00%61%00%73%00%74%00%74%00%61%00%67%00%3e%00%3c%00%65%00%6e%00%74%00%69%00%74%00%79%00%69%00%64%00%3e%00%3c%00%2f%00%65%00%6e%00%74%00%69%00%74%00%79%00%69%00%64%00%3e%00%3c%00%70%00%72%00%6f%00%70%00%3e%00%3c%00%2f%00%70%00%72%00%6f%00%70%00%3e%00%3c%00%71%00%63%00%3e%00%3c%00%2f%00%71%00%63%00%3e%00%3c%00%71%00%63%00%6c%00%3e%00%2d%00%37%00%3c%00%2f%00%71%00%63%00%6c%00%3e%00%3c%00%2f%00%44%00%4f%00%43%00%55%00%4d%00%45%00%4e%00%54%00%3e%00&trafficSign=&forbidRequery=%30%00&toTime=%30%00&lasttag=%3c%00%50%00%45%00%52%00%53%00%4f%00%4e%00%3e%00%3a%00%3c%00%50%00%5f%00%41%00%5f%00%50%00%45%00%52%00%53%00%4f%00%4e%00%5f%00%34%00%3e%00&queryString=%18%52%b7%5f%4e%53%84%76%01%80%46%5a&interOnly=%30%00&sql=%53%00%45%00%4c%00%45%00%43%00%54%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%ba%4e%22%00%20%00%57%00%48%00%45%00%52%00%45%00%20%00%4e%00%41%00%4d%00%45%00%20%00%3d%00%20%00%22%00%18%52%b7%5f%4e%53%22%00%20%00%41%00%4e%00%44%00%20%00%22%00%54%00%59%00%50%00%45%00%22%00%20%00%3d%00%20%00%22%00%ba%4e%22%00%20%00%41%00%4e%00%44%00%20%00%28%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%73%51%fb%7c%0d%54%f0%79%22%00%20%00%4c%00%49%00%4b%00%45%00%20%00%22%00%4d%91%76%50%22%00%20%00%4f%00%52%00%20%00%22%00%ba%4e%69%72%7b%7c%5f%00%ba%4e%5f%00%b2%4e%c6%5b%73%51%fb%7c%3a%00%ba%4e%69%72%7b%7c%5e%5c%27%60%5f%00%ba%4e%5e%5c%27%60%5f%00%b2%4e%c6%5b%73%51%fb%7c%5f%00%73%51%fb%7c%0d%54%f0%79%22%00%20%00%3d%00%20%00%22%00%bb%59%50%5b%22%00%20%00%29%00&start=%30%00&userGroup=%30%00&urlFilterLevel=%31%00%32%00%37%00&clusterFilter=%31%00&summaryFilter=%31%00"

res = requests.post('http://10.134.107.108:28001', data=data, headers=headers)
print(res.text.encode('utf8'))
if b'\u003f' in res.text.encode('utf8'):
    print(res.text.encode('utf8'))
    print("True")