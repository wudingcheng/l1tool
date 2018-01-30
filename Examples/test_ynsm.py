#!/usr/env/bin python
# encoding: utf-8

from l1tool import l1filter, reader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = 'ynsm_up.dat'
df = reader(filename)
x, w, s = components = l1filter(df['t'].values,
                                df['component'].values,
                                periods=(365.25, 186.725),
                                lam=2000,
                                rho=80,
                                verbose=True)
df['trends'] = components[0]
df['level'] = components[1]
df['seasonal'] = components[2]

df.pop('t')
df.to_csv('ynsm_up_out.dat', float_format='%.2f', sep=' ')


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
