import os

def initialize_matrix():
    """Initialize the matrix from user input."""
    mat = []
    a = int(input("Enter number of rows: "))
    for x in range(a):
        mat.append(list(input(f"Enter row {x+1}: ")))
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
                sum_dict[mat[x][y]] = operation_func(x,y)
            else:
                sum_dict[mat[x][y]] += operation_func(x, y)
    return sum_dict

def print_results(div, sum_dict, description):
    """Print results for each key in div."""
    for key in div.keys():
        print(f"Matching for device for {description} {key} is {sum_dict[key] / div[key]}")

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
    with open("plot_data.txt", "w") as f:
        for i, key in enumerate(sum_dict.keys(), start=1):
            f.write(f"{i} \"{key}\" {sum_dict[key] / div[key]}\n")  # Assign numeric values for the x-axis, but still display string labels

    # Create the Gnuplot script
    gnuplot_script = f"""
        set title "Matching for {description}"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set xtics format "%s"  # Format x-tics as strings
        plot "plot_data.txt" using 1:3:xtic(2) with linespoints title "{description} values"
        pause -1
    """

    # Write the Gnuplot script to a file
    with open("gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    # Execute Gnuplot with the script
    os.system("gnuplot gnuplot_script.gp")


def clubed_plot(dict_div_sum, div):
    """Plot all dictionaries in list_div_sum on one graph with different colors."""
    # setting max value to be 100 for much clean graph
    # and min value 0
    MAX_GRAPH = 100
    MIN_GRAPH = 0
    for relation in dict_div_sum:
        MAX_VALUE = -1000000000000
        MIN_VALUE = +1000000000000
        for divise in dict_div_sum[relation]:
                MAX_VALUE = max(MAX_VALUE,dict_div_sum[relation][divise]/div[divise])
                MIN_VALUE = min(MIN_VALUE,dict_div_sum[relation][divise]/div[divise])
        for divise in dict_div_sum[relation]:
            if MAX_VALUE == MIN_VALUE:
                dict_div_sum[relation][divise] = 0
                continue
            dict_div_sum[relation][divise] = (dict_div_sum[relation][divise]/div[divise] - MIN_VALUE)/(MAX_VALUE - MIN_VALUE) * (MAX_GRAPH - MIN_GRAPH) + MIN_GRAPH
    allplots = ''
    line_style = 1
    for relation in dict_div_sum:
        with open(relation+".txt","w") as f:
            for i, key in enumerate(dict_div_sum[relation].keys(), start=1):
                f.write(f"{i} \"{key}\" {dict_div_sum[relation][key]}\n")  # normalize this value to be max equal to MAX_GRAPH mand min to MIN_GRAPH
        allplots += f'"{relation}.txt" using 1:3:xtic(2) title "{relation} values" with line linestyle {line_style},'
        line_style += 1

    gnuplot_script = f"""
        set title "Normalized Matchings (MAX = {MAX_GRAPH}, MIN = {MIN_GRAPH})"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set xtics format "%s"  # Format x-tics as strings
        plot {allplots}
        pause -1
    """

    # Write the Gnuplot script to a file
    with open("gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    # Execute Gnuplot with the script
    os.system("gnuplot gnuplot_script.gp")

def list_plot(dict_div_sum, div):
    """Plot all dictionaries in list_div_sum in the same graph."""
    allplots = ''
    for relation in dict_div_sum:
        with open(relation+".txt","w") as f:
            for i, key in enumerate(dict_div_sum[relation].keys(), start=1):
                f.write(f"{i} \"{key}\" {dict_div_sum[relation][key] / div[key]}\n")  # Assign numeric values for the x-axis, but still display string labels
        allplots += f"""plot "{relation+".txt"}" using 1:3:xtic(2) with linespoints title "{relation} values
        """

    gnuplot_script = f"""
        set xlabel "Device"
        set ylabel "Average"
        set multiplot layout {int(len(dict_div_sum)**0.5)},{int(len(dict_div_sum))**0.5 if (int(len(dict_div_sum))**2 == len(dict_div_sum)) else  int(len(dict_div_sum))**0.5+1} columns
        set xtics format "%s"  # Format x-tics as strings
        {allplots}
        unset multiplot
        pause -1
    """

    # Write the Gnuplot script to a file
    with open("gnuplot_script.gp", "w") as f:
        f.write(gnuplot_script)

    # Execute Gnuplot with the script
    os.system("gnuplot gnuplot_script.gp")

def main():
    mat = initialize_matrix()
    div = initialize_div(mat)  # map/dictionary of device to its frequency
    dict_div_sum = {}
    # Calculate and plot results for each operation
    dict_div_sum["X"] = calculate_matching_values(mat, div, op_x)
    # print_results(div, dict_div_sum["X"], "x")
    # plot(dict_div_sum["X"], div, "x")

    dict_div_sum["Y"] = calculate_matching_values(mat, div, op_y)
    # print_results(div, sum_dict_2, "y")
    # plot(sum_dict, div, "y")

    dict_div_sum["squar(X)"] = calculate_matching_values(mat, div, op_x_squared)
    # print_results(div, sum_dict_3, "x^2")
    # plot(sum_dict, div, "x^2")

    dict_div_sum["squar(Y)"] = calculate_matching_values(mat, div, op_y_squared)
    # print_results(div, sum_dict_4, "y^2")
    # plot(sum_dict, div, "y^2")

    dict_div_sum["X*Y"] = calculate_matching_values(mat, div, op_xy)
    # print_results(div, sum_dict_5, "x*y")
    # plot(sum_dict, div, "x*y")

    dict_div_sum["squar(X)*squar(Y)"] = calculate_matching_values(mat, div, op_x_squared_y_squared)
    # print_results(div, sum_dict_6, "x^2*y^2")
    # plot(sum_dict, div, "x^2 + y^2")
    list_plot(dict_div_sum,div)
    clubed_plot(dict_div_sum,div)
# Call the main function
if __name__ == "__main__":
    main()
