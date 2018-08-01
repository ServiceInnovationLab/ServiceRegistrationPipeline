# CKAN data pipeline

This is a set of command line scripts that can be used to pickup data files from one location and push it into a CKAN dataset using the API. It can be set up via a Cronjob to run regularly and ensure fresh data is available in your CKAN dataset.

## Requirements
 - git
 - python 2.7.14 (see `.python-version`)
 - pyenv and virtualenv
 - pip dependencies via requirements.txt
 - ssh
 - gpg (optional if dealing with encyrpted data)
 - A server to run on (should run on most distros, debian based prefered)

## Documentation

Here's what it does:

 - First, it fetches the data from an sftp pickup point. (see fetch.sh).
 - (Optional) Then it decrypts the data using gpg, the file should have been encrypted with your public key before you fetch it (see decrypt.sh).
 - Lastly, it publishes this data into a CKAN dataset either creating a new data resource or updating an existing one (see publish.sh).

### Getting started and installing on host machine
See [Docs](docs/en/index.md)

### Installing via Docker container
See [Docker docs](docs/en/docker.md)

## License
Licensed under the GNU General Public License Version 3.0 (GPLv3).

See [LICENSE](LICENSE.md).md

## Bugtracker
Bugs are tracked in the issues section of this repository. 

Before submitting an issue please read over existing issues to ensure yours is unique. 
 
If the issue does look like a new bug:
 
 - Create a new issue
 - Describe the steps required to reproduce your issue, and the expected outcome. Unit tests, screenshots 
 and screencasts can help here.
 - Describe your environment e.g. OS, software versions etc.
 
Please report security issues to the module maintainers directly. Please don't file security issues in the bugtracker.

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).md

## Maintainers
 - Cam Findlay ([camfindlay](https://github.com/camfindlay)) - cam.findlay@dia.govt.nz
 - [Brenda Wallace](brenda.wallace@dia.govt.nz) 
