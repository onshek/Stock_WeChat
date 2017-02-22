# Stock_WeChat

微信股价预警提示

This package supports only Python 3.x.


## Installation

    $ pip install Stosk_WeChat

## How to Use

### 登陆个人微信

    >>> from Stock_WeChat import sw
    >>> sw.login()
    Getting uuid of QR code.
    Downloading QR code.
    Please scan the QR code to log in.
    Please press confirm on your phone.
    Login successfully as ipreacher


### 开启推送模式
* 每 3 秒推送一次
* 关键词：'股票代码', 最低预警价格, 最高预警价格

    >>> sw.push('000002', 20, 21)
    14:06:36
    000002 的当前价格为 20.92
    价格正常

### 开启提醒模式
* 每 3 秒获取一次股价
* 如果超过预警价格则发送信息至微信
* 关键词：'股票代码', 最低预警价格, 最高预警价格

    >>> sw.remind('000002', 21, 22)
    14:07:01
    000002 的当前价格为 20.92
    低于最低预警价格


## Comments

You can commit an Issue if you have any question or suggestion.


## License

MIT
