<h1 align="center"> AirBnB clone - The console </h1>
<div id="header" align="center">
<img src="https://assets-global.website-files.com/603c87adb15be3cb0b3ed9b5/610e34d74c178bd24998a886_39.png" alt="luggage" width="200"/>
</div>

## About the project
<div>
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231102%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231102T011416Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=45516547395deb121414149d7202d0d236ba51c59870c2a78ecdf9383f39f3c3"/>
</div>

The AirBnB clone project comprises of four parts, the console, the front-end website, the database and an API. This particular project is the console, the first piece of the AirBnB clone. The requirements of the console project are as follows:
- create your data model
- manage (create, update, destroy, etc) objects via a console/command interpreter
- store and persist objects to a file (JSON file)

## Table of contents
<details>
    <summary>Table of Contents</summary>
    <ul>
    <li>
    <a href="#requirements">Requirements</a>
    </li>
    <li>
    <a href="#getting-started">Getting Started</a>
        <ul>
        <li><a href="#installation">Installation</a></li>
        </ul>
    <li>
    <a href="#usage">Usage</a>
        <ul>
            <li><a href="#command-interpreter">Command Interpreter</a></li>
        </ul>
    </li>
    <li>
    <a href="#authors">Authors</a>
    </li>
    </ul>
</details>

## Requirements
<ul>
<li>Ubuntu 20.04 LTS</li>
	<ul>
<li><a href="https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview">Windows 10 or 11</a></li>
<li><a href="https://ubuntu.com/download/desktop">Mac</a></li>
	</ul>
<li>Python3 (version 3.8.x)</li>
<li>Follows pycodestyle checks</li>
</ul>

## Getting Started
To get a local copy up and running on your own machine, follow these simple steps:

### Installation

- If you don't already have Python 3.8.x, install Python
`sudo apt-get install python3`

- Clone this repository
`git clone https://github.com/chelseyqc/holbertonschool-AirBnB_clone`

## Usage
The command interpreter allows you to manipulate data without a visual interface. For the AirBnB clone, it allows you to create new objects, retrieve objects from files or databases, update object attributes, etc.

### Command Interpreter
The command interpreter can be used in two modes, interactive mode or non-interactive mode.
To start the command interpreter in the interactive mode you can run one of the following commands:

`./console.py`

or

`python3 console.py`

Once the command interpreter is running the the interactive mode, you can use the following commands:

|**Command**|**Description**|
|-----------|---------------|
|`create`| Creates a new instance of a class |
|`show`| Prints the instance with the class name and ID |
|`destroy`| Deletes an instance based on the class name and ID |
|`all`| Prints all instances |
|`update`| Updates an instance with an attribute based on the class name and ID |
|`help`| Displays a list of the available commands |
|`quit`| Exits the command interpreter |

In non-interactive mode, you can provide commands through a pipe or input redirection.

`echo "all" | ./console.py`

## Authors
- [Alicia Tan](https://github.com/aliciastudies)
- [Chelsey Chia](https://github.com/chelseyqc)