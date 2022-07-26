import pytest
import pathlib
import fetching_data_pdb as fdp
import config


class TestFetchingDataPDB:
    @pytest.fixture(autouse=True)
    def _path(self):
        self._path = {
            "pdb_files": "pdb_files_test",
            "register": "register_test",
        }

    @pytest.fixture(autouse=True)
    def _pdb_codes(self):
        self._codes = ['119l', '153l']

    def test_listing_codes(self):
        config.init_config(config_file='pdb_parser_test.toml')
        assert fdp.listing_codes(list_of_codes='test_pdb_codes.txt', paths=self._path,
                                 error_file='test_errors.txt') == self._codes

    def test_get_pdb_files(self):
        fdp.get_pdb_files(pdb_codes=self._codes, paths=self._path, error_file='test_errors.txt')

        pdb_files = pathlib.Path(__file__).parent
        pdb_files = pdb_files.joinpath(self._path['pdb_files'])

        for code in self._codes:
            assert (pdb_files.joinpath(f'{code}.pdb')).is_file()
