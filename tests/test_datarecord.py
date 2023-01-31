def test_add_field(test_comp_datarecord, test_time_comp, test_quantity_comp):
    test_comp_datarecord.add_field(test_time_comp)
    test_comp_datarecord.add_field(test_quantity_comp)
    assert test_comp_datarecord.fields.__contains__(test_time_comp)
    assert test_comp_datarecord.fields.__contains__(test_quantity_comp)


def test_get_num_fields(test_comp_datarecord, test_time_comp, test_quantity_comp):
    test_comp_datarecord.add_field(test_time_comp)
    test_comp_datarecord.add_field(test_quantity_comp)
    assert test_comp_datarecord.get_num_fields() == 2


def test_flat_field_map(test_comp_datarecord, test_time_comp, test_quantity_comp):
    test_comp_datarecord.add_field(test_time_comp)
    test_comp_datarecord.add_field(test_quantity_comp)
    field_map = test_comp_datarecord.flat_id_to_field_map()
    assert field_map.keys().__contains__(test_time_comp.get_uuid())
    assert field_map.keys().__contains__(test_quantity_comp.get_uuid())
