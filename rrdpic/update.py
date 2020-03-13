# -*- coding: utf-8 -*-
import rrdtool

import time,psutil

total_input_traffic=psutil.net_io_counters()[1]
total_ouput_traffic=psutil.net_io_counters()[0]

starttime=int(time.time())

update=rrdtool.updatev('Flow.rrd','%s:%s:%s'%(str(total_input_traffic),str(total_ouput_traffic),str(starttime)))
print(update)
