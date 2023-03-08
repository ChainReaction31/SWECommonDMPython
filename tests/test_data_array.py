import json


def test_data_array(test_comp_data_array):
    d_arr = test_comp_data_array
    arr_json = d_arr.datastructure_to_dict()
    doodad = d_arr.get_value()
    print(json.dumps(arr_json))


    assert True
