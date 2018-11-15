from urllib.request import urlopen as uReq  
# extract the urlopen function,取名为uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://book.douban.com/latest?icn=index-latestbook-all'

# opening the url and download the infor from the website in the uClient
# read() 读取信息
# close() 关闭文件

uClient =  uReq(my_url)
page_html = uClient.read()
uClient.close()

# Right now the html convert to a container of text

# page html parsing
page_soup = soup(page_html,"html.parser")

page_soup.h1 #返回页面标题：新书速递

# The goal: try to convert every item of the page into a csv file

# The next step: inspect the elements of the page

#grabs each book
# 关于书的源代码，找到其中一本书的链接，单击右键，找到inspect寻找源代码
book = page_soup.findAll("div",{"class":"detail-frame"})

len(book) # there are total 40 books(items)

# The next step is to find out the web code structure of one book

#book[0] 
# the information of the first book
# 网页解析码在另外一个文件里面
#一般而言，book[0]是在loop里面做首个遍历example的

#book_1 = book[0]
#book_1.h2 
# 获取一个link
#<a href="https://book.douban.com/subject/30338769/">梦的化石</a>
# 书籍名称是 属于text的部分，所以用一个function text()
# book_1.h2.text 
# return '\n梦的化石\n'
# 去掉换行符号'\n'的方法：strip('\n')
# book_1.h2.text.strip('\n')

#经过了以上的实验，可以开始写loop

#对于作者姓名，出版社，以及出版时间的爬取
#通过对于源代码的分析，我们可以发现这些信息是在同一<p下的某一个类型下面>
#因此这里的想法就是用 解析soup的function： findAll()
# book_1.findAll("p",{"class":"color-gray"})
# return: [<p class="color-gray">  [日]今敏 / 北京联合出版公司 / 2018-11-1 </p>]
# 这是在一个list [ ]里面，若单纯获得里面的信息，则需要:author_1 = book_1.findAll("p",{"class":"color-gray"})[0]

# author_1.text
# return: '\n                        [日]今敏 / 北京联合出版公司 / 2018-11-1\n   

# author_1.text.strip('\n')
# author_1.text.strip('\n').split('/')[0] 返还作者名：'                        [日]今敏 '

# Create a csv file
filename = "新书速递.csv"
f = open(filename,"w")

headers = "bookname,authorname,publish,time\n" # should have a new line

f.write(headers) # write first line

#Loop

for book_1 in book:
    bookname = book_1.h2.text.strip('\n')

    authorname = book_1.findAll("p",{"class":"color-gray"})[0].text.strip('\n').split('/')[0]

    publish = book_1.findAll("p",{"class":"color-gray"})[0].text.strip('\n').split('/')[1]

    time = book_1.findAll("p",{"class":"color-gray"})[0].text.strip('\n').split('/')[2]

    print("bookname: " + bookname)
    print("authorname: " + authorname)
    print("publish: " + publish)
    print("time: " + time)

    f.write(bookname    +   "," +   authorname  +   "," +   publish +   "," +   time    +   "\n")

f.close() #remove space
 



