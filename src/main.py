import os, shutil
from os.path import join
import supervisely as sly
from supervisely.io.fs import silent_remove, get_file_name
from supervisely.io.fs import mkdir

from dotenv import load_dotenv


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

INPUT_DIR: str = os.environ.get("modal.state.slyFolder", None)
INPUT_FILE: str = os.environ.get("modal.state.slyFile", None)

if INPUT_DIR:
    IS_ON_AGENT = api.file.is_on_agent(INPUT_DIR)
else:
    IS_ON_AGENT = api.file.is_on_agent(INPUT_FILE)

STORAGE_DIR: str = sly.app.get_data_dir()
mkdir(STORAGE_DIR, True)


class MyImport(sly.app.Import):
    def process(self, context: sly.app.Import.Context):

        project_dir = context.path
        if context.is_directory is False:
            project_folder = join(STORAGE_DIR, get_file_name(project_dir))
            shutil.unpack_archive(project_dir, project_folder)
            silent_remove(project_dir)
            project_dir = project_folder
        project_name = os.path.basename(project_dir)
        sly.upload_volume_project(
            dir=project_dir,
            api=api,
            workspace_id=context.workspace_id,
            project_name=project_name,
            log_progress=True,
        )


app = MyImport()
app.run()
