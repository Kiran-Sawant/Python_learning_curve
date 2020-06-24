import time
import multiprocessing as multi

start_time = time.perf_counter()

def do_something():
    print('Sleep for a while')
    time.sleep(1)
    print('Done sleeping')

p1 = multi.Process(target=do_something)
p2 = multi.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

end_time = time.perf_counter()

print(f"Time Consumed: {end_time - start_time:.2f} sec")