import matplotlib.pyplot as plt
import matplotlib
import os

def save_plot(x, y, labels, legends, format, filename, *args):
    """
        Save plots as pdf/pgf for LaTeX
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
    os.environ["PATH"] += os.pathsep + 'C:/Users/berkc/AppData/Local/Programs/MiKTeX 2.9/miktex/bin/x64'
    print(os.getenv("PATH"))

    #===========================     Using LaTeX compatible fonts      =============================== #
    # use LaTeX fonts in the plot
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    # get the figure
    fig = plt.figure()

    # plot
    plt.plot(x, y, label=legends[0])
    if args:
        plt.plot(args[0], args[1], label=legends[1])

    plt.legend()
    # set labels (LaTeX can be used)
    # plt.title(r'\textbf{Mutual Information Feature Selection}', fontsize=11)
    plt.xlabel(r'{}'.format(labels[0]), fontsize=11)
    plt.ylabel(r'{}'.format(labels[1]), fontsize=11)

    # plt.show()

    #=============================      Save the image as pdf/pgf    # ======================================== #
    if format == True:
        # save as PDF
        fig.savefig("{}.pdf".format(filename), bbox_inches='tight', dpi=300)
    else:
        # save as PGF
        fig.set_size_inches(w=3, h=2)
        fig.savefig('{}.pgf',format(filename))



# # Example
# # x axis
# ks = range(5, 14)
#
# # y axis
# results = [0.77627718442, 0.779758651376, 0.779831336605, 0.780332508531, 0.780986909681, 0.803343901758,
#            0.804763267426, 0.799750946218, 0.801493061947]
# labels = ['x', 'y']
# legends='aa'
# save_plot(ks,results,labels,legends,True)