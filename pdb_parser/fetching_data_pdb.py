import requests
import pathlib


def listing_codes(list_of_codes, paths, error_file='register.txt'):

    pdb_codes = []
    errors = pathlib.Path(__file__).parent
    errors = errors.joinpath(errors, paths['register'], error_file)

    with open(list_of_codes, 'r') as listing:

        for line in listing:
            line = line.strip('\n')

            if len(line) > 4:

                with errors.open(mode="x") as err:
                    err.write(f'{line}: exceeds standard length for pdb code')

                continue
            else:
                pdb_codes.append(line)
    print(pdb_codes)
    return pdb_codes


def get_pdb_files(pdb_codes, paths, error_file='register.txt'):

    errors = pathlib.Path(__file__).parent
    errors = errors.joinpath(errors, paths['register'], error_file)
    pdb_files = pathlib.Path(__file__).parent
    pdb_files = pdb_files.joinpath(paths['pdb_files'])

    for code in pdb_codes:
        request = requests.get(f'https://files.rcsb.org/download/{code}.pdb')

        if request.status_code == 200:

            open(pdb_files.joinpath(f'{code}.pdb'), 'wb').write(request.content)
        else:
            with errors.open(mode='a') as err:
                err.write(f'{code}: could not be fetched from pdb database. Status code: {request.status_code}')
