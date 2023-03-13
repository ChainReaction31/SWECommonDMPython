import json


def test_data_array(test_comp_data_array):
    d_arr = test_comp_data_array
    arr_json = d_arr.datastructure_to_dict()
    doodad = d_arr.get_value()
    print(json.dumps(arr_json))

    assert True


def test_darr_add_vals(test_comp_data_array):
    d_arr = test_comp_data_array
    values = [1, 2, 3]
    d_arr.set_value(values)
    print(d_arr.get_value())


def test_da_nested_1(test_nested_comp_data_array_1):
    d_arr = test_nested_comp_data_array_1
    values = [{'f1': 'A', 'f2': 1}, {'f1': 'B', 'f2': 2}]
    d_arr.set_value(values)
    print(d_arr.get_value())


def test_da_nested_2(test_nested_comp_data_array_2):
    d_arr = test_nested_comp_data_array_2
    values = [{'Lat': 0.0, 'Lon': 0.0, 'Alt': 0.0}, {'Lat': 34.74, 'Lon': -86.60, 'Alt': 190}]
    d_arr.set_value(values)
    print(d_arr.get_value())


def test_da_nested_3(test_nested_comp_data_array_3):
    d_arr = test_nested_comp_data_array_3
    values = []
    for i in range(1920):
        inner_values = []
        for j in range(1080):
            inner_values.append(j)
        values.append(inner_values)

    d_arr.set_value(values)
    print(d_arr.get_value())
