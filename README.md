# GHG Data

## What is this?
GHG Data is a dataset compiled out of national greenhouse gas (GHG) inventory submissions by 
[Annex I](http://unfccc.int/parties_and_observers/parties/annex_i/items/2774.php) Parties to 
[UNFCCC](http://unfccc.int). The primary purpose of this dataset is to simplify comparison of and charting of GHG
data on a single-variable level. 

## How do I access GHG Data? 
Data is available on Amazon S3, in JSON format, one file per inventory variable. The URL format is 
 
http://ghg-data.s3-website.eu-central-1.amazonaws.com/<VARIABLE-UID>.json

The uid should be CAPITALIZED. 

The response is JSON in the following format: 

```json
{"years":[<list-of-years>],
 "series":{
  "<party-code>":[<list-of-values>]}
}
```
Where: 

* `list-of-years` is a list of strings with year names (brows back down and see below in gotchas) sorted alphabetically
* `party-code` is a three-letter code of the Party. In most cases, but not always, this is ISO ALPHA-3 code.
* `list-of-values` is a list of record values sorted according to the years in `list-of-years`

### Where do I get the variable uid? 

This is outside of the scope of this README. The short answer is that all variables are defined in UNFCCC metadata 
available [here](https://confluence.unfccc.int/download/attachments/17137769/meta_data_6.0.3.xml.zip).
If you are a user of UNFCCC CRF Reporter, you may see variable UIDs when you export reporting tables with uids. 
If you are a user of Spherical's [National Inventory System](http://nis.spherical.pm), you will find uids of variables
on cell info boxes on all data entry and reporting views. If you are neither, making sense of variable uids is not easy.

### Gotchas
_"Life is really simple, but we insist on making it complicated"_ - Confucius

#### Funny year names
Years are not numbered but rather named. This is because Parties are free to to name their reporting years the way they 
like, and Hungary used this freedom to name one of their years "1985-1987". In addition to that, there is a year that is
used as baseline for calculating the Party's performance in GHG reduction. This year is named "Base Year". Most of the 
time, you will not be needing these years but you'll need to filter them out on your side
 
#### Nulls
According to the rules, complete GHG inventories shall not have empty records or zeroes. At the same time, there is a number
of situations when a record does not contain a valid numeric value:
* The variable is non-numeric. 
* The Party could not report a number for some reason (the data point is zero, confidential, included in another 
variable or unavailable)
* The year is not applicable for the Party

In these cases the dataset will include `null` for the record. GHG management software usually treats most of such
cases as zeroes. If you are using the dataset for charting purposes and your charting library allows, it is better to 
use "missing dots" on the chart. 

## How fresh is the dataset? 

The dataset is based on the latest 2017 GHG inventory submissions.

## Come on, give me some uids to test my charts!

Sure! 
* [F05D8EF0-CD04-4769-81BE-303183271230](http://ghg-data.s3-website.eu-central-1.amazonaws.com/F05D8EF0-CD04-4769-81BE-303183271230.json) - Total direct national emissions in `kt CO2 equivalent`
* [B3C6CE61-81BF-440C-A5EC-3451AB9205B8](http://ghg-data.s3-website.eu-central-1.amazonaws.com/B3C6CE61-81BF-440C-A5EC-3451AB9205B8.json) - Total Methane emissions in `kt`
* [1D3FFBBD-28D5-4AD6-A543-9C6CC01B3F3B](http://ghg-data.s3-website.eu-central-1.amazonaws.com/1D3FFBBD-28D5-4AD6-A543-9C6CC01B3F3B.json) - Emissions from agriculture in `kt CO2 equivalent`
* [A4543811-91B0-4DE7-B239-83F43DF6DF4E](http://ghg-data.s3-website.eu-central-1.amazonaws.com/A4543811-91B0-4DE7-B239-83F43DF6DF4E.json) - Emissions from waste in `kt CO2 equivalent`
* [A5A0958C-BDF7-43CA-BE3C-EB76B9A24348](http://ghg-data.s3-website.eu-central-1.amazonaws.com/A5A0958C-BDF7-43CA-BE3C-EB76B9A24348.json) - Number of sheep in the country :) in `thousands`

## Legal status of this data
All data is produced by national governments and officially reported to the UN. Data is further dedicated to public 
domain by UNFCCC. This work, presented by [Spherical](http://www.spherical.pm), is a repackaging of public domain 
data which Spherical further dedicates to public domain. Important notes: 
* Although data has not been modified, no warranty of any kind is provided as to its accuracy, authenticity or integrity. 
**This is not an official source**. If you require officially sourced data, you will need to source it from the respective
national government or [from UNFCCC directly](http://unfccc.int/national_reports/annex_i_ghg_inventories/national_inventories_submissions/items/10116.php).
* Continuous availability of data is not pledged. The service may be interrupted or discontinued without notice. 
* Programming errors and irregularities in the original dataset may have led to errors in this data. No responsibility
is assumed for such errors. If you believe that you have found an error, please let us know. 
 
 