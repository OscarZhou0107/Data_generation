import pygal
from die import Die
die1 = Die();
die2 = Die(10);
results  = []
for roll in range(50000):
    result = die1.roll()+die2.roll()
    results.append(result)
frequencies =[]
for value in range(2,die1.num_sides+die2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title="Result of rolling two Dices 1000 times"
hist.x_labels =['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6+D10',frequencies)
hist.render_to_file('die.visual.svg')
