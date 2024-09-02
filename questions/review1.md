# review1

## 1.1

### R1

本书中主机等同于端系统，计算机、联网家具、服务器都属于端系统。Web服务器也属于端系统。

### R2

下面粘贴自Wikipedia中外交协议的英文解释：

> In international politics, protocol is the etiquette of diplomacy and affairs of state. It may also refer to an international agreement that supplements or amends a treaty. A protocol is a rule which describes how an activity should be performed, especially in the field of diplomacy. In diplomatic services and governmental fields of endeavor protocols are often unwritten guidelines. Protocols specify the proper and generally accepted behavior in matters of state and diplomacy, such as showing appropriate respect to a head of state, ranking diplomats in chronological order of their accreditation at court, and so on.

### R3

协议规定了双方的行为以及背后的含义，如果双方的协议不遵守某一标准将可能导致一方无法理解另一方的行为，从而导致通信失败。

## 1.2

### R4

- 住宅接入：DSL、电缆因特网接入、FTTH
- 公司接入：LAN, Wi-Fi
- 广域无线接入：固定5G基站，4G，3G

### R5

HFC的传输速率共享，下行HFC中不会发生碰撞，因为下行HFC由头端进行广播发送，头端会依次地发送数据，而不会发生碰撞。

### R6

我家目前使用FTTH接入，曾经使用过DSL拨号上网，具体的速度和费用待查。

### R7

目前主流的超五类和六类以太网线的传输速率为1000Mbps。

### R8

双绞线、同轴线缆、光纤、陆地和卫星无线通道

### R9

|    比较项目    | 拨号调制解调器 |       HFC      |        DSL      |   FTTH   |
| :-----------: | :-----------: | :------------: | :-------------: | :------: |
|  上行传输速率  |     56kbps    | 30Mbps/100Mbps |  3.5Mbps/16Mbps |  20Mbps  |
|  下行传输速率  |     56kbps    | 40Mbps/1.2Gbps |  24Mbps/52Mbps  |  20Mbps  |
|    传输距离    |     3km       |      100km     |     5-10英里    |   20km   |
|  速率是否共享  | 否 | 是 | 否 | 是 |

### R10

家庭大多使用FTTH接入并使用WiFi和以太网建立内部连接。此外某些个人设备使用蓝牙连接。

## 1.3

### R11

$$
\text{总时延} = 2 \times \frac{L}{\min{(R_1, R_2)}}
$$

### R12

电路交换更稳定，更适合实时服务

TDM相对于FDM更灵活

### R13

#### a

最多两个用户

#### b

两个用户共同使用链路时链路内的数据传输速率为 2Mbps 与链路的最大传输率相同，三个及以上用户共享链路时超出链路的最大承载量，发生排队

#### c

与传输的时间比率相同，为$0.2$

#### d

同时传输的概率为 $0.2^3 = 0.008$, 此即队列增长的时间比率

### R14

相互直接传送流量，从而减少向上层ISP支付的费用。

第三方可以建立IXP使得多个ISP可以相互对等，IXP可以收取恰当的费用。

### R15

谷歌拥有大量的数据中心，这些数据中心经过专用的TCP/IP网络互联，组成专用网络，仅承载谷歌的流量。

目的是减少向第一层ISP支付的费用，并提高数据传输的速度，还可以对服务如何交付客户端有更多的控制。

## 1.4

### R16

### R17

### R18

### R19

### R20

### R21

## 1.5

### R22

### R23

### R24

### R25

## 1.6

### R26

### R27

### R28
