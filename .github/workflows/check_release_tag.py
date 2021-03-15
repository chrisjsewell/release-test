"""Check that the GitHub release tag matches the version."""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('GITHUB_REF', help='The GITHUB_REF environmental variable')
    parser.add_argument('SETUP_PATH', help='Path to the setup.json')
    args = parser.parse_args()
    assert args.GITHUB_REF.startswith('refs/tags/v'), f'GITHUB_REF should start with "refs/tags/v": {args.GITHUB_REF}'
    tag_version = args.GITHUB_REF[11:]
    with open(args.SETUP_PATH) as handle:
        data = json.read(handle)
    pypi_version = data['version']
    assert tag_version == pypi_version, f'{tag_version} != {pypi_version}'

