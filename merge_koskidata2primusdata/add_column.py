import os
import sys
import glob
import click
import logging
import pandas as pd


@click.command()
@click.argument("source_file", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path(exists=True))
@click.option("-e", "--empty_value", type=click.STRING)
def main(source_file, output_path, empty_value=None):

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    # logger.infof(f"Trying to add column to file.")

    files = []

    try:
        for file in glob.glob(
            f"{output_path}{os.path.sep}kuukausiraportti_koski*.xlsx"
        ):
            files.append(
                {"relative_pathname": file, "filename": file.split(os.path.sep)[1]}
            )
    except Exception as error:
        logger.critical(
            f"Reading output filenames from relative path {output_path} failed. error: {error}"
        )
        sys.exit(0)

    try:
        source_data = pd.read_csv(f"{source_file}", encoding="utf-8", delimiter=";")
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
            combined = pd.merge(
                df,
                source_data,
                how="left",
                left_on="Opiskeluoikeuden tunniste lähdejärjestelmässä",
                right_on="Korttinumero",
            )
        except Exception as error:
            logger.critical(
                f"Combining KOSKI data and Primus data failed. error: {error}"
            )
            sys.exit(0)
        if empty_value is not None:
            combined[combined.columns[-1]] = combined[combined.columns[-1]].fillna("Ei")
        combined = combined.drop("Korttinumero", 1)

        try:
            combined.to_excel(
                f"{output_path}{os.path.sep}{file['filename']}", index=False,
            )
            logger.info(
                f"Writing combined data file {output_path}{os.path.sep}{file['filename']} succesfully."
            )
        except Exception as error:
            logger.critical(
                f"Saving combined data to file {output_path}{os.path.sep}{file['filename']} failed. error: {error}"
            )
            sys.exit(0)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

