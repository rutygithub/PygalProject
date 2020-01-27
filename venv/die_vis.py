from die import Die
import pygal

die = Die()
res = []
for i in range(1, 1000):
    single_res = die.roll()
    res.append(single_res)

print(res)

freqs = []
for v in range(1, die.side + 1):
    single_freq = res.count(v)
    freqs.append(single_freq)

print(freqs)

histogram = pygal.Bar()
histogram.title = 'results of rolling the die'
histogram.x_labels = ['1', '2', '3', '4', '5', '6']
histogram.x_title='result'
histogram.y_title = 'frequncy of results'

histogram.add('Die6', freqs)
histogram.render_to_file('die_visual4.svg')
