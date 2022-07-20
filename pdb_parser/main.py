import fetching_data_pdb as fd
import config


def main():
    paths = config.init_config()
    fd.get_pdb_files(fd.listing_codes('pdb_codes.txt', paths), paths)


if __name__ == '__main__':
    main()
