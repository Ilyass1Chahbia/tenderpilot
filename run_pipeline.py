import  subprocess, sys, logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)
try:
    logging.info("Fetch started")
    subprocess.run(
        [sys.executable, "fetch_tenders.py"],
        check=True
    )
    logging.info("Fetch completed")

    logging.info("Storage started")
    subprocess.run(
        [sys.executable, "store_tenders.py"],
        check=True
    )
    logging.info("Storage completed")
except subprocess.CalledProcessError:
    logging.exception("Pipeline failed")
    raise