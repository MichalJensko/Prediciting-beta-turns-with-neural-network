import fetching_data_pdb as fd
import config
import data_extraction_from_pdb as extraction


def main():
    paths = config.init_config()
    fd.get_pdb_files(fd.listing_codes('pdb_codes.txt', paths), paths)
    extraction.list_pdb_files(paths)


if __name__ == '__main__':
    main()
