import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import math
def display_samples(X, title, title_str, xlabel, xlabel_str, class_dict, columns = 5, indices = slice(None, None, None)):
    #print(str.format('indices: {}', indices))
    X = X[indices]
    title = title[indices]
    if xlabel.size > 0:
        xlabel = xlabel[indices]

    cases = len(X)
    rows = math.ceil(cases/columns)
    gs1 = gridspec.GridSpec(rows, columns)
    gs1.update(wspace=0.9, hspace=0.9) # set the spacing between axes. 
    plt.figure(figsize=(columns*4, rows*2))
    for i in range(cases):
        ax1 = plt.subplot(gs1[i])
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.set_aspect('equal')
        ax1.set_title(str.format('{} {}', title_str, class_dict[title[i]]))
        if xlabel.size > 0:
            ax1.set_xlabel(str.format('{} {}', xlabel_str, class_dict[xlabel[i]]))
        plt.imshow(X[i])
    plt.show()
