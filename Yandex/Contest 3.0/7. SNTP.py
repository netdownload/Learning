time_start, time_serv, time_end = open('input.txt').read().splitlines()


def time_in_sec(t):
    h, m, s = t.split(':')
    tis = int(h) * 60 * 60 + int(m) * 60 + int(s)
    return tis


if time_in_sec(time_end) < time_in_sec(time_start):
    time_dif = (24*60*60 - time_in_sec(time_start) + time_in_sec(time_end))/2
else:
    time_dif = (time_in_sec(time_end) - time_in_sec(time_start))/2

if time_dif - int(time_dif) >= 0.5:
    time_dif = int(time_dif) + 1
else:
    time_dif = int(time_dif)

time_real = time_in_sec(time_serv) + time_dif

s = time_real % (24 * 3600)
h = s // 3600
s %= 3600
m = s // 60
s %= 60
print('%02d:%02d:%02d' % (h, m, s))
