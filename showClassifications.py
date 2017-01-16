import numpy as np
import matplotlib.pyplot as plt
from displaySamples import display_samples
from signIDtoName import sign_id_to_name

rank_names = {0: 'Correct recognition',
               1: 'The target class as second guesses',
               2: 'The target class as third guesses'
}

def rank_label(i, k):
    if k <= i:
        return str.format("The target class as beyond {}-th guesses", k)
    else:
        return rank_names.get(i, str.format('The target class as {}-th guesses', i+1))

def show_rank_counts(rank_counts, k):
    l = len(rank_counts)
    # The slices will be ordered and plotted counter-clockwise.
    colors = ['gold', 'yellowgreen', 'lightskyblue', 'lightcoral', 'cyan', 'red', 'magenta']
    explode = (0.2, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice
    assert(l <= len(colors))
    assert(l <= len(explode))
    patches, texts = plt.pie(rank_counts, explode=explode[:l], colors=colors[:l], shadow=True, startangle=90)
    # autopct='%1.2f%%', labels=labels
    total = sum(rank_counts)
    labels = [str.format('{:04.1f}% - {}', 100*rank/total, rank_label(i, k))
              for i, rank in zip(range(l), rank_counts)]
    plt.legend(patches, labels, loc='best', bbox_to_anchor=(-0.1, 1.), fontsize=8)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

def show_classifications(ranks, classified, xx, yy, k = 3, limit = 10):
    rank_counts = np.zeros(k+1, dtype=np.int)
    total_cases = len(yy)
    for j in range(len(rank_counts)):
        matched_idices = np.where(np.array(ranks) == j)
        rank_counts[j] = matched_idices[0].size
    show_rank_counts(rank_counts, k)
    for j in range(len(rank_counts)):
        if 0 < rank_counts[j]:
            print(str.format('{}: {:.2f}%, partial samples:', rank_label(j, k), (rank_counts[j]/total_cases)*100))
            display_samples(xx[matched_idices], np.array(classified)[matched_idices], 'Classified:',
                            yy[matched_idices], 'Expected:', sign_id_to_name, columns=5,
                            indices = slice(0, min(rank_counts[j], limit)))
    return rank_counts
