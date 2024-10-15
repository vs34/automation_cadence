
        set title "Clubbed Plot"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set style data linespoints
        set xtics rotate by -45
        set key outside
    plot "clubed_plot_data.txt" index 0 using 1:3:xtic(2) title "Dataset 1" with linespoints
plot "clubed_plot_data.txt" index 1 using 1:3:xtic(2) title "Dataset 2" with linespoints
plot "clubed_plot_data.txt" index 2 using 1:3:xtic(2) title "Dataset 3" with linespoints
plot "clubed_plot_data.txt" index 3 using 1:3:xtic(2) title "Dataset 4" with linespoints
plot "clubed_plot_data.txt" index 4 using 1:3:xtic(2) title "Dataset 5" with linespoints
plot "clubed_plot_data.txt" index 5 using 1:3:xtic(2) title "Dataset 6" with linespoints
