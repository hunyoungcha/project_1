import time
import datacon as dc

time_s=dc.get_data('cha','uname','time')

print( time_s==f'{time.localtime().tm_hour}:{time.localtime().tm_min}')
