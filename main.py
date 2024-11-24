from tkinter import END, RAISED, DISABLED
from stats_cal import Stats
import tkinter


window = tkinter.Tk()
window.geometry("700x680")
# window.resizable(0, 0)
window.title("Statistics")

text_label = tkinter.Label(window, text="Data:", font=("Arial", 20, "normal"))
text_label.place(x = 9, y = 50)

text_area = tkinter.Text(window, width=45, height=5, font=("Arial", 20, "normal"), borderwidth=3, relief=RAISED)
text_area.focus()
text_area.place(x = 110, y = 10)


def data_list():
    symbols = [" ", "\n"]
    new_list = []
    data = []
    for i in text_area.get("1.0", "end-1c"):
        if i not in symbols:
            new_list.append(i)
    element = ""
    for j in new_list:
        if j != ",":
            element += j
        else:
            data.append(float(element))
            element = ""
    data.append(float(element))
    return data


def show():
    mean_entry.delete(0, "end")
    median_entry.delete(0, "end")
    mode_entry.delete(0, "end")
    maximum_entry.delete(0, "end")
    minimum_entry.delete(0, "end")
    range_entry.delete(0, "end")
    q1_entry.delete(0, "end")
    q3_entry.delete(0, "end")
    iqr_entry.delete(0, "end")

    data = data_list()
    statistics = Stats(data)
    statistics.calculate()
    modal_list = statistics.mode
    modal_value = ", ".join(modal_list)
    arranged_data_list = statistics.arr
    arranged_data_list = [str(i) for i in arranged_data_list]
    arranged_data_array = ", ".join(arranged_data_list)
    arranged_data_entry.insert("1.0", arranged_data_array)
    mean_entry.insert(0, statistics.mean)
    median_entry.insert(0, statistics.median)
    mode_entry.insert(0, modal_value)
    maximum_entry.insert(0, statistics.maximum)
    minimum_entry.insert(0, statistics.minimum)
    range_entry.insert(0, statistics.rangevalue)
    q1_entry.insert(0, statistics.q1)
    q3_entry.insert(0, statistics.q3)
    iqr_entry.insert(0, statistics.iqr)
    frequency_entry.insert(0, statistics.frequency)


def clear():
    text_area.delete("1.0", END)


Calculate = tkinter.Button(window, text="Calculate", font=("", 20, "normal"), borderwidth=5, relief=RAISED,
                           command=show)
Calculate.place(x=250, y=150)

Clear = tkinter.Button(window, text="Clear", font=("", 20, "normal"), borderwidth=5, relief=RAISED, command=clear)
Clear.place(x=410, y=150)

arranged_data_label = tkinter.Label(window, text = "Arranged\nData:", font = ("Arial", 20, "normal"))
arranged_data_label.place(x = 8, y = 250)

arranged_data_entry = tkinter.Text(window, width=45, height=5, font=("Arial", 20, "normal"), borderwidth= 3, relief= RAISED)
arranged_data_entry.place(x = 110, y = 200)

mean_label = tkinter.Label(window, text="Mean:", font=("Arial", 20, "normal"))
mean_label.place(x=8, y=340)

mean_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
mean_entry.place(x=150, y=335)

median_label = tkinter.Label(window, text="Median:", font=("Arial", 20, "normal"))
median_label.place(x=8, y=410)

median_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
median_entry.place(x=150, y=405)

mode_label = tkinter.Label(window, text="Mode:", font=("Arial", 20, "normal"))
mode_label.place(x=8, y=480)

mode_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
mode_entry.place(x=150, y=475)

maximum_label = tkinter.Label(window, text="Maximum:", font=("Arial", 20, "normal"))
maximum_label.place(x=8, y=550)

maximum_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
maximum_entry.place(x=150, y=545)

minimum_label = tkinter.Label(window, text="Minimum:", font=("Arial", 20, "normal"))
minimum_label.place(x=8, y=620)

minimum_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
minimum_entry.place(x=150, y=615)

range_label = tkinter.Label(window, text="Range:", font=("Arial", 20, "normal"))
range_label.place(x=320, y=340)

range_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
range_entry.place(x=462, y=335)

q1_label = tkinter.Label(window, text="Q1:", font=("Arial", 20, "normal"))
q1_label.place(x=320, y=410)

q1_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
q1_entry.place(x=462, y=405)

q3_label = tkinter.Label(window, text="Q3:", font=("Arial", 20, "normal"))
q3_label.place(x=320, y=480)

q3_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
q3_entry.place(x=462, y=475)

iqr_label = tkinter.Label(window, text="IQR:", font=("Arial", 20, "normal"))
iqr_label.place(x=320, y=550)

iqr_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
iqr_entry.place(x=462, y=545)

frequency_label = tkinter.Label(window, text="Frequency:", font=("Arial", 20, "normal"))
frequency_label.place(x=320, y=620)

frequency_entry = tkinter.Entry(window, font=("Arial", 20, "normal"), width=10)
frequency_entry.place(x=462, y=615)

window.mainloop()