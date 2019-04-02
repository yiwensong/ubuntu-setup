import argparse

import yaml

def load_ppa_config(config_file='ppa.yaml'):
    """Loads a ppa config and returns the list of ppas and packages that
    are requested.
    """
    with open(config_file, 'r') as conf:
        conf = yaml.safe_load(conf)
    ppas = set(
        pkg['ppa'] for pkg in conf
    ) - {'default'}
    packages = set(pkg for pkgs in conf for pkg in pkgs['packages'])
    return {
        'ppas': ppas,
        'packages': packages,
    }


def generate_script(confdict, output_file=None):
    add_cmd_ppas = [
        'apt-add-repository -y ppa:{}'.format(ppa) for ppa in confdict['ppas']
    ]

    shebang = '#!/bin/sh'
    cmd_add = '\n'.join(add_cmd_ppas)
    cmd_update = 'apt-get update -y'
    cmd_install = 'apt-get install -y\\\n    {}'.format('\\\n    '.join(
        confdict['packages'],
    ))
    cmd_upgrade = 'apt-get upgrade -y'
    cmd_autoremove = 'apt autoremove -y'

    script = '\n'.join([
        shebang,
        cmd_add,
        cmd_update,
        cmd_install,
        cmd_upgrade,
        cmd_autoremove,
    ])

    if output_file:
        with open(output_file, 'w') as outf:
            outf.write(script)

    return script



def main():
    parser = argparse.ArgumentParser(description='generate a setup script for ubuntu')
    parser.add_argument(
        '-s',
        '--source',
        default='ppa.yaml',
        help='the file that contains package info',
    )
    parser.add_argument(
        '-o',
        '--output',
        default='install-apt-packages.sh',
        help='where to put the generated script',
    )
    args = parser.parse_args()
    
    confdict = load_ppa_config(args.source)
    script = generate_script(confdict, args.output)


if __name__ == '__main__':
    main()
