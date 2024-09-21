import argparse
import logging
import os
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(Path().resolve())
ASSETS_DIR = Path(__file__).parent / "assets"
BASE_PROJECT_DIR = ASSETS_DIR / "base_project"

DISTRIBUTION_TOOL_MACOS = ASSETS_DIR / "DistributionTool"
DISTRIBUTION_TOOL_WINDOWS = ASSETS_DIR / "DistributionTool.exe"


def main():
    parser = argparse.ArgumentParser(description="StreamDeckSDK")
    parser.add_argument("command")
    parser.add_argument("-i", default=None, required=False, type=str, help="Input file", )
    parser.add_argument('-F', action='store_true', help="Force build", )
    args = parser.parse_args()
    logger.info(args)
    command = args.command
    if command == "startproject":
        shutil.copytree(str(BASE_PROJECT_DIR.resolve()), str(BASE_DIR.resolve()), symlinks=False, dirs_exist_ok=True)
    elif command == "build":
        if args.i is None:
            raise ValueError("Invalid value for -i param.")
        input_file = str(Path(args.i).resolve())

        now = datetime.now()
        dt = now.strftime("%Y_%m_%d_%H_%M_%S")
        release_dir = BASE_DIR / f"releases/{dt}"
        release_dir.mkdir(exist_ok=True, parents=True)
        release_dir = str(release_dir.resolve())

        [p.unlink() for p in BASE_DIR.rglob('*.py[co]')]
        [p.rmdir() for p in BASE_DIR.rglob('__pycache__')]

        force = args.F
        if force:
            force_build(i=input_file, o=release_dir)
            return

        os_name = platform.system()
        logger.info(os_name)
        if os_name == "Darwin":
            distribution_tool = str(DISTRIBUTION_TOOL_MACOS.resolve())
        elif os_name == "Windows":
            distribution_tool = str(DISTRIBUTION_TOOL_WINDOWS.resolve())
        else:
            raise ValueError("Unsupported Operation System.")
        os.chmod(distribution_tool, 755, )
        subprocess.run(
            [distribution_tool, "-b", "-i", input_file, "-o", release_dir],
        )


def force_build(i: str, o: str) -> None:
    i = Path(i)
    o = Path(o)
    output_zip_base_name = o / i.name
    shutil.make_archive(
        base_name=str(output_zip_base_name.resolve()),
        format="zip",
        root_dir=str(i.parent.resolve()),
        base_dir=i.name,
    )
    output_zip_file_path = o / f"{i.name}.zip"
    output_plugin_file_path = o / i.name.replace(".sdPlugin", ".streamDeckPlugin")
    os.rename(
        str(output_zip_file_path.resolve()),
        str(output_plugin_file_path.resolve())
    )
