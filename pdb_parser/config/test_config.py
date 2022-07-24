import pytest
import config
import pathlib


class TestConfig:

    @pytest.fixture(autouse=True)
    def _path(self):
        self._path = {
            "pdb_files": "pdb_files",
            "register": "register",
                      }

    def test_parse_config(self):
        assert config.parse_config() == self._path

    def test_create_workspace_directories(self):
        path = pathlib.Path(__file__).parents[1]
        config.create_workspace_directories(self._path)

        for key in self._path.keys():
            directory = path.joinpath(self._path[key])
            assert directory.is_dir()
            directory.rmdir()



