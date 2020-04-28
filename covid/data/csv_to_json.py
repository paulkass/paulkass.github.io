import pandas as pd
import sys

csv_file = pd.DataFrame(pd.read_csv(sys.argv[1], sep = ",", header = 0, index_col = False))
csv_file.to_json(sys.argv[2], orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
