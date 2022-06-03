import matplotlib.pyplot as plt

BLEU_scores = [1.2, 1.6, 1.8, 1.9, 2.0, 2.0, 2.1, 2.1, 2.1, 2.1, 2.1]
beam_size = [1, 2, 3, 4, 5, 9, 10, 12, 15, 18, 35]

fig, ax = plt.subplots()
ax.plot(beam_size, BLEU_scores, c='lightpink')

hfont = {'fontname':'Helvetica Neue', 'fontweight':'ultralight'}

ax.set_xlabel('beam size (k)', fontsize=14, **hfont)
ax.set_ylabel('BLEU', fontsize=14, **hfont)
ax.set_title('BLEU in relation to Beam Size', fontsize=18, **hfont)
ax.grid(c='#f5f5f5')


fig.savefig("beam_BLEU.png")
plt.show()


