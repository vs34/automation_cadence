#include <gtk/gtk.h>
#include <cairo.h>

// Function to draw the graph
gboolean draw_callback(GtkWidget *widget, cairo_t *cr, gpointer data) {
    // Get the dimensions of the drawing area
    int width = gtk_widget_get_allocated_width(widget);
    int height = gtk_widget_get_allocated_height(widget);

    // Set the background color (white)
    cairo_set_source_rgb(cr, 1, 1, 1);
    cairo_paint(cr);

    // Draw the axes (black)
    cairo_set_source_rgb(cr, 0, 0, 0);
    cairo_set_line_width(cr, 2.0);
    cairo_move_to(cr, 50, 10);  // y-axis
    cairo_line_to(cr, 50, height - 50);
    cairo_line_to(cr, width - 10, height - 50);  // x-axis
    cairo_stroke(cr);

    // Sample graph data points
    double data[] = {10, 20, 30, 50, 80, 130, 100};
    int data_len = sizeof(data) / sizeof(data[0]);

    // Scale factors
    double x_scale = (width - 60) / (data_len - 1);
    double y_scale = (height - 60) / 130.0;  // Assuming max value is 130

    // Plot the data (in red)
    cairo_set_source_rgb(cr, 1, 0, 0);
    cairo_set_line_width(cr, 2.0);

    // Move to the first data point
    cairo_move_to(cr, 50, height - 50 - data[0] * y_scale);

    // Draw the lines between data points
    for (int i = 1; i < data_len; i++) {
        cairo_line_to(cr, 50 + i * x_scale, height - 50 - data[i] * y_scale);
    }

    cairo_stroke(cr);

    return FALSE;
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *drawing_area;

    // Initialize GTK
    gtk_init(&argc, &argv);

    // Create the main window
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Graph with GTK and Cairo");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 300);

    // Create the drawing area
    drawing_area = gtk_drawing_area_new();
    gtk_container_add(GTK_CONTAINER(window), drawing_area);

    // Connect the draw callback function to the drawing area
    g_signal_connect(G_OBJECT(drawing_area), "draw", G_CALLBACK(draw_callback), NULL);

    // Connect the destroy signal for the window
    g_signal_connect(G_OBJECT(window), "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Show all widgets
    gtk_widget_show_all(window);

    // Run the GTK main loop
    gtk_main();

    return 0;
}
