from __future__ import with_statement
import os

def initialize_matrix():
    """Initialize the matrix from user input."""
    mat = []
    a = int(raw_input("Enter number of rows: "))
    for x in range(a):
        mat.append(list(raw_input("Enter row {0}: ".format(x + 1))))
    return mat

def initialize_div(mat):
    """ map/dictionary of device to its frequency """
    div = {}
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] not in div:
                div[mat[x][y]] = 1
            else:
                div[mat[x][y]] += 1
    return div

def calculate_matching_values(mat, div, operation_func):
    """Calculate matching values for a given operation."""
    sum_dict = {}
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] not in sum_dict:
                sum_dict[mat[x][y]] = operation_func(x, y)
            else:
                sum_dict[mat[x][y]] += operation_func(x, y)
    return sum_dict

def print_results(div, sum_dict, description):
    """Print results for each key in div."""
    for key in div.keys():
        print("Matching for device for {0} {1} is {2}".format(description, key, float(sum_dict[key]) / div[key]))

# Operation functions
def op_x(x, y): return x + 1
def op_y(x, y): return y + 1
def op_x_squared(x, y): return (x + 1) ** 2
def op_y_squared(x, y): return (y + 1) ** 2
def op_xy(x, y): return (x + 1) * (y + 1)
def op_x_squared_y_squared(x, y): return (x + 1) ** 2 * (y + 1) ** 2

def plot(sum_dict, div, description):
    """Plot the graph using Gnuplot."""
    # Create a temporary data file
    with open("temp/plot_data.txt", "w") as f:
        for i, key in enumerate(sum_dict.keys(), start=1):
            f.write("{0} \"{1}\" {2}\n".format(i, key, float(sum_dict[key]) / div[key]))

    # Create the Gnuplot script
    gnuplot_script = """
        set title "Matching for {0}"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set xtics format "%s"  # Format x-tics as strings
        plot "temp/plot_data.txt" using 1:3:xtic(2) with linespoints title "{0} values"
        pause -1
    """.format(description)

    # Write the Gnuplot script to a file
    with open("temp/gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    # Execute Gnuplot with the script
    os.system("gnuplot temp/gnuplot_script.gp")

def clubed_plot(dict_div_sum, div):
    """Plot all dictionaries in list_div_sum on one graph with different colors."""
    MAX_GRAPH = 100
    MIN_GRAPH = 0
    for relation in dict_div_sum:
        MAX_VALUE = -1000000000000
        MIN_VALUE = +1000000000000
        for device in dict_div_sum[relation]:
            MAX_VALUE = max(MAX_VALUE, float(dict_div_sum[relation][device]) / div[device])
            MIN_VALUE = min(MIN_VALUE, float(dict_div_sum[relation][device]) / div[device])
        for device in dict_div_sum[relation]:
            if MAX_VALUE == MIN_VALUE:
                dict_div_sum[relation][device] = 0
                continue
            dict_div_sum[relation][device] = (float(dict_div_sum[relation][device]) / div[device] - MIN_VALUE) / (MAX_VALUE - MIN_VALUE) * (MAX_GRAPH - MIN_GRAPH) + MIN_GRAPH

    allplots = ''
    line_style = 1
    for relation in dict_div_sum:
        with open("temp/" + relation + ".txt", "w") as f:
            for i, key in enumerate(dict_div_sum[relation].keys(), start=1):
                f.write("{0} \"{1}\" {2}\n".format(i, key, dict_div_sum[relation][key]))
        allplots += '"temp/{0}.txt" using 1:3:xtic(2) title "{0} values" with lines linestyle {1},'.format(relation, line_style)
        line_style += 1
    allplots = allplots[:-1]

    gnuplot_script = """
        set title "Normalized Matchings (MAX = {0}, MIN = {1})"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set xtics format "%s"
        plot {2}
        pause -1
    """.format(MAX_GRAPH, MIN_GRAPH, allplots)

    with open("temp/gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    os.system("gnuplot temp/gnuplot_script.gp")

def list_plot(dict_div_sum, div):
    """Plot all dictionaries in list_div_sum in the same graph."""
    allplots = ''
    for relation in dict_div_sum:
        with open("temp/" + relation + ".txt", "w") as f:
            for i, key in enumerate(dict_div_sum[relation].keys(), start=1):
                f.write("{0} \"{1}\" {2}\n".format(i, key, float(dict_div_sum[relation][key]) / div[key]))
        allplots += 'plot "temp/{0}.txt" using 1:3:xtic(2) with linespoints title "{0} values\n'.format(relation)

    gnuplot_script = """
        set xlabel "Device"
        set ylabel "Average"
        set multiplot layout {0},{1}
        set xtics format "%s"
        {2}
        unset multiplot
        pause -1
    """.format(int(len(dict_div_sum) ** 0.5), int(len(dict_div_sum) ** 0.5) if len(dict_div_sum) ** 2 == len(dict_div_sum) else int(len(dict_div_sum) ** 0.5) + 1, allplots)

    with open("temp/gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    os.system("gnuplot temp/gnuplot_script.gp")

def main():
    mat = initialize_matrix()
    div = initialize_div(mat)  # map/dictionary of device to its frequency
    dict_div_sum = {}
    # Calculate and plot results for each operation
    dict_div_sum["X"] = calculate_matching_values(mat, div, op_x)
    dict_div_sum["Y"] = calculate_matching_values(mat, div, op_y)
    dict_div_sum["squar(X)"] = calculate_matching_values(mat, div, op_x_squared)
    dict_div_sum["squar(Y)"] = calculate_matching_values(mat, div, op_y_squared)
    dict_div_sum["X*Y"] = calculate_matching_values(mat, div, op_xy)
    dict_div_sum["squar(X)*squar(Y)"] = calculate_matching_values(mat, div, op_x_squared_y_squared)

    list_plot(dict_div_sum, div)
    # clubed_plot(dict_div_sum, div)

# Call the main function
if __name__ == "__main__":
    main()
