<div align="center" markdown>

<img src="https://i.imgur.com/yRR9brX.png" style="width: 100%;"/>

# Import Volumes in Supervisely format

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-to-Run">How to Run</a> •
  <a href="#Demo">Demo</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-volumes-with-anns)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-volumes-with-anns)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/import-volumes-with-anns)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/import-volumes-with-anns)](https://supervise.ly)

</div>

# Overview

Import volumes in Supervisely format with annotations. Volume files must be in `.NRRD` format.


#### Input files structure

You can upload a directory or an archive. If you are uploading an archive, it must contain a single top-level directory.

Directory name defines project name. Subdirectories define dataset names.

Project directory example:

```
.
my_volumes_project
├── ds1
│   ├── ann
│   │   └── MRHead.nrrd.json
│   └── volume
│       └── MRHead.nrrd
├── ds2
│   ├── ann
│   │   ├── CTACardio.nrrd.json
│   │   └── CTChest.nrrd.json
│   ├── interpolation
│   │   └── CTChest.nrrd
│   │       └── daff638a423a4bcfa34eb12e42243a87.stl
│   └── volume
│       ├── CTACardio.nrrd
│       └── CTChest.nrrd
├── key_id_map.json
└── meta.json

```

As a result we will get project `my_volumes_project` with 2 datasets named: `ds1` and `ds2`.

# How to Run

**Step 1.** Add [Import Volumes in Supervisely format](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-volumes-with-anns) app to your team from Ecosystem

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/import-volumes-with-anns" src="https://i.imgur.com/16lSFXP.png" width="350px" style='padding-bottom: 10px'/>

**Step 2.** Run the application from the context menu of the directory with images on Team Files page

<img src="https://i.imgur.com/zqpVnE8.png" width="80%" style='padding-top: 10px'>  

**Step 3.** Press the Run button in the modal window

<img src="https://i.imgur.com/raSxilo.png" width="80%" style='padding-top: 10px'>

**Step 4.** After running the application, you will be redirected to the Tasks page. Once application processing has finished, your project will become available. Click on the project name to open it.

<img src="https://i.imgur.com/xnPdWWa.png" width="80%" style='padding-top: 10px'>

### Demo
Example of uploading volumes project with annotations to Supervisely:
![](https://i.imgur.com/61MvEbb.gif)


