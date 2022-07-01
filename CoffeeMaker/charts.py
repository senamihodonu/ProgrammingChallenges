import matplotlib.pyplot as plt

def methods_to_ratings_bar(methods):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.set_ylim(0,100)
    axes.bar(
        range(len(methods)),
        [method[1] for method in methods],
        tick_label=[method[0] for method in methods]
    )
    return figure