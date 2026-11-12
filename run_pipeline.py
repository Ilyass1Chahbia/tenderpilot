import  subprocess, sys, logging
from pathlib import Path

project_dir = Path(__file__).resolve().parent

logging.basicConfig(
    filename=project_dir / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)
try:
    logging.info("Fetch started")
    subprocess.run(
        [sys.executable, "fetch_tenders.py"],
        cwd=project_dir,
        check=True
    )
    logging.info("Fetch completed")

    logging.info("Storage started")
    subprocess.run(
        [sys.executable, "store_tenders.py"],
        cwd=project_dir,
        check=True
    )
    logging.info("Storage completed")
except subprocess.CalledProcessError:
    logging.exception("Pipeline failed")
    raise