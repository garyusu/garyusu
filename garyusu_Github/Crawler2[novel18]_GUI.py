import site
import requests  #用於get請求
from bs4 import BeautifulSoup as bs #網頁分析
from os import mkdir #建資料夾(目錄)
import tkinter as tk
from tkinter import messagebox

url = "https://novel18.syosetu.com" #主頁

#要改動項目1
cookie = '_ga=GA1.2.2119806991.1639036262; over18=yes; ks2=amh1ad1bqbr; sasieno=0; lineheight=0; fontsize=0; novellayout=0; fix_menu_bar=1; autologin=1997094<>2555dc56b585055f3875535e55b44d784259e15d045c43de68492b5bd716da67; nlist3=14rtk.5-14qmt.k-14r7p.0-pszu.5-dzol.d-rz2h.10; _pbjs_userid_consent_data=3524755945110770; cto_bidid=KTq1xl9XWW5ncXZLR25SRWR4OWd5RUpLUG02S0R5QXFQRmdNSCUyRiUyQk10UFJkNERGTjBEZEhrRWdwRWNuSllCWFNRUXVMWmFOOWtZYmVtU2lEbXFNNDh2ckthSXhBNGNpUHE1ZW9CRUFGR3VPRkg4UmslM0Q; cto_bundle=1DYnUV9OcTUyOTdVSEdmYUZGWXE4TFRwOVBFeWJReEdwbU96TlkxamdFU0ZxMDRpMWU2WGZ3eHhjSHBNcm1vbGx4ZkclMkZwaG5zYjhpazdHR3p3ZTdHUFBxN2VqUjFYRHNNU21KTmRFZ094NjNOM0w1Y05mJTJCZG5xM1dzdW15a0p0Ym1hR1c4QzgzeHNMOTJrQWRqdFd5dG5wUFV3JTNEJTNE; ses=94e2slt4j5tlaq2fnlg63srlbr'

headers={ #要改動項目2
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br', 
    'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'novel18.syosetu.com', #不用改
    'Cookie':cookie,
    'Upgrade-Insecure-Requests':'1',#不用改
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}  


# def get_novel(url):
#     novel_id = '/n1571cz/' #小說連結編號 #要改動項目3
#     url_novel = url + novel_id #小說目錄連結

#     req = requests.get(url_novel, headers = headers)
#     soup = bs(req.text, "html.parser")
#     # print(soup)
#     if req.status_code != 200:
#         print("連接失敗")
    
#     novel_list = soup.select('dl.novel_sublist2 > dd.subtitle > a') #章節連結
#     a = 1 #檔案開頭編號
#     novel_title = soup.select('p.novel_title') #小說標題
#     novel_writerName = soup.select('div.novel_writername > a') #作者名
#     dirName = novel_title[0].text #資料夾名
#     mkdir(dirName)#於工作區內建新資料夾
    
#     for nl in novel_list:
#         url_href = url + nl['href'] #章節連結
#         r2 = requests.get(url_href, headers = headers)
#         r2.encoding = r2.apparent_encoding #轉碼
#         soup2 = bs(r2.text , "html.parser").select('div#novel_honbun') #小說內文
#         a_str = nl.text + '[作者：' + novel_writerName[0].text + ']' + '.txt' #小說檔名

#         with open(dirName + '/' + a_str, 'a', encoding="utf-8") as txt:
#             txt.write(nl.text + '\n\n\n') #寫入開頭標題
#             for s in soup2:
#                 sr = s.text.replace('<br/>', '\n') #把小說內文的<br/>換掉
#                 txt.write(sr + '\n')
#         txt.close
#         a = a + 1

# get_novel(url)
# print("OVER!!")

intput_website ='' #輸入網址

def new_window():
    window = tk.Tk()
    window.title('新視窗')
    window.geometry('600x800')
    window.maxsize(1280,700)

    #元件類別(父類別, 選擇性參數1 = 值1, ...) ，建立元件
    #元件.grid(row=列數, column=行數) ，設定(相對)位置
    mylabel = tk.Label(window, text='請輸入網址：')
    mylabel.grid(row=0, column=0)

    intput_website = tk.StringVar() #輸入的字
    myEntry = tk.Entry(window, textvariable=intput_website, width=40) #文字輸入框
    myEntry.grid(row=0, column=1)

    #button觸發
    def button_event():
        if intput_website.get() == '':
            tk.messagebox.showerror('message', '未輸入答案') #showerror 提醒訊息

    myButton = tk.Button(window, text='計算', command= button_event)
    myButton.grid(row=1, column=0, rowspan=2)



    #inp1 = tk.Entry(window, text="Hello World", bg="yellow", fg="#263238", font=('Arial', 20))，進一步元件風格

    window.mainloop()

if __name__=='__main__':
    new_window()