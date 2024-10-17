
        set title "Normalized Matchings (MAX = 100, MIN = 0)"
        set xlabel "Device"
        set ylabel "Average"
        set grid
        set xtics format "%s"  # Format x-tics as strings
        plot "temp/X.txt" using 1:3:xtic(2) title "X values" with line linestyle 1,"temp/Y.txt" using 1:3:xtic(2) title "Y values" with line linestyle 2,"temp/squar(X).txt" using 1:3:xtic(2) title "squar(X) values" with line linestyle 3,"temp/squar(Y).txt" using 1:3:xtic(2) title "squar(Y) values" with line linestyle 4,"temp/X*Y.txt" using 1:3:xtic(2) title "X*Y values" with line linestyle 5,"temp/squar(X)*squar(Y).txt" using 1:3:xtic(2) title "squar(X)*squar(Y) values" with line linestyle 6,
        pause -1
    