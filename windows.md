

## Installation

        mkdir opiskelijavuodet && cd opiskelijavuodet
        python -m venv venv
        venv\Scripts\activate
        pip install merge-koskidata2primusdata

## Upgrading

        cd opiskelijavuodet
        venv\Scripts\activate
        pip install --no-cache-dir --upgrade merge-koskidata2primusdata==0.3.0


## Datafiles

### Koski-data

         Directory of D:\code\opiskelijavuodet\2020-03-02

        02.03.2020  08:14    <DIR>          .
        02.03.2020  08:14    <DIR>          ..
        02.03.2020  08:05         2 981 034 koski_opiskelijavuodet_2018.csv
        02.03.2020  08:06         3 177 914 koski_opiskelijavuodet_2019.csv
        02.03.2020  08:12         1 913 851 koski_opiskelijavuodet_2020.csv
        02.03.2020  08:14         2 037 895 koski_opiskelijavuodet_2020_helmikuu.csv
        02.03.2020  08:13         1 944 400 koski_opiskelijavuodet_2020_tammikuu.csv

### Primus-data

        Directory of D:\code\opiskelijavuodet\pq

        02.03.2020  08:27    <DIR>          .
        02.03.2020  08:27    <DIR>          ..
        02.03.2020  08:27            17 583 et.csv
        25.02.2020  11:16               323 et1.priq
        25.02.2020  11:08               252 et2.priq
        27.02.2020  12:56             1 861 opphenk.priq
        02.03.2020  08:26        11 888 744 opphenk_data.csv
        02.03.2020  08:27            29 318 oppisopimus.csv
        25.02.2020  10:50               368 oppisopimus.priq

# merge

## Duplicates

If same student is duplicate on the Koski data, getting following error on merging, when validation is on.

        CRITICAL - Merging KOSKI data and Primus data failed. error: Merge keys are not unique in left dataset; not a one-to-one merge
        INFO - Duplicated identifiers on Koski report: [NNNNNN, NNNNNN, NNNNNN]

If same student is more than one time on the primusquery generated file, getting following error.

        CRITICAL - Merging KOSKI data and Primus data failed. error: Merge keys are not unique in right dataset; not a one-to-one merge
        INFO - Duplicated identifiers on Primus report: [NNNNNN, NNNNNN, NNNNNN]

If you want do merging despite of the duplicates, option -v can disable validation.

        merge_student_years 2020-03-02 output pq\opphenk_data.csv -v False

## Running

        (venv) D:\code\opiskelijavuodet>merge_student_years 2020-03-02 output pq\opphenk_data.csv
        2020-03-02 08:45:45,791 - merge_koskidata2primusdata.merge_student_years - INFO - Primus/Koski report merging started.
        2020-03-02 08:45:45,956 - merge_koskidata2primusdata.merge_student_years - INFO - Reading Primus data file pq\opphenk_data.csv to the dataframe succesfully.
        2020-03-02 08:45:46,020 - merge_koskidata2primusdata.merge_student_years - INFO - Reading KOSKI data file 2020-03-02\koski_opiskelijavuodet_2018.csv to the dataframe succesfully.
        2020-03-02 08:46:03,372 - merge_koskidata2primusdata.merge_student_years - INFO - Writing merged data file output\raportti_koski_opiskelijavuodet_2018.xlsx succesfully.
        2020-03-02 08:46:03,455 - merge_koskidata2primusdata.merge_student_years - INFO - Reading KOSKI data file 2020-03-02\koski_opiskelijavuodet_2019.csv to the dataframe succesfully.
        2020-03-02 08:46:22,194 - merge_koskidata2primusdata.merge_student_years - INFO - Writing merged data file output\raportti_koski_opiskelijavuodet_2019.xlsx succesfully.
        2020-03-02 08:46:22,252 - merge_koskidata2primusdata.merge_student_years - INFO - Reading KOSKI data file 2020-03-02\koski_opiskelijavuodet_2020.csv to the dataframe succesfully.
        2020-03-02 08:46:33,970 - merge_koskidata2primusdata.merge_student_years - INFO - Writing merged data file output\raportti_koski_opiskelijavuodet_2020.xlsx succesfully.
        2020-03-02 08:46:34,032 - merge_koskidata2primusdata.merge_student_years - INFO - Reading KOSKI data file 2020-03-02\koski_opiskelijavuodet_2020_helmikuu.csv to the dataframe succesfully.
        2020-03-02 08:46:46,469 - merge_koskidata2primusdata.merge_student_years - INFO - Writing merged data file output\raportti_koski_opiskelijavuodet_2020_helmikuu.xlsx succesfully.
        2020-03-02 08:46:46,529 - merge_koskidata2primusdata.merge_student_years - INFO - Reading KOSKI data file 2020-03-02\koski_opiskelijavuodet_2020_tammikuu.csv to the dataframe succesfully.
        2020-03-02 08:46:58,701 - merge_koskidata2primusdata.merge_student_years - INFO - Writing merged data file output\raportti_koski_opiskelijavuodet_2020_tammikuu.xlsx succesfully.


Example of the dataframe info. Fields 0-44 are Koski data and after 44 are Primus data.

        <class 'pandas.core.frame.DataFrame'>
        Int64Index: 6396 entries, 0 to 6395
        Data columns (total 99 columns):
        #   Column                                                          Non-Null Count  Dtype
        ---  ------                                                          --------------  -----
        0   Opiskeluoikeuden oid                                            6396 non-null   object
        1   Lähdejärjestelmä                                                6396 non-null   object
        2   Opiskeluoikeuden tunniste lähdejärjestelmässä                   6396 non-null   int64
        3   Sisältyy opiskeluoikeuteen                                      9 non-null      object
        4   Ostettu                                                         6396 non-null   object
        5   Sisältyvät opiskeluoikeudet                                     102 non-null    object
        6   Sisältyvien opiskeluoikeuksien oppilaitokset                    102 non-null    object
        7   Päivitetty                                                      6396 non-null   object
        8   Toimipisteet                                                    6396 non-null   object
        9   Yksilöity                                                       6396 non-null   object
        10  Oppijan oid                                                     6396 non-null   object
        11  Sukunimi                                                        6396 non-null   object
        12  Etunimet                                                        6396 non-null   object
        13  Suorituksen tyyppi                                              6396 non-null   object
        14  Tutkinnot                                                       6396 non-null   object
        15  Osaamisalat                                                     4610 non-null   float64
        16  Päätason suorituksen suoritustapa                               6234 non-null   object
        17  Opiskeluoikeuden alkamispäivä                                   6396 non-null   object
        18  Viimeisin opiskeluoikeuden tila                                 6396 non-null   object
        19  Viimeisin opiskeluoikeuden tila aikajakson lopussa              6396 non-null   object
        20  Rahoitukset                                                     6214 non-null   float64
        21  Läsnä rahoitus syötetty                                         6396 non-null   object
        22  Loma/valmistunut rahoitus syötetty                              6396 non-null   object
        23  Päättynyt                                                       6396 non-null   object
        24  Päättymispäivä                                                  370 non-null    object
        25  Arvioitu päättymispäivä                                         6396 non-null   object
        26  Opiskelijavuosikertymä (pv)                                     6396 non-null   float64
        27  Läsnä tai valmistunut (pv)                                      6396 non-null   int64
        28  Opiskelijavuoteen kuuluvat lomat (pv)                           6396 non-null   int64
        29  Muut lomat (pv)                                                 6396 non-null   int64
        30  Majoitus (pv)                                                   6396 non-null   int64
        31  Sisäoppilaitosmainen majoitus (pv)                              6396 non-null   int64
        32  Vaativan erityisen tuen yhteydessä järjestettävä majoitus (pv)  6396 non-null   int64
        33  Erityinen tuki (pv)                                             6396 non-null   int64
        34  Vaativat erityisen tuen tehtävä (pv)                            6396 non-null   int64
        35  Hojks (pv)                                                      6396 non-null   int64
        36  Vaikeasti vammainen (pv)                                        6396 non-null   int64
        37  Vammainen ja avustaja (pv)                                      6396 non-null   int64
        38  Osa-aikaisuusjaksot (prosentit)                                 461 non-null    object
        39  Osa-aikaisuus keskimäärin (%)                                   6396 non-null   float64
        40  Opiskeluvalmiuksia tukevat opinnot (pv)                         6396 non-null   int64
        41  Vankilaopetuksessa (pv)                                         6396 non-null   int64
        42  Oppisopimus (pv)                                                6396 non-null   int64
        43  Henkilöstökoulutus                                              6396 non-null   object
        44  Koulutusvienti                                                  6396 non-null   object
        45  Koulutus                                                        6396 non-null   object
        46  Tavoite koulutuksessa                                           6393 non-null   object
        47  Tutkintotyyppi                                                  6396 non-null   object
        48  Yhdistelmäopintojen tyyppi                                      293 non-null    object
        49  Kustannuspaikka-alueet                                          6395 non-null   float64
        50  Tiimi                                                           6396 non-null   object
        51  Toimiala                                                        6396 non-null   object
        52  Yksikkö                                                         6396 non-null   object
        53  Tutkinto                                                        6376 non-null   object
        54  Opiskelijalaji                                                  6396 non-null   object
        55  Kustannuspaikka                                                 6395 non-null   float64
        56  Toiminto 1                                                      6395 non-null   float64
        57  Toiminto 2                                                      6395 non-null   float64
        58  Työvoimakoulutus                                                6396 non-null   object
        59  Kansalaisuus                                                    6392 non-null   object
        60  Aloituspvm                                                      6396 non-null   object
        61  Koulutuspäällikkö                                               6396 non-null   object
        62  Ryhmävalmentaja                                                 6396 non-null   object
        63  Opinto-ohjaaja                                                  6396 non-null   object
        64  Opintosihteeri                                                  6396 non-null   object
        65  Viimeisin rahoitusmuoto                                         6395 non-null   object
        66  Kotikunta                                                       6390 non-null   object
        67  Ikä                                                             6396 non-null   int64
        68  Sukupuoli                                                       6395 non-null   object
        69  Opintoala                                                       6303 non-null   object
        70  Koulutusala                                                     6396 non-null   object
        71  Arvioitu opintojen kesto vuosina                                6396 non-null   object
        72  Asuinkunta                                                      5334 non-null   object
        73  Osaamisala                                                      4611 non-null   object
        74  Eron syy                                                        6396 non-null   int64
        75  Keskeytyksen syy                                                6396 non-null   int64
        76  Äidinkieli                                                      6390 non-null   object
        77  pvm alkaen viimeinen                                            6395 non-null   object
        78  pvm saakka viimeinen                                            6395 non-null   object
        79  opiskeluoikeuden tila viimeinen (primus)                        6395 non-null   object
        80  Projektikoodit                                                  26 non-null     object
        81  Tutkintokoodi                                                   6352 non-null   float64
        82  Opiskelumuoto                                                   5444 non-null   object
        83  Yhteishaun kautta                                               6396 non-null   object
        84  Opiskelijavuosikertymä (v)                                      6396 non-null   float64
        85  Läsnä tai valmistunut (v)                                       6396 non-null   float64
        86  Opiskelijavuoteen kuuluvat lomat (v)                            6396 non-null   float64
        87  Muut lomat (v)                                                  6396 non-null   float64
        88  Majoitus (v)                                                    6396 non-null   float64
        89  Sisäoppilaitosmainen majoitus (v)                               6396 non-null   float64
        90  Vaativan erityisen tuen yhteydessä järjestettävä majoitus (v)   6396 non-null   float64
        91  Erityinen tuki (v)                                              6396 non-null   float64
        92  Vaativat erityisen tuen tehtävä (v)                             6396 non-null   float64
        93  Hojks (v)                                                       6396 non-null   float64
        94  Vaikeasti vammainen (v)                                         6396 non-null   float64
        95  Vammainen ja avustaja (v)                                       6396 non-null   float64
        96  Opiskeluvalmiuksia tukevat opinnot (v)                          6396 non-null   float64
        97  Vankilaopetuksessa (v)                                          6396 non-null   float64
        98  Oppisopimus (v)                                                 6396 non-null   float64
        dtypes: float64(24), int64(18), object(57)
        memory usage: 4.9+ MB

# add_column 

        add_column pq\oppisopimus.csv output -e Ei