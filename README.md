<div align="center" markdown>

<img src="https://user-images.githubusercontent.com/48245050/182855159-50a5c414-268d-4d50-9d2a-b04c04fb07bf.jpg"/>

# Import Volumes in Supervisely format

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#whats-new">What's new</a> •
  <a href="#how-to-run">How to Run</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-volumes-with-anns)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-volumes-with-anns)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/import-volumes-with-anns.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/import-volumes-with-anns.png)](https://supervise.ly)

</div>

## Overview

Import volumes in Supervisely format with annotations. Volume files must be in `.NRRD` format.


## What's new 

Version `v1.3.0`
 - 🏷️ new format for storing `Mask3D` geometry as `.nrrd` files in the `mask` directory. To learn more read [this article](https://docs.supervisely.com/data-organization/00_ann_format_navi/08_supervisely_format_volume).
 - ℹ️ Convert closed mesh surfaces `.stl` to `Mask3D` automatically on uploading due to format obsolescence. On subsequent export you will get interpolation annotation objects as `Masks3D` with geometries in `.nrrd` files.

Version `v1.2.0`
 - 🏋️ application supports import from a special directory on your local computer. It is made for Enterprise Edition customers who need to upload tens or even hundreds of gigabytes of data without using a drag-and-drop mechanism:
    1. Run an agent on your computer where data is stored. Watch the [how-to video](https://youtu.be/aO7Zc4kTrVg).
    2. Copy your data to a special folder on your computer that was created by the agent. Agent mounts this directory to your Supervisely instance and it becomes accessible in Team Files. Learn more in the [documentation](https://docs.supervise.ly/customization/agents/agent-storage). Watch the [how-to video](https://youtu.be/63Kc8Xq9H0U).
    3. Go to `Team Files` -> `Supervisely Agent` and find your folder there.
    4. Right-click to open context the menu and start the app. Now the app will upload data directly from your computer to the platform.


## How to Run

#### Input files structure

You can upload a directory or an archive. If you are uploading an archive, it must contain a single top-level directory.<br>
ℹ️ You can download the archive with data example [here](https://github.com/supervisely-ecosystem/import-volumes-with-anns/files/12548165/my_volume_project.zip).<br>

The directory name defines the project name. Subdirectories define dataset names.

Project directory example:

```
📦project.tar
 └──📂project_dir
     ├──📂dataset_1
     │   ├──📂ann
     │   │   ├──📜MRHead.nrrd.json
     │   │   └── ...    
     │   ├──📂interpolation
     │   │   ├──📂MRHead.nrrd
     │   │   │   ├──📜daff638a423a4bcfa34eb12e42243a87.stl
     │   │   │   └── ...
     │   │   └── ... 
     │   ├──📂mask
     │   │   ├──📂MRHead.nrrd
     │   │   │   ├──📜78cc73a8bd654ab3951dde035f760ab1.nrrd
     │   │   │   └── ...
     │   │   └── ... 
     │   └──📂volume
     │        ├──📜MRHead.nrrd
     │        └── ...    
     ├──📂...
     │
     ├──📜key_id_map.json
     └──📜meta.json
```

As a result, we will get project `my_volumes_project` with 2 datasets named: `ds1` and `ds2`.

**Step 1.** Add [Import Volumes in Supervisely format](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-volumes-with-anns) app to your team from Ecosystem

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/import-volumes-with-anns" src="https://i.imgur.com/16lSFXP.png" width="350px" style='padding-bottom: 10px'/>

**Step 2.** Run the application from the context menu of the directory with images on the Team Files page

<img src="https://i.imgur.com/zqpVnE8.png" width="80%" style='padding-top: 10px'>  

**Step 3.** Press the Run button in the modal window

<img src="https://i.imgur.com/raSxilo.png" width="80%" style='padding-top: 10px'>

**Step 4.** After running the application, you will be redirected to the Tasks page. Once application processing has finished, your project will become available. Click on the project name to open it.

<img src="https://i.imgur.com/xnPdWWa.png" width="80%" style='padding-top: 10px'>



