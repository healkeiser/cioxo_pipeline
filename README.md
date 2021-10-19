<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/healkeiser/Cioxo">
    <img src="all/ui/graphics/logos/cioxoLogo_border.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Cioxo</h3>

  <p align="center">
    Cioxo Pipeline
    <br />
    <a href="https://github.com/healkeiser/Cioxo"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/healkeiser/Cioxo">View Demo</a>
    ·
    <a href="https://github.com/healkeiser/Cioxo">Report Bug</a>
    ·
    <a href="https://github.com/healkeiser/Cioxo">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Cioxo Pipeline is an under development VFX pipeline for freelancers/small scaled productions. 

<a href="https://github.com/healkeiser/Cioxo">
    <img src="all/ui/graphics/screenshots/cioxo_splashScreen_screenshot_02.png" height="560">
  </a>

### Built With

* [PySide](https://github.com/PySide)



<!-- GETTING STARTED -->
## Getting Started

In order to make Cioxo work, here is what needs to be done.

### Prerequisites

Here are all the Python libraries you'll need:
* PySide2

  ```sh
  pip install PySide2
  ```

### Installation

Under construction



<!-- USAGE EXAMPLES -->
## Usage

The two main programs are:

* [Define Root](https://github.com/healkeiser/Cioxo/blob/main/all/cioxo_main_defineRoot.py)

**Cioxo - Define Root** needs to run first, it will define the rootDirectory of all your projects. 

> Note that the **rootDirectory** can be changed at any time by simply running Cioxo - Define Root again

* [Project Manager](https://github.com/healkeiser/Cioxo/blob/main/all/cioxo_main_projectManager.py)

Once **Cioxo - Define Root** has created the needed directories and files, you can run **Cioxo - Project Manager**. This program is the heart of the pipeline, centralizing all the projects, sequences, shots, assets, and other useful informtations such as the Frame Range, or the Project Resolution. It can also create the files for the included DDCs while the integrations are under development.

Under construction

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

- [x] Project Manager

    - [x] Projects
    - [x] Assets
    - [x] Sequences
    - [x] Shots
    - [x] Frame Range
    - [x] Resolution
    - [x] Thumbnail
    - [x] Comment

- [ ] DCCs integrations

    - [ ] Houdini
    
        - [ ] Open Workspace
        - [x] Publish Workspace
        - [x] Help
        - [x] About

    - [ ] Nuke
    - [ ] Substance Painter
    - [ ] After Effects
    - [ ] Photoshop



<!-- CONTACT -->
## Contact

Valentin Beaumont - [LinkedIn](https://uk.linkedin.com/in/valentin-beaumont) - [Behance](https://www.behance.net/el1ven) - valentin.onze@gmail.com

Project Link: [Cioxo](https://github.com/healkeiser/Cioxo)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

List of resources that helped me through it:

* [Awesome CG / VFX Pipeline](https://github.com/cgwire/awesome-cg-vfx-pipeline)



<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: all/ui/graphics/screenshots/cioxo_splashScreen_screenshot_02.png
