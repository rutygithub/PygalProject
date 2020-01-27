import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

res = []
for roll_num in range(1, 1000):
    single_res1 = die_1.roll()
    single_res2 = die_2.roll()
    single_res = single_res1 + single_res2
    res.append(single_res)

freqs = []
for v in range(2, 17):
    single_freq = res.count(v)
    freqs.append(single_freq)

print(freqs)
his = pygal.Bar()
his.title = 'result of rolling two different dice'
his.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
his.x_title = 'result'
his.y_title = 'freq of result'

his.add('dice', freqs)
his.render_to_file('diff_die.svg')
