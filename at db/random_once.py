from dpark import DparkContext
dpark = DparkContext()
count = dpark.accumulator(0)

def random_once(*args, **kwrgs):
    x = random() * 2 - 1
    y = random() * 2 - 1
    if x * x + y * y < 1:
        count.add(1)

depark.parallelize(range(0, N), 10).foreach(random_once)
print 'PI is roughly ', 4.0 * count.value / N
