from tkinter import *
import requests
import time,re,requests,os,zipfile
LOG_LINE_NUM = 0
class MY_GUI_SET():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title(" 抖音无水印下载软件")
        self.init_window_name.geometry("730x150+10+10")
        self.init_window_name.attributes("-alpha", 1)  # 虚化 值越小虚化程度越高
        # 标签
        self.init_data_label = Label(self.init_window_name, text="链接")
        self.init_data_label.grid(row=0, column=0)
        self.name_data_label = Label(self.init_window_name, text="视频名称")
        self.name_data_label.grid(row=0, column=12)

    # 文本框
        self.init_data_Text = Text(self.init_window_name, width=45, height=9)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)

        self.name_data_Text = Text(self.init_window_name, width=45, height=9)  # 处name果展示
        self.name_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始下载", bg="lightblue", width=10,
                                              command=self.Get_music_url)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
    def Get_music_url(self):
            a=self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
            b = self.name_data_Text.get(1.0, END).strip().replace("\n", "").encode()
            Web_url=str(a,encoding="utf-8")
            name=str(b,encoding="utf-8")
            # 设置浏览器代理，一定要是移动设备，安卓/iOS均可
            headers = {
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
            }
            input_url = Web_url
            # 根据粘贴的分享内容，提取视频短链接
            preurl = re.findall(r'douyin.com\/(.*?)\/', input_url, re.I | re.M)
            print(preurl)
            # print("https://v.douyin.com/"+preurl[0])
            # 组装短链接url
            url = "https://v.douyin.com/" + preurl[0]

            # 请求短链接，获得itemId和dytk
            get = requests.get(url, headers=headers)
            html = get.content
            # print(html)
            itemId = re.findall(r"(?<=itemId:\s\")\d+", str(html))
            # print(itemId[0])
            dytk = re.findall(r"(?<=dytk:\s\")(.*?)(?=\")", str(html))
            # print(dytk[0])

            # 组装视频长链接
            videourl = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + itemId[0] + "&dytk=" + dytk[0]
            # print(videourl)

            # 请求长链接，获取play_addr
            videoopen = requests.get(videourl, headers=headers)
            vhtml = videoopen.text
            # print(vhtml)
            uri = re.findall(r'(?<=\"uri\":\")\w{32}(?=\")', str(vhtml))
            # print(uri[0])

            # 长链接的格式其实是固定的，唯一变动的就是video_id，上面提取出uri后进行组装即可得到最终链接
            play_addr = "https://aweme.snssdk.com/aweme/v1/play/?video_id=" + uri[0] + "&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH"
            print("===>复制下面的长链接到手机浏览器打开即可得到无水印视频\n===>" + play_addr)

            # 自定义文件名保存短视频

            video = requests.get(url=play_addr, headers=headers)
            with open(name + ".mp4", 'wb')as file:
                file.write(video.content)
                file.close()
                print("===>视频下载完成！")


if __name__=="__main__":
    init_window = Tk()
    MY_GUI_SET(init_window).set_init_window()
    init_window.mainloop()
