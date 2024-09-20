import tkinter as tk
import extract as ext
import helper_funcs as hf

path_name = "variables"
file_list = ext.get_filenames(path_name)
curr_file_location = 0
curr_file = file_list[curr_file_location]
var_list = hf.get_variable_list(curr_file)
curr_var_location = 0
curr_var = var_list[curr_var_location]
variable_size = hf.get_variable_size(curr_file) -1

window = tk.Tk()
window.geometry("500x600")
# create top frame for buttons
top_frame = tk.Frame(window)
bottom_frame = tk.Frame(window)
top_frame.pack(side="top", anchor="ne")
bottom_frame.pack(side="bottom", anchor="se", fill= "both", expand= True)

def previous_variable():
    global var_list
    global curr_var_location
    global curr_var
    if curr_var_location > 0:
        curr_var_location -= 1
        curr_var = var_list[curr_var_location]
    pre_var = "with the %d variable in %d variables" %(curr_var_location, variable_size)
    var_name["text"] = pre_var
    remove_reconfig()
    
def next_variable():
    global var_list
    global curr_var_location
    global curr_var
    global variable_size
    if curr_var_location < variable_size:
        curr_var_location += 1
        curr_var = var_list[curr_var_location]
    next_var = "with the %d variable in %d variables" %(curr_var_location, variable_size)
    var_name["text"] = next_var
    remove_reconfig()

attribute = tk.IntVar()

second = tk.IntVar()

const_attr = tk.IntVar()


def submit_variable():
    global curr_file
    global curr_var

    global attribute
    global second
    global const_attr
    local_attr = ""
    detail = ""
    if attribute.get() == 0:
        remove_reconfig()
        return
    elif attribute.get() == 1:
        if const_attr.get() != 0:
            remove_reconfig()
            return
        else:
            local_attr = "variable"
    elif attribute.get() == 2:
        if second.get() != 0:
            remove_reconfig()
            return
        else:
            local_attr = "constant"
    elif attribute.get() == 3:
        if second.get() != 0 or const_attr.get() != 0:
            remove_reconfig()
            return
        else:
            local_attr = "operator"
    elif attribute.get() == 4:
        if second.get() != 0 or const_attr.get() != 0:
            remove_reconfig()
            return
        else:
            local_attr = "unit descriptor"

    if (second.get() != 0 and const_attr.get() != 0):
        remove_reconfig()
        return
    elif (second.get() != 0):
        if second.get() == 1:
            detail = "Scalar"
        elif second.get() == 2:
            detail = "Vector"
        elif second.get() == 3:
            detail = "Matrix"
    elif (const_attr.get() != 0):
        if const_attr.get() == 1:
            detail = "Local"
        elif const_attr.get() == 2:
            detail = "Global"
        elif const_attr.get() == 3:
            detail = "Discipline specified"

    combine = "\n" + curr_file + " " + str(curr_var_location) + " " + hf.remove_n(curr_var) + " " + local_attr  + " " + detail
    print(combine)
        
    with open("test_database", "ab") as in_file:
        in_file.write(combine.encode('utf8'))

    remove_reconfig()
    next_variable()


def remove_reconfig():
    global attribute
    global second
    global const_attr
    # part to remove the selection and reconfig the sentence
    attribute.set("0")
    second.set("0")
    const_attr.set("0")

    selection = "the selected symbol is a " + str(attribute.get())
    test_out.config(text=selection)

    sub = "the selected variable is a " + str(second.get())
    sub_out.config(text=sub)

    con = "the selected constant is a " + str(const_attr.get())
    const_out.config(text=con)


def next_file():
    global file_list
    global curr_file_location
    global curr_file
    global var_list
    global curr_var_location
    global variable_size

    if curr_file_location <= len(file_list):
        curr_file_location += 1
        curr_file = file_list[curr_file_location]

    # update all variables
    var_list = hf.get_variable_list(curr_file)
    curr_var_location = 0
    variable_size = hf.get_variable_size(curr_file)

    next_file = "Now your are in file:  " + curr_file
    file_name["text"] = next_file

    new_var = "with the %d variable in %d variables" %(curr_var_location, variable_size)
    var_name["text"] = new_var
    remove_reconfig()

# GUI for top part
prev_button = tk.Button(top_frame, text = "prev", width=10, height=2, command=previous_variable)
next_button = tk.Button(top_frame, text = "next", width=10, height=2, command=next_variable)
next_file_button = tk.Button(top_frame, text= "Next file", width=10, height=2, command=next_file)

next_button.pack(side= "right")
prev_button.pack(side= "right")
next_file_button.pack(in_= top_frame, side= "left")


# GUI for bottom part
quit_button = tk.Button(window, text="Quit", width=10, height=2, command=window.destroy)
submit_button = tk.Button(window, text="Submit", width=10, height=2, command=submit_variable)
reset_button = tk.Button(window, text="Reset",width=10, height=2, command=remove_reconfig)
quit_button.pack(in_= bottom_frame, side="right", anchor="se")
submit_button.pack(in_=bottom_frame, side="right", anchor="se")
reset_button.pack(in_=bottom_frame, side="right", anchor="se")


# label frame for information related to the variable
labelFrame = tk.LabelFrame(window, text="Information related to variable")
labelFrame.pack(fill="both")
# logics need to be added 

file_name = tk.Label(labelFrame, text="Now your are in file:  " + curr_file)
file_name.grid(row=1,column=1)
var_name = tk.Label(labelFrame, text="with the %d variable in %d variables" %(curr_var_location, variable_size))
var_name.grid(row=2,column=1)
content_location = tk.Label(labelFrame, text="The content of this variable is: ").grid(row=3,column=1)



def get_attribute():
    selection = "the selected symbol is a " + str(attribute.get())
    test_out.config(text=selection)

def get_subclass():
    sub = "the selected variable is a " + str(second.get())
    sub_out.config(text=sub)

def get_constdefine():
    con = "the selected constant is a " + str(const_attr.get())
    const_out.config(text=con)

# label frame for the classification of variables
variableFrame = tk.LabelFrame(window, text="Variable classification")
variableFrame.pack(fill="both")
test_out = tk.Label(variableFrame, text="the selected symbol is a ")
test_out.grid(row=1, column=1)
# change the value later for the data base recognition
var = tk.Radiobutton(variableFrame, text="variable", variable=attribute, value=1, command=get_attribute)
var.grid(row=2, column=1)
const = tk.Radiobutton(variableFrame, text="constant", variable=attribute, value=2, command=get_attribute)
const.grid(row=3, column=1)
op = tk.Radiobutton(variableFrame, text="operator", variable=attribute, value="3", command=get_attribute)
op.grid(row=4, column=1)
unit = tk.Radiobutton(variableFrame, text="unit descriptor", variable=attribute, value="4", command=get_attribute)
unit.grid(row=5, column=1)

subFrame = tk.LabelFrame(window, text="If this symbol is a variable, what is its attribute?")
subFrame.pack(fill="both")

sub_out = tk.Label(subFrame, text="the selected variable is a ") 
sub_out.grid(row=1, column=1)
variable_scalar = tk.Radiobutton(subFrame, text="Scalar", variable=second, value=1, command=get_subclass)
variable_scalar.grid(row=2, column=1)
variable_Vector = tk.Radiobutton(subFrame, text="Vector", variable=second, value=2, command=get_subclass)
variable_Vector.grid(row=3, column=1)
variable_Matrix = tk.Radiobutton(subFrame, text="Matrix", variable=second, value=3, command=get_subclass)
variable_Matrix.grid(row=4, column=1)

constFrame = tk.LabelFrame(window, text="If this symbol is a constant or operator, what is its attribute?")
constFrame.pack(fill="both")

const_out = tk.Label(constFrame, text="the selected constant is a ")
const_out.grid(row=1, column=1)
const_local = tk.Radiobutton(constFrame, text="Local", variable=const_attr, value=1, command=get_constdefine)
const_local.grid(row=2, column=1)
const_global = tk.Radiobutton(constFrame, text="Global", variable=const_attr, value=2, command=get_constdefine)
const_global.grid(row=3, column=1)
const_dis = tk.Radiobutton(constFrame, text="Discipline-specified", variable=const_attr, value=3, command=get_constdefine)
const_dis.grid(row=4, column=1)

# keyboard operations on traverse variables
window.bind('r', lambda event:remove_reconfig())
window.bind('s', lambda event:submit_variable())
window.bind ('<Left>', lambda event: previous_variable())
window.bind('<Right>', lambda event: next_variable())
window.bind('<Down>', lambda event: next_file())
window.bind('<Escape>', lambda event: window.destroy())
window.bind('q', lambda event: window.destroy())

# keyboard operations on assign variables
def var_21():
    attribute.set(1)
    get_attribute()
def var_22():
    attribute.set(2)
    get_attribute()
def var_23():
    attribute.set(3)
    get_attribute()
def var_24():
    attribute.set(4)
    get_attribute()
window.bind('1', lambda event:var_21())
window.bind('2', lambda event:var_22())
window.bind('3', lambda event:var_23())
window.bind('-', lambda event:var_24())

# keyboard operation on assign constants
def var_scalar():
    second.set(1)
    get_subclass()

def var_vector():
    second.set(2)
    get_subclass()

def var_matrix():
    second.set(3)
    get_subclass()

window.bind('4', lambda event: var_scalar())
window.bind('5', lambda event: var_vector())
window.bind('6', lambda event: var_matrix())


# keyboard operation to set constant values
def con_local():
    const_attr.set(1)
    get_constdefine()

def con_global():
    const_attr.set(2)
    get_constdefine()

def con_ds():
    const_attr.set(3)
    get_constdefine()

window.bind('7', lambda event: con_local())
window.bind('8', lambda event: con_global())
window.bind('9', lambda event: con_ds())


window.mainloop()