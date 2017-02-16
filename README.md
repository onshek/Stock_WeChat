# Stosk_WeChat


This package supports only Python 3.x.


## Installation

    $ pip install Stosk_WeChat

## Quich Start

    from Stock_WeChat import reminder

The result is:

	请输入股票代码 
	>  000002
	请输入最低预警价格 
	>  20
	请输入最高预警价格 
	>  21

Then:

	reminder.run_task()

The result is:

	Getting uuid of QR code.
	Downloading QR code.
	Please scan the QR code to log in.
	Please press confirm on your phone.
	Login successfully as ipreacher
	12:06:40
	000002 的当前价格为 20.62


## License

MIT