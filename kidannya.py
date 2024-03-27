import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

N = 17  
num_samples = 10  

def roll_dice(N, symmetric=True):
    if symmetric:
        return np.random.randint(1, N+1, 2) 
    else:
        return np.random.randint(1, N+1), np.random.choice(range(1, N+1), p=np.arange(1, N+1)/sum(np.arange(1, N+1)))

results_symmetric = np.array([sum(roll_dice(N, symmetric=True)) for _ in range(num_samples)])
results_asymmetric = np.array([sum(roll_dice(N, symmetric=False)) for _ in range(num_samples)])

fig = make_subplots(rows=1, cols=2, subplot_titles=['Симетричні кубики', 'Асиметричний другий кубик'])

print("Симетричні кубики:")
for i in range(num_samples):
    dice_results = roll_dice(N, symmetric=True)
    sum_result = sum(dice_results)
    print(f"Результат кидка: {dice_results} Сума результатів: {sum_result}")
    fig.add_trace(go.Bar(x=[sum_result], y=[1], name=f"Кидок {i+1}"), row=1, col=1)

print("\nАсиметричний другий кубик:")
for i in range(num_samples):
    dice_results = roll_dice(N, symmetric=False)
    sum_result = sum(dice_results)
    print(f"Результат кидка: {dice_results} Сума результатів: {sum_result}")
    fig.add_trace(go.Bar(x=[sum_result], y=[1], name=f"Кидок {i+1}"), row=1, col=2)

fig.update_layout(title='Гістограма сум результатів кидків двох кубиків', barmode='group')
fig.update_xaxes(title_text='Сума результатів', row=1, col=1)
fig.update_xaxes(title_text='Сума результатів', row=1, col=2)
fig.update_yaxes(title_text='Частота', row=1, col=1)

pio.write_html(fig, file='histogram.html', auto_open=True)