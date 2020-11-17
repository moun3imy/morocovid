import argparse
import covid_stats_json
import utils

parser = argparse.ArgumentParser("Generate Morocco's COVID-19  data ")
parser.add_argument('Date',
                    type = str,
                    help = 'date to generate the data for,\n provided in dd-MM-yy with non padding zero when day or month are <10'
                    )
parser.add_argument('-from',
                    type = str,
                    help = 'date to generate the data from, works with the parameter "to",\n provided in dd-MM-yy with non padding zero when day or month are <10'
                    )
parser.add_argument('-to',
                    type = str,
                    help = 'generate the data until this date, works with the parameter "from",\n provided in dd-MM-yy with non padding zero when day or month are <10'
                    )
parser.add_argument('-city',
                    type = str, 
                    help = 'generate the covid-19 data of particular city'
                    )

args = parser.parse_args()

date = args.Date

print(covid_stats_json.get_coronavirus_json(date))