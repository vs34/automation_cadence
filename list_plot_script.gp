
        set terminal qt size 800,600  # QT terminal for interactive plotting
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set style data linespoints
        set xtics rotate by -45
        set xtics format "%s"
        set title "All datasets on the same graph"
        plot \
    'list_plot_data.txt' index 0 using 1:3:xtic(2) title 'Dataset 1' with linespoints, \
'list_plot_data.txt' index 1 using 1:3:xtic(2) title 'Dataset 2' with linespoints, \
'list_plot_data.txt' index 2 using 1:3:xtic(2) title 'Dataset 3' with linespoints, \
'list_plot_data.txt' index 3 using 1:3:xtic(2) title 'Dataset 4' with linespoints, \
'list_plot_data.txt' index 4 using 1:3:xtic(2) title 'Dataset 5' with linespoints, \
'list_plot_data.txt' index 5 using 1:3:xtic(2) title 'Dataset 6' with linespoints