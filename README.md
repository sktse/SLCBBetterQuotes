# SLCBBetterQuotes

[![Latest](https://img.shields.io/github/release/sktse/SLCBBetterQuotes.svg)](https://github.com/sktse/SLCBBetterQuotes/releases/latest/) 
[![CircleCI](https://circleci.com/gh/sktse/SLCBBetterQuotes/tree/master.svg?style=svg)](https://circleci.com/gh/sktse/SLCBBetterQuotes/tree/master)

* A better quote system than what ships with Streamlabs ChatBot

### Table of Contents
* [Details](#details)
* [Installation](#installation)
    * [Installing Python 2.7.13](#install_python)
    * [Configuring Python for Streamlabs Chatbot](#configure_python)
    * [Importing Scripts into Streamlabs Chatbot](#import_script)
    * [Manually Uninstalling Scripts from Streamlabs Chatbot](#uninstall)
* [For Developers](#for-developers)

<a name="details"/>

## Details

* TBD

<a name="installation"/>

## Installation

<a name="install_python"/>

### Installing Python 2.7.13
* Streamlabs Chatbot scripts require that you have Python 2.7.13 installed on your local machine.
* You can download Python 2.7.13 from the official [Python Software Foundation Download page](https://www.python.org/downloads/release/python-2713/).
    * This is the direct link to the [Windows x86-64 MSI installer](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi).
* Run the `msi` file to install Python 2.7.13. You can do this by double-clicking the file.
* Go through the Python 2.7.13 installer wizard.
* By default, the installer will save Python in `C:\Python27`

<a name="configure_python"/>

### Configuring Python for Streamlabs Chatbot
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Settings button ![settings button](https://user-images.githubusercontent.com/11049883/47404591-eae89500-d71b-11e8-8a4e-89b3902a2541.png) in the top right corner of the tab.

![global script settings](https://user-images.githubusercontent.com/11049883/47404567-d1dfe400-d71b-11e8-9628-c76fe6942bc4.png)
* This will open up the Global Scrip Settings page for Streamlabs Chatbot
* Click the **Pick Folder** under the **Python 2.7.13 Directory** section
* This will open up a file explorer.  Select the folder of `\Python27\lib` folder.
    * The default Python installation path is `C:\Python27\lib`

<a name="import_script"/>

### Importing Scripts into Streamlabs Chatbot
* Streamlabs Chatbot supports importing scripts as Zip files.
* To download the `SLCBBetterQuotes` Zip file:
    * Find the latest release by go to the [latest release page](https://github.com/sktse/SLCBBetterQuotes/releases/latest)
    * Find all the releases, including older versions, by going to [releases tab](https://github.com/sktse/SLCBBetterQuotes/releases)
    * For the version you want to use, click the ![SLCBBetterQuotes.zip](https://user-images.githubusercontent.com/11049883/47473761-fbfbd980-d7e1-11e8-874d-276b50d835b6.png) link to download the Streamlabs Chatbot compatible Zip file.

![Streamlabs Chatbot Screenshot](https://user-images.githubusercontent.com/11049883/47262578-37349a80-d4ba-11e8-9812-c3354bebc13d.png)
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Import button ![import button](https://user-images.githubusercontent.com/11049883/48686710-71618c80-eb8b-11e8-838c-4bf83bde9438.png) in the top right corner of the tab.
* This will open up a file explorer.  Select the downloaded Zip file.

<a name="uninstall"/>

### Manually Uninstalling Scripts from Streamlabs Chatbot
* In your File Explorer, go to the folder where Streamlabs Chatbot is installed.
    * By default, Streamlabs Chatbot will be installed in `C:\Users\<your user name>\AppData\Roaming\Streamlabs\Streamlabs Chatbot`
* From the Streamlabs Chatbot folder, go to `\Services\Scripts`.  This is where Streamlabs Chatbot installs all the scripts.
* Delete any folders that start with `SLCBBetterQuotes`.
* In the Streamlabs Chatbot Scripts panel, click the Reload button ![refresh button](https://user-images.githubusercontent.com/11049883/47473935-ce636000-d7e2-11e8-89b6-86fed4c6c92c.png) to upload your scripts.
* The Better Quotes script should now be removed. 

<a name="for-developers"/>

## For Developers

* To setup the project, run `make install`
* To run tests, run `make test`
* To build the Streamlabs Chatbot `zip` file for release, run `make release`
* To reset the environment, run `make clean`
