from l1tool import l1filter, gen_d2, main
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = main(['-f', './ynsm_up.dat', '-l', '2000'])
ax = plt.subplot(411)
df['component'].plot(ax=ax, marker='.', color='k', markersize=0.5, linewidth=0)
ax.plot(df.index,
        df['trends'] + df['level'] + df['seasonal'],
        '-r', linewidth=1.0)
label = ['ynsm_up', 'Trends + Level + Seasonal']
ax.legend(label, ncol=2)
ax.grid()
ax.set_ylabel('mm')
plt.setp(ax.get_xticklabels(), visible=False)
for i, col in enumerate(('trends', 'level', 'seasonal')):
    ax = plt.subplot(412 + i)
    df[col].plot(ax=ax)
    ax.set_ylabel('mm')
    ax.grid()
    ax.legend([col], loc=2)
    if i < 2:
        plt.setp(ax.get_xticklabels(), visible=False)


plt.subplots_adjust(hspace=0.0)
plt.savefig('ynsm_up.png', dpi=300, bbox_inches='tight')
plt.show()
