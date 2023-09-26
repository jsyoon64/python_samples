import re
    
mystring2 = """
12:00:50.972     Metrotask.c  362 H (0)Act P: -0.012W, E: 0.000Wh, V: 236.394V, I: 0.001A
12:00:50.972     Metrotask.c  379 H (1)Act P: 0.004W, E: 0.000Wh, V: 237.104V, I: 0.001A
12:00:50.972 (0)Raw RMS volt: 6662, Curr: 6
12:00:50.973 rtxstate_send.c  137 H vRTX SEND State Entered.
12:00:50.973 rtxstate_send.c  321 H Send data packet.
12:00:53.518  net_cfg_wifi.c  444 H ERROR Response ERROR(1).
12:00:53.518 rtxstate_send.c  391 E Time out. Response failed
12:00:53.971     Metrotask.c  362 H (0)Act P: -0.014W, E: 0.000Wh, V: 236.288V, I: 0.001A
12:00:53.972     Metrotask.c  379 H (1)Act P: 0.048W, E: 0.000Wh, V: 236.962V, I: 0.001A
12:00:53.972 (0)Raw RMS volt: 6659, Curr: 6
12:00:53.972 rtxstate_send.c  321 H Send data packet.
"""

pattern2 = 'Raw RMS volt:'

""" Raw RMS volt: 6662 """
p = re.compile(pattern2 + r'\s+\d+')

""" 6662 """
q = re.compile(pattern2 + r'\s+(\d+)')

""" [('Raw RMS volt: 6662', '6662'), ('Raw RMS volt: 6659', '6659')] """
r = re.compile('('+pattern2+r'\s+(?P<val>\d+)'+')')
#print(p)
if pattern2 in mystring2:
    m = p.findall(mystring2)
    print('len=',len(m),',',m)

    m = q.findall(mystring2)
    print('len=', len(m), ',', m)
    
    m = r.search(mystring2)
    print('m -> ',m)
    print("'m.group(0) ->",m.group(0))
    print("'m.group('val') ->", m.group('val'))
    

p = re.compile(r'Raw RMS volt:\s+\d+,')
if 'Raw RMS volt' in mystring2:
    m = p.findall(mystring2)
    print(m)
