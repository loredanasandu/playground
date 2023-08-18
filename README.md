# playground
Miscellaneous scripts and notebooks made for fun to try stuff out. Some of them are quick tools, most of them are random experiments made out of curiosity.

## Contents
- [Image thresholding](#image-thresholding)
- [Search in pi](#search-in-pi)
- [Select column from csv](#select-column-from-csv)

### [Image thresholding](image-thresholding)
Converts pixel images to binary images using the Pillow library. Performed image thresholding on a couple of NASA's Jupiter photos.

### [Search in pi](search-in-pi)
Searches for a number input by the user among the decimals of $\pi$. A million digits of $\pi$ are loaded from `pi-million.txt` file.

### [Select column from csv](select-column-from-csv)
Selects a column from input csv files named `input1.csv`, `input2.csv`... Creates output csv files named `output1.csv`, `output2.csv`,...
The output files contain a specified number of first rows unchanged from the input files, and afterwards, all the rows from the selected column.
All files are stored in the `csv_files` directory.
