import unittest

class TestServiceRegistration(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    def test_find_files(self):
        self.assertEqual(find_files(), [])
    def test_ensure_data_structure_unchanged(self):
        # filename, archive_dir, incoming_dir):
        pass
    def test_find_existing_resource_id(self):
        # filename):
        pass
    def test_archive_file(self):
        # filename):
        pass
    def test_existing_resources(self):
        pass
    def test_update_existing_resource(self):
        # filename, resource_id):
        pass
    def test_create_new_resource(self):
        # filename):
        pass
    def test_delete_all_existing_resources(self):
        pass
    def test_file_to_publish(self):
        # filename):
        pass


if __name__ == '__main__':
    unittest.main()