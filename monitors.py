from screeninfo import get_monitors
from screeninfo.common import Monitor

def detect_monitor()->Monitor:
    monitors = get_monitors()
    monitor:Monitor
    for m in monitors:
        print(m)
        if(m.is_primary == True):
            monitor = m
    return monitor