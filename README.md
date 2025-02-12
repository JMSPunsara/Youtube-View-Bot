# YouTube View Bot

This is a tool designed to boost the viewer count on a YouTube video. It is not intended for malicious purposes or monetization strategies. This tool was created for personal use and testing purposes.

## Developed By
This script was developed by **PunsaraJMS**.

- [Facebook](https://web.facebook.com/PunsaraJMS/)
- [Instagram](https://www.instagram.com/punsarajms/)
- [LinkedIn](https://www.linkedin.com/in/punsara-jms-98b3772a0/)

## Installation

### Python Version
Download the latest version of [Python](https://www.python.org/downloads/).

This program was developed using Python 3.9.0, but it should work with Python 3.9.0+ versions.

### Downloading the GitHub Repository
To install the repository, you can use the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
pip install https://github.com/JMSPunsara/Youtube-View-Bot.git

```
## Configuration

`config.json`

Enter the required settings into the `config.json` file:

```bash
{
    "website": "YOUR VIDEO URL", 
    "tab_amount": 3,
    "watch_time": 35,
    "view_cycles": 5,
    "browser": "chrome"
}
```
Note: Make sure to replace "YOUR VIDEO URL" with the actual URL of the YouTube video you want to boost.


## Usage
### How to Run the Program
After completing the setup and configuration, open a terminal in this directory and run the following command:
```bash
python main.py
```

This will start the bot, which will begin simulating views on your YouTube video according to the configurations you set in the `config.json` file.

## Contributing
Pull requests are welcome! If you're planning to make major changes, please open an issue first to discuss what you'd like to change.

Make sure to update the tests as needed.
