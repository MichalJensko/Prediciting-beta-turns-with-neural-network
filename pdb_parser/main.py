import fetching_data_pdb as fd
import initialize_config


def main():
    paths = initialize_config.init_config()
    fd.get_pdb_files(fd.listing_codes('./pdb_codes.txt'), paths['pdb_files'])


if __name__ == '__main__':
    main()
