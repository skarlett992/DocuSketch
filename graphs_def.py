import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib import *
from pylab import *
import seaborn as sns

def predicted_results(data):
    x = data.gt_corners
    y = data.rb_corners
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y)
    plt.title('Find out errors in our prediction model')
    plt.xlabel('gt_corners values')
    plt.ylabel('rb_corners values')
    if not os.path.isdir('plots'):
        os.makedirs('plots')
    fig.savefig('plots/model_predictions.png')

def count_and_types_rooms(data, name_y_true_col):
    vals = data[name_y_true_col].value_counts().tolist()
    labels = data[name_y_true_col].value_counts().index.tolist()
    explode = (0, 0.2, 0.3, 1.2)
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=explode)
    ax.axis("equal")
    if not os.path.isdir('plots/room_types'):
        os.makedirs('plots/room_types')
    fig.savefig('plots/room_types/count_and_types_rooms.png')
    print("The model predicted values in gt_corners. Let's look at their types\n\
    Also we can see, we have only 4 corner types, and rooms: 4, 6, 8 and 10. "
          "Besides, common type is 4-corners rooms.\
    Room with 10 corners only one, so we can use separatly "
          "description for it without graphs:")
    print(f'type of corner room and count items for this: \n{data[name_y_true_col].value_counts()}')

def distribution_and_deviations(data):
    print('So, graphs show to us that the values don t have normal distribution. \
    Also, we have many noise, because a lot of items unusual design - '
          'from 25 to more than 200 degree of deviations\
    Most min values, including floor and ceiling, have approximately '
          'deviations from 0 to 10 degree.\
    Majority of mean values - from 0 to 20\
    And common of max values - from 0 to 50.\
    If we try to exclude noises, we ll find out more exactly values.')
    f = figure(figsize=(20, 5))
    sns.distplot(data['min'])
    sns.distplot(data['floor_min'])
    sns.distplot(data['ceiling_min'])
    plt.title('Comparing min, floor_min and ceiling_min deviations')
    plt.xlabel('deviations values')
    plt.ylabel('density values')
    plt.legend([
        'min deviations',
        'floor_min deviations',
        'ceiling_min deviations'
    ])
    plt.show()
    if not os.path.isdir('plots/distribution_and_deviations'):
        os.makedirs('plots/distribution_and_deviations')
    f.savefig('plots/distribution_and_deviations/min.png', dpi=300)


    f = figure(figsize=(20, 5))
    sns.distplot(data['mean'])
    sns.distplot(data['floor_mean'])
    sns.distplot(data['ceiling_mean'])
    plt.title('Comparing mean, floor_mean and ceiling_mean deviations')
    plt.xlabel('deviations values')
    plt.ylabel('density values')
    plt.legend([
        'mean deviations',
        'floor_mean deviations',
        'ceiling_mean deviations'
    ])
    plt.show()
    f.savefig('plots/distribution_and_deviations/mean.png')


    f = figure(figsize=(20, 5))
    sns.distplot(data['max'])
    sns.distplot(data['floor_max'])
    sns.distplot(data['ceiling_max'])
    plt.title('Comparing max, floor_max and ceiling_max deviations')
    plt.xlabel('deviations values')
    plt.ylabel('density values')
    plt.legend([
        'max deviations',
        'floor_max deviations',
        'ceiling_max deviations'
    ])
    f.savefig('plots/distribution_and_deviations/max.png')

def boxplot_with_noises(data):
    print('Let s try boxes: that graphs have clearlier explanation.\
    You can find out description how they works follow this link:\
    https://matplotlib.org/stable/_images/boxplot_explanation.png. \
    Common mean and floor_mean deviations have +/- equall values of degree, \
          instead of ceiling_mean devitions. \
          We have similar picture of the min and max values.\
          But there is a lot of noise in the data. ')
    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['mean'])
    plt.title('Comparing common mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'mean deviations'
                ])
    plt.show()
    if not os.path.isdir('plots/boxplots_with_noises'):
        os.makedirs('plots/boxplots_with_noises')
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_mean.png')



    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['floor_mean'])
    plt.title('Comparing floor_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'floor_mean deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_floor_mean.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['ceiling_mean'])
    plt.title('Comparing ceiling_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'ceiling_mean deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_ceiling_mean.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['max'])
    plt.title('Comparing common mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'max deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_max.png')

    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['floor_max'])
    plt.title('Comparing floor_max deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'floor_max deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_floor_max.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['ceiling_max'])
    plt.title('Comparing ceiling_max deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'ceiling_max deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_ceiling_max.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['min'])
    plt.title('Comparing common min deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'min deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_min.png')



    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['floor_min'])
    plt.title('Comparing floor_min deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'floor_min deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_floor_min.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data['gt_corners'], y=data['ceiling_min'])
    plt.title('Comparing ceiling_min deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'ceiling_min deviations'
                ])
    plt.show()
    f.savefig('plots/boxplots_with_noises/boxplot_with_noises_ceiling_min.png')


def boxplot_common_deviations_without_noises(data):
    print('We removed noise and left the most common values.')
    print('At first, we show common derivation: min, mean and max')
    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners']!=10]['gt_corners'], y=data[data['min']<0.6]['min'])
    plt.title('Comparing common mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'min deviations'
                ])
    plt.show()
    if not os.path.isdir('plots/boxplot_without_noises'):
        os.makedirs('plots/boxplot_without_noises')
    f.savefig('plots/boxplot_without_noises/boxplot_without_noises_min.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners']!=10]['gt_corners'], y=data[data['mean']<4.5]['mean'])
    plt.title('Comparing common mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'mean deviations'
                ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_without_noises_mean.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners']!=10]['gt_corners'], y=data[data['max']<40]['max'])
    plt.title('Comparing common mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
                'max deviations'
                ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_without_noises_max.png')


    corners = data.gt_corners.value_counts().index.tolist()

    for corner in corners[:-1]:
        common_min = data[data['gt_corners']==corner][data['min']<0.6]['min']
        common_mean = data[data['gt_corners']==corner][data['mean']<4.5]['mean']
        common_max = data[data['gt_corners']==corner][data['max']<40]['max']

        print(f"common deviations: for {round(corner)}-corners:\n\
        from {round(common_min.min(), 2)}\
        to {round(common_min.max(), 2)},\
        with majority of them is approximately {round(common_min.mean(), 2)} degree for MIN;\n\
        from {round(common_mean.min(), 2)}\
        to {round(common_mean.max(), 2)},\
        with majority of them is approximately {round(common_mean.mean(), 2)} degree for MEAN;\n\
        from {round(common_max.min(), 2)}\
        to {round(common_max.max(), 2)},\
        with majority of them is approximately {round(common_max.mean(), 2)} degree for MAX;")


def boxplot_floor_deviations_without_noises(data):
    print('Secondly, we show floor derivation: floor_min, floor_mean and floor_max')
    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['floor_min'] < 0.6]['floor_min'])
    plt.title('Comparing common floor_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'floor_min deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_floor_deviations_without_noises_min.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['floor_mean'] < 4.5]['floor_mean'])
    plt.title('Comparing common floor_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'floor_mean deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_floor_deviations_without_noises_mean.png')

    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['floor_max'] < 40]['floor_max'])
    plt.title('Comparing common floor_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'floor_max deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_floor_deviations_without_noises_max.png')

    corners = data.gt_corners.value_counts().index.tolist()

    for corner in corners[:-1]:
        floor_min = data[data['gt_corners'] == corner][data['floor_min'] < 0.6]['floor_min']
        floor_mean = data[data['gt_corners'] == corner][data['floor_mean'] < 4.5]['floor_mean']
        floor_max = data[data['gt_corners'] == corner][data['floor_max'] < 40]['floor_max']

        print(f"floor deviations: for {round(corner)}-corners:\n\
        from {round(floor_min.min(), 2)}\
        to {round(floor_min.max(), 2)},\
        with majority of them is approximately {round(floor_min.mean(), 2)} degree for floor_MIN;\n\
        from {round(floor_mean.min(), 2)}\
        to {round(floor_mean.max(), 2)},\
        with majority of them is approximately {round(floor_mean.mean(), 2)} degree for floor_MEAN;\n\
        from {round(floor_max.min(), 2)}\
        to {round(floor_max.max(), 2)},\
        with majority of them is approximately {round(floor_max.mean(), 2)} degree for floor_MAX;")


def boxplot_ceiling_deviations_without_noises(data):
    print('And trird, we show ceiling derivation, wich quite different from another types of derivations\
    : ceiling_min, ceiling_mean and ceiling_max')
    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['ceiling_min'] < 1]['ceiling_min'])
    plt.title('Comparing common ceiling_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'ceiling_min deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_ceiling_deviations_without_noises_min.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['ceiling_mean'] < 6]['ceiling_mean'])
    plt.title('Comparing common ceiling_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'ceiling_mean deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_ceiling_deviations_without_noises_mean.png')


    f = plt.figure(figsize=(27, 7))
    sns.boxplot(x=data[data['gt_corners'] != 10]['gt_corners'], y=data[data['ceiling_max'] < 30]['ceiling_max'])
    plt.title('Comparing common ceiling_mean deviations from rooms')
    plt.xlabel('4 classes of corners% 4 corners, 6 corners, 8 corners and 10 coners')
    plt.ylabel('deviations values')
    plt.legend([
        'ceiling_max deviations'
    ])
    plt.show()
    f.savefig('plots/boxplot_without_noises/boxplot_ceiling_deviations_without_noises_max.png')

    corners = data.gt_corners.value_counts().index.tolist()

    for corner in corners[:-1]:
        ceiling_min = data[data['gt_corners'] == corner][data['ceiling_min'] < 1]['ceiling_min']
        ceiling_mean = data[data['gt_corners'] == corner][data['ceiling_mean'] < 6]['ceiling_mean']
        ceiling_max = data[data['gt_corners'] == corner][data['ceiling_max'] < 30]['ceiling_max']

        print(f"ceiling deviations: for {round(corner)}-corners:\n\
        from {round(ceiling_min.min(), 2)}\
        to {round(ceiling_min.max(), 2)},\
        with majority of them is approximately {round(ceiling_min.mean(), 2)} degree for ceiling_MIN;\n\
        from {round(ceiling_mean.min(), 2)}\
        to {round(ceiling_mean.max(), 2)},\
        with majority of them is approximately {round(ceiling_mean.mean(), 2)} degree for ceiling_MEAN;\n\
        from {round(ceiling_max.min(), 2)}\
        to {round(ceiling_max.max(), 2)},\
        with majority of them is approximately {round(ceiling_max.mean(), 2)} degree for ceiling_MAX")

