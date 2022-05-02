import os
import pathlib
import platform
import shutil
import subprocess
import sys

import pkg_resources


def install_windows(update_settings: bool = True) -> None:
    installer_folder = pathlib.Path(os.path.dirname(__file__))
    print(f'Installation found at: {installer_folder}')

    program_files = pathlib.Path(os.environ['ProgramW6432']).joinpath('util')
    print(f'Program folder resolved as: {program_files}')

    try:
        shutil.copytree(installer_folder.joinpath(pathlib.Path('util')),
                        program_files,
                        dirs_exist_ok=True)
    except PermissionError as exception:
        print(f'{exception.strerror}: {exception.filename}. Please run in Administrator mode.')
        return

    required = {'python-magic-bin',}
    installed = set(map(lambda i: i.project_name, pkg_resources.working_set))
    missing = required - installed
    if missing:
        print(f'Installing missing packages {missing}')
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    else:
        print('All required packages are installed')
    print(f'Installation completed. Add {program_files} to PATH')


def main() -> None:
    match platform.system():
        case 'Windows':
            install_windows(False)
        case _:
            print('Platform is not supported')


if __name__ == '__main__':
    main()
