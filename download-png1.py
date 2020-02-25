import urllib.request
url = "https://api.aoikujira.com/ip/ini"
url2 = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 텍스트 출력
mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))

# 이미지 다운로드
#urlib.request.urlretrieve(url, savename)

mem2 = urllib.request.urlopen(url).read()
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다!")
