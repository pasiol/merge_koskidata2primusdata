import os
import sys
import glob
import click
import logging
import pandas as pd


@click.command()
@click.argument("source_file", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path(exists=True))
@click.option("-e", "--empty_value", default=None, type=click.STRING)
@click.option(
    "-e", "--primus_encoding", type=click.STRING, default="utf-8-sig", show_default=True
)
@click.option("-d", "--delimiter", type=click.STRING, default=";", show_default=True)
def main(source_file, output_path, empty_value, primus_encoding, delimiter):

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    # logger.infof(f"Trying to add column to file.")

    files = []

    try:
        for file in glob.glob(f"{output_path}{os.path.sep}*.xlsx"):
            files.append(
                {"relative_pathname": file, "filename": file.split(os.path.sep)[1]}
            )
    except Exception as error:
        logger.critical(
            f"Reading output filenames from relative path {output_path} failed. error: {error}"
        )
        sys.exit(0)

    try:
        source_data = pd.read_csv(
            f"{source_file}", encoding=primus_encoding, delimiter=delimiter
        )
    except Exception as error:
        logger.critical(f"Reading data from file {source_file} failed. error: {error}")
        sys.exit(0)

    for file in files:
        try:
            df = pd.read_excel(file["relative_pathname"],)
            logger.info(
                f"Reading KOSKI data file {file['relative_pathname']} to the dataframe succesfully."
            )
        except Exception as error:
            logger.critical(
                f"Reading koski data from file {file['relative_pathname']} failed. error: {error}"
            )
            sys.exit(0)
        try:
            merged = pd.merge(
                df,
                source_data,
                how="left",
                left_on="Opiskeluoikeuden tunniste lähdejärjestelmässä",
                right_on="Korttinumero",
            )
        except Exception as error:
            logger.critical(
                f"Merging KOSKI data and Primus data failed. error: {error}"
            )
            sys.exit(0)
        if empty_value is not None:
            merged[merged.columns[-1]] = merged[merged.columns[-1]].fillna("Ei")
        merged = merged.drop("Korttinumero", 1)

        try:
            merged.to_excel(
                f"{output_path}{os.path.sep}{file['filename']}", index=False,
            )
            logger.info(
                f"Writing merged data file {output_path}{os.path.sep}{file['filename']} succesfully."
            )
        except Exception as error:
            logger.critical(
                f"Saving merged data to file {output_path}{os.path.sep}{file['filename']} failed. error: {error}"
            )
            sys.exit(0)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

