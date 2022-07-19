import tomli
import pathlib


def parse_config():

    paths = {}
    path = pathlib.Path(__file__).parent
    path = path.joinpath("pdb_parser.toml")

    with path.open(mode="rb") as c_file:
        config = tomli.load(c_file)

    for key in config['paths'].keys():
        paths[key] = config['paths'][key]

    return paths


def create_workspace_directories(config_paths):
    path = pathlib.Path(__file__).parents[1]

    for key in config_paths.keys():
        directory = path.joinpath(config_paths[key])
        directory.mkdir(parents=False, exist_ok=True)


def init_config():
    paths = parse_config()
    create_workspace_directories(paths)
    return paths
