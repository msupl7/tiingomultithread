from sp500 import *
import threading
import time
fx = clsfunctions()
startTime = time.time()

t1 = threading.Thread(target=fx.tiingo,args=(0, 50))
t2 = threading.Thread(target=fx.tiingo,args=(50, 100))
t3 = threading.Thread(target=fx.tiingo,args=(100, 150))
t4 = threading.Thread(target=fx.tiingo,args=(150, 200))
t5 = threading.Thread(target=fx.tiingo,args=(200, 250))
t6 = threading.Thread(target=fx.tiingo,args=(250, 300))
t7 = threading.Thread(target=fx.tiingo,args=(300, 350))
t8 = threading.Thread(target=fx.tiingo,args=(350, 400))
t9 = threading.Thread(target=fx.tiingo,args=(400, 450))
t10 = threading.Thread(target=fx.tiingo,args=(450, 501))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()


print(round(time.time() - startTime, 2), ' seconds')