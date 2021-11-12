
from graphs_def import predicted_results, count_and_types_rooms, \
    distribution_and_deviations, boxplot_ceiling_deviations_without_noises, \
    boxplot_common_deviations_without_noises, boxplot_floor_deviations_without_noises,\
    boxplot_with_noises


class all_plots():
    def __init__(self, data):
        self.data = data

    def draw_plots(self):
        predicted_results(self.data)

    def draw_target_types(self, name_y_true_col):
        count_and_types_rooms(self.data, name_y_true_col)

    def draw_distributions(self):
        distribution_and_deviations(self.data)

    def draw_boxes(self):
        boxplot_with_noises(self.data)
        boxplot_common_deviations_without_noises(self.data)
        boxplot_floor_deviations_without_noises(self.data)
        boxplot_ceiling_deviations_without_noises(self.data)


