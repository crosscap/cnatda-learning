# question_answers

## 1

![info](images/info.png)
![clinet_http_info](images/clinet_http_info.png)
![server_http_info](images/server_http_info.png)

### q1

本机使用 HTTP/1.1 协议，服务器使用 HTTP/1.1 协议。

### q2

zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2

中文 英文 日文

### q3

本机 IP 地址：192.168.31.156
服务器 IP 地址：128.119.245.12

### q4

540

### q5

last_modified: Fri, 13 Sep 2024 05:59:01 GMT

### q6

Content-Length: 128\r\n

### q7

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0\r\n
Accept-Encoding: gzip, deflate\r\n

出于某些不可抗力, 此后使用作者提供的 pcapng

## 2

![modfied_info](images/modfied_info.png)
![modfied_GET_1](images/modfied_GET_1.png)
![modfied_receive_1](images/modfied_receive_1.png)
![modfied_GET_2](images/modfied_GET_2.png)
![modfied_receive_2](images/modfied_receive_2.png)

### q8

没有 IF-MODIFIED-SINCE

### q9

显式返回了文件的内容

返回的状态码是 200 OK, 并且返回的长度较长

### q10

有 IF-MODIFIED-SINCE

If-Modified-Since: Wed, 03 Feb 2021 06:59:02 GMT\r\n

### q11

304 Not Modified

没有返回文件内容, 状态码与 200 OK 不同, 并且返回的长度较短

## 3

![long_text_info](images/long_text_info.png)

### q12

发送了 1 个 GET 请求

第 26 号数据包

### q13

第 32 号数据包

### q14

200 OK

### q15

总共 4 个 TCP 段, 这里是 28, 29, 31, 32

## 4

![insert_info](images/insert_info.png)

### q16

4 个

两个 128.119.245.12, 一个 178.19.137.164, 一个  178.79.137.164 (重定向)

### q17

连续下载, 在第一个图片的回复到达后第二个图片的请求才被发送

## 5

![auth_info](images/auth_info.png)

### q18

401 Unauthorized

### q19

Cache-Control: max-age=0\r\n
Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n
