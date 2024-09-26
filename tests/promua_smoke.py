import pytest

class TestPromUaSmokePytest:
    search_data = ["18650", "21700"]

    @pytest.mark.parametrize("search_value", search_data)
    def test_smoke_search_verification(self, get_objects, search_value):
        get_objects.main_page.verify_default_main_page()
        get_objects.general_search.simple_search(search_value)
        list_of_plates = get_objects.general_search.get_product_plates()
        get_objects.base_functionality.verify_true(len(list_of_plates)>0, "list plates are empty")
        for this_plate in list_of_plates:
            product_description = get_objects.general_search.get_product_description(this_plate)
            print("product description: " + product_description)
            get_objects.base_functionality.verify_true(search_value in product_description,
                                                       "product description is not contains " + search_value)