import os
import sys
import glob
import click
import logging
import pandas as pd


@click.command()
@click.argument("koski_input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path(exists=True))
@click.argument("primus_data_file", type=click.Path(exists=True))
@click.option(
    "-e", "--primus_encoding", type=click.STRING, default="utf-8-sig", show_default=True
)
@click.option("-d", "--delimiter", type=click.STRING, default=";", show_default=True)
def main(koski_input_path, output_path, primus_data_file, primus_encoding, delimiter):
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger.info("Primus/Koski report merging started.")

    files = []

    try:
        for file in glob.glob(f"{koski_input_path}{os.path.sep}koski*.csv"):
            files.append(
                {"relative_pathname": file, "filename": file.split(os.path.sep)[1]}
            )
    except Exception as error:
        logger.critical(
            f"Reading input filenames from relative path {koski_input_path} failed. error: {error}"
        )
        sys.exit(0)

    try:
        primus_opphenk = pd.read_csv(
            "data/opphenk_data.csv", encoding=primus_encoding, delimiter=delimiter
        )
    except Exception as error:
        logger.critical(
            f"Reading primus data from file {primus_data_file} failed. error: {error}"
        )
        sys.exit(0)

    for file in files:
        try:
            df = pd.read_csv(
                file["relative_pathname"],
                encoding="windows-1252",
                delimiter=delimiter,
                decimal=",",
            )
            logger.info(
                f"Reading KOSKI data file {file['relative_pathname']} to the dataframe succesfully."
            )
        except Exception as error:
            logger.critical(
                f"Reading koski data from file {koski_input_path}{os.path.sep}{primus_data_file} failed. error: {error}"
            )
            sys.exit(0)
        try:
            merged = pd.merge(
                df,
                primus_opphenk,
                how="left",
                left_on="Opiskeluoikeuden tunniste lähdejärjestelmässä",
                right_on="Korttinumero",
            )
        except Exception as error:
            logger.critical(
                f"Merging KOSKI data and Primus data failed. error: {error}"
            )
            sys.exit(0)
        merged = merged.drop("Korttinumero", 1)

        student_dates_columns = [name for name in merged.columns if "(pv)" in name]
        for column in student_dates_columns:
            merged[column.replace("(pv)", "(v)")] = merged[column] / 365
        try:
            merged.to_excel(
                f"{output_path}{os.path.sep}raportti_{file['filename'][:-4]}.xlsx",
                index=False,
            )
            logger.info(
                f"Writing merged data file {output_path}{os.path.sep}raportti_{file['filename'][:-4]}.xlsx succesfully."
            )
        except Exception as error:
            logger.critical(
                f"Saving merged data to file {output_path}{os.path.sep}raportti_{file['filename'][:-4]}.xlsx failed. error: {error}"
            )
            sys.exit(0)

    merged.info()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

