#dantri.com.vn
#thanhnien.vn
import re
import urllib.request
dantri_item = ['su-kien','xa-hoi','the-gioi','the-thao','lao-dong-an-sinh','suc-khoe','tam-long-nhan-ai','kinh-doanh', 'bat-dong-san', 'o-to-xe-may', 'suc-manh-so', 'giao-duc-huong-nghiep', 'van-hoa', 'giai-tri', ]

thanhnien_item = ['thoi-su', 'the-gioi', 'tai-chinh-kinh-doanh', 'doi-song', 'van-hoa', 'giai-tri', 'gioi-tre', 'giao-duc', 'the-thao', 'suc-khoe']
with open("/content/drive/My Drive/Colab Notebooks/thanhnien.txt", "w+",encoding="utf-8") as f:
    Post = set()
    for ar in thanhnien_item:
        for i in range(1,31):
            url = 'https://thanhnien.vn/'+ str(ar)+'/trang-'+ str(i) + '.html'
            #print(url)
            html_res = urllib.request.urlopen(url).read().decode("utf-8")
            #print(html_res)
            url_pattern = r'([\w\.\/\-\?\:\#]*?)'      
            title_pattern = r"([\w\s\d\,\/\:\.]*?)"
            thanhnien_link = re.findall('href="' + url_pattern + '" title="' + title_pattern + '" class="story__title"' , html_res, re.DOTALL)
            '''dantri_link = re.findall('class="news-item__sapo" title="' + title_pattern + '"' + \
                                 ' href="' + url_pattern + '">', html_res, re.DOTALL)'''
            Post.update(thanhnien_link)
        for p in Post:
          try:
            html = urllib.request.urlopen('https://thanhnien.vn' + p[0]).read().decode("utf-8")
            f.write("-----------------------------------"+"\n")
            f.write("Tiêu đề: "+ p[1] + "\n" + "Link: https://thanhnien.vn"+ p[0] + "\n")
            date_pattern = r'([\w\s\d\,\/\:\.\(\)\+\-]*?)'
            #date_post = re.findall('<span class="dt-news__time">' + date_pattern + '</span>', html_1, re.DOTALL) # dantri
            date_post = re.findall('<time>' + date_pattern + '</time>', html, re.DOTALL) #thanhnien
            if len(date_post) == 1:
              f.write("Ngày: "+ str(date_post) + "\n")
          except:
            pass
    f.close()