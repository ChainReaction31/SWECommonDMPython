import json


def test_vector_json(test_comp_vector):
    vec = test_comp_vector
    vec_json = vec.datastructure_to_dict()
    print(f'\n{json.dumps(vec_json)}')
    assert True
