import pathlib
import CONSTANT


def list_pdb_files(paths):
    """
    Function listing all the paths to pdb files present in given directory.

    :param paths: dict, Name of folder containing pdb files hidden under pdb_files key

    :return: list paths to all pdb files in given dictionary
    """
    pdb_files = []
    pdb_files_directory = pathlib.Path(__file__).parent
    pdb_files_directory = pdb_files_directory.joinpath(paths['pdb_files'])

    # Loop for creating list of paths to pdb files
    for file in pdb_files_directory.iterdir():
        if str(file).endswith('.pdb'):
            pdb_file = str(pdb_files_directory.joinpath(file))
            pdb_files.append(pdb_file.lstrip('PosixPath'))

    return pdb_files


def code_3_to_1(sequence_3):
    """
    Function translating sequence of 3-letter amino acid codes into a sequence of 1-letter codes.

    :param sequence_3: str, Sequence of amino acids written using 3-letter codes

    :return: str, returns the same amino acid sequence translated to 1-letter codes

    :raises: ValueError, when length of sequence can't be divided by 3 without a reminder
    """
    sequence_1 = ''

    if len(sequence_3) % 3 != 0:
        raise ValueError('Provided sequence can\'t be divided by 3 without a reminder. Please check your sequence')

    for j in range(0, len(sequence_3), 3):
        aa_code = sequence_3[j:j + 3]
        code = ''
        for i in range(len(aa_code) // 3):
            code += CONSTANT.AA_KEY[aa_code[3 * i: 3 * i + 3]]
        sequence_1 = sequence_1 + code

    return sequence_1


def sequence_from_pdb(pdb_file_name):
    """
    Function extracting amino acid sequence from pdb file based.

    :param pdb_file_name: str, path to pdb file

    :return: str, sequence of protein extracted from pdb files
    """
    sequence = ''

    with open(f'{pdb_file_name}', 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('SEQRES'):
                sequence = sequence+line[19:]

    return sequence.replace(' ', '').replace('\n', '')


def extract_coordinates(atom, path, sequence):
    """
    Function extracting coordinates of specific type of atoms from pdb file.
    """
    coordinates = []
    sequence_length = len(sequence)

    with open(path, 'r') as pdb_file:
        counter = 0

        for line in pdb_file:
            if counter == sequence_length:
                break

            elif line.startswith('ATOM') and line[12:16] == atom:
                if line == sequence[counter]:
                    coordinates.append(line[0])
                    counter += 1

                    pass

    return coordinates


def construct_pdb_dict(pdb_files):
    # pbb_file + sequence
    pdb_dict = {}

    for path in pdb_files:
        if path in pdb_dict:
            print(f'more than one file with code {path}')
            continue
        else:
            pdb_dict[path] = {'sequence': code_3_to_1(sequence_from_pdb(path))}
            pdb_dict[path] = {'CA': extract_coordinates('CA', path, pdb_dict[path]['sequence'])}
            pdb_dict[path] = {'N': extract_coordinates('N', path, pdb_dict[path]['sequence'])}


def construct_initial_dataset(pdb_dict):
    pass
