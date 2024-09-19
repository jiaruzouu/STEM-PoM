import math

def get_unique_categories(database):
    unique_categories = []
    with open(database, "rb") as in_file:
        for lines in in_file:
            category = lines[0:13].decode('utf8')
            if category not in unique_categories:
                unique_categories.append(category)
    return unique_categories[1:]

def get_all_categories(database):
    all_categories = []
    with open(database, "rb") as in_file:
        for lines in in_file:
            category = lines[0:26].decode('utf8')
            if category not in all_categories:
                all_categories.append(category)
    return all_categories[1:]

# there must be a better way to do this, but this is enough for now
def variable_numdic(database):
    variables_in_papers = dict()
    all_categories = get_all_categories(database)
    with open(database, "rb") as in_file:
        first = 0
        for lines in in_file:
            for categories in all_categories:
                if categories == lines[0:26].decode('utf8'):
                    first = first + 1
                    variables_in_papers[categories] = first

    idx = 0
    cal_table = [None] * len(all_categories)
    for values in variables_in_papers.values():
        cal_table[idx] = values
        idx += 1
    idx = 0
    for categories in all_categories:
        if idx == 0:
            variables_in_papers[categories] = cal_table[idx]
        else:
            variables_in_papers[categories] = cal_table[idx] - cal_table[idx - 1]
        idx += 1
        
    return variables_in_papers

def category_numdic(database):
    variables_in_category = dict()
    categories = get_unique_categories(database)
    all_variables = variable_numdic(database)
    for category in categories:
        number = 0
        for key in all_variables.keys():
            if category == key[0:13]:
                number += all_variables[key]
        variables_in_category[category] = number
    return variables_in_category

def average_variable(variables_dic):
    average_variable_num = 0
    for var_num in variables_dic.values():
        average_variable_num += var_num
    average_variable_num /= len(variables_dic)
    # print(math.ceil(average_variable_num))
    return math.ceil(average_variable_num)



unique = get_unique_categories("test_database")
# met a problem of inaccurate numbers since we skipped some non-variable symbols
# solved in a non-elegant way, might be improved later
all_ = get_all_categories("test_database")
category_dic = category_numdic("test_database")
paper_dic = variable_numdic("test_database")
average = average_variable(paper_dic)


# the category need to -1 becasue we have the heading line
print("There are " + str(len(unique)) + " unique categories")
print("There are " + str(len(all_)) + " articles in total")
print("In average, each article contains " + str(average) + " variables")
print("If u want to see more details about this dataset, please visit the database")


# add those statistics into the database
def add_statistic(database):
    with open(database, "ab") as in_file:
        unique = get_unique_categories("test_database")
        all_ = get_all_categories("test_database")
        category_dic = category_numdic("test_database")
        paper_dic = variable_numdic("test_database")
        category = "\n \nUnique Categories " + str(unique)
        in_file.write(category.encode('utf8'))
        ca_dic = "\nNumber of variables each category contains " + str(category_dic) + "\n"
        in_file.write(ca_dic.encode('utf8'))
        every = "\nAll articles " + str(all_)
        in_file.write(every.encode('utf8'))
        paper = "\nNumber of variables each article contains " + str(paper_dic)
        in_file.write(paper.encode('utf8'))

add_statistic("test_database")
