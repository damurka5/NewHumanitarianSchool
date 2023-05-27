import pandas as pd
import matplotlib.pyplot as plt

def draw_plot(path):
    # Чтение данных из файла CSV
    data = pd.read_csv(path, header=None)

    # Преобразование данных в список
    data_list = data[0].tolist()

    # Создание графика
    fig, ax = plt.subplots()
    ax.plot(data_list)

    # Отображение графика
    plt.show()

draw_plot('/Users/daniiltesluk/PycharmProjects/NewHumanitarianSchool/quizes/quiz on may 27/data.csv')
draw_plot('/Users/daniiltesluk/PycharmProjects/NewHumanitarianSchool/quizes/quiz on may 27/data2.csv')