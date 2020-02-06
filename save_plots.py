import matplotlib.pyplot as plt
import matplotlib
import os
import numpy as np

def run_subplot(data, labels, filename, format=True, plot_type=1, legends=[], *args):
    """
        Save plots as pdf/pgf for LaTeX
        legends = [] - default
        plot_type = 1 - plot, 2 - scatter
        format = True - pdf, False - pgf
    """

    # Adjust your matplotlib script by adding the following lines after import matplotlib
    if format == True:
        matplotlib.use("pdf")
    else:
        matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })

    # add LaTeX on python path
    user_name = os.getlogin()
    os.environ["PATH"] += os.pathsep + 'C:/Users/' + user_name + '/AppData/Local/Programs/MiKTeX 2.9/miktex/bin/x64'
    print(os.getenv("PATH"))

    #===========================     Using LaTeX compatible fonts      =============================== #
    # use LaTeX fonts in the plot
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    # get the figure
    fig = plt.figure()

    # plot
    if plot_type==1:    # plot
        if not legends: # if legends are given
            if data.shape[1] == 1:
                plt.plot(data[0][0], alpha=0.8)
            else:
                plt.plot(data[0][0], data[0][1], alpha=0.8)
        else:
            for count, lines in enumerate(data):
                plt.plot(lines[0], lines[1], label=legends[count], alpha=0.8)
            plt.legend()
    else:
        if not legends:  # if legends are given
            if data.shape[1] == 1:
                plt.scatter(data[0][0], alpha=0.8)
            else:
                plt.scatter(data[0][0], data[0][1], alpha=0.8)
        else:
            for count, points in enumerate(data):
                plt.scatter(points[0], points[1], label=legends[count], alpha=0.8)
            plt.legend()


    # if len(args)==1:
    #     plt.plot(args[0], args[1], label=legends[1])


    # set labels (LaTeX can be used)
    # plt.title(r'\textbf{Mutual Information Feature Selection}', fontsize=11)
    plt.xlabel(r'{}'.format(labels[0]), fontsize=11)
    plt.ylabel(r'{}'.format(labels[1]), fontsize=11)

    # plt.show()

    save_plots(fig, format, filename)


def save_plots(fig, format, filename):

    # =============================      Save the image as pdf/pgf    # ======================================== #
    if format == True:
        # save as PDF
        fig.savefig("{}.pdf".format(filename), bbox_inches='tight', dpi=300)
    else:
        # save as PGF
        fig.set_size_inches(w=3, h=2)
        fig.savefig('{}.pgf', format(filename))


# # Example
# # x axis
# x1 = range(5, 14)
# x2 = range(5, 14)
#
# # y axis
# y1 = np.array([0.77627718442, 0.779758651376, 0.779831336605, 0.780332508531, 0.780986909681, 0.803343901758,
#            0.804763267426, 0.799750946218, 0.801493061947])
# y2 = [0.5627718442, 0.59758651376, 0.6831336605, 0.80332508531, 0.50986909681, 0.803343901758,
#            0.54763267426, 0.3750946218, 0.31493061947]
#
# labels = ['x', 'y']
# legends = ['aa', 'bb']
# filename = 'deneme'
#
# # initialize array with size number of lines
# data = np.full((2,2), None) # row: number of lines, col.: dimension of the plot (e.g., (1,2) -> 1 line with x and y values)
#
# # fill data array with data points [x,y,z]
# data[0] = [x1,y1]
# data[1] = [x2,y2]
# # etc...
#
# run_subplot(data, labels, filename, legends=legends, plot_type=2)