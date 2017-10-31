# GHG Data

## What is this?
GHG Data is a dataset compiled out of national greenhouse gas (GHG) inventory submissions by 
[Annex I](http://unfccc.int/parties_and_observers/parties/annex_i/items/2774.php) Parties to 
[UNFCCC](http://unfccc.int). The primary purpose of this dataset is to simplify comparison and charting of GHG
data on a single-variable level. 

## How do I access GHG Data? 
Data is available on Amazon S3, in JSON format, one file per inventory variable. The URL format is 
 
http://ghg-data.s3-website.eu-central-1.amazonaws.com/VARIABLE-UID.json

The uid should be CAPITALIZED. 

The response is JSON in the following format: 

```json
{"years":["list","of","years"],
 "series":{
  "<party-code>":["list","of","values"]}
}
```
Where: 

* `"list","of","years"` is a list of strings with year names (brows back down and see below in gotchas) sorted alphabetically
* `party-code` is a three-letter code of the Party. In most cases, but not always, this is an [ISO ALPHA-3](https://www.iso.org/obp/ui/#search) code.
* `"list","of","values"` is a list of record values sorted according to the years in `"list","of","years"`

### Where do I get the variable uid? 

This is outside of the scope of this README. The short answer is that all variables are defined in UNFCCC metadata 
available [here](https://confluence.unfccc.int/download/attachments/17137769/meta_data_6.0.3.xml.zip).
If you are a user of UNFCCC CRF Reporter, you may see variable UIDs when you export reporting tables with uids. 
If you are a user of Spherical's [National Inventory System](http://nis.spherical.pm), you will find uids of variables
on cell info boxes on all data entry and reporting views. If you are neither, making sense of variable uids is not easy.
[Ask Spherical](mailto:support@spherical.pm), we will help. 

### Gotchas
_"Life is really simple, but we insist on making it complicated"_ - Confucius

#### Non-numeric year names
Years are not numbered but rather named. This is because Parties are free to name their reporting years the way they 
like, and Hungary used this freedom to name one of their years "1985-1987". In addition to that, there is a year that is
used as baseline for calculating the Party's performance in GHG reduction. This year is named "Base Year". Most of the 
time, you will not be needing these years but you'll need to filter them out on your side.
 
#### Non-ISO country codes

Most country codes are ISO country codes. A UNFCCC-invented three-letter codes are used where an ISO country code 
is not available for a reporting entity. In particular:  

* Sub-countries reporting separately:
  * Belgium: `BRU` is Brussels, `WAL` is Wallonia, `FLA` is Flanders
  * UK: `GBE` is UK excluding overseas territories that are not part of EU
* Countries reporting under the Convention and under the Kyoto Protocol separately:
  * Denmark: `DKE` is for the 1st commitment period of the Kyoto Protocol, `DNM` is for the 2nd
  * France: `FRK` is France's report under the Kyoto Protocol
  * UK: `GBK` is UK's report under the Kyoto Protocol
* Non-countries considered Parties to UNFCCC
  * EU: `EUA` is European Union, `EUC` is European Union's report under the Kyoto Protocol

#### Funny numbers

All numbers in the inventory are floating point numbers, with 
[all floating number fun to be expected](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html). In addition
to that, some data may be a result of complex calculations in national or UN software that are not rounded 
properly to make sense. Do not be surprised to see a country reporting a quarter of a cow and handle it appropriately
in your solutions.   

#### Nulls
According to the rules, complete GHG inventories shall not have empty records or zeroes. At the same time, there is a 
number of situations when a record does not contain a valid numeric value:
* The variable is non-numeric
* The Party could not report a number for some reason (the data point is zero, confidential, included in another 
variable or unavailable)
* The year is not applicable for the Party

In these cases the dataset will include `null` for the record. GHG management software usually treats most of such
records as zeroes. 

## How fresh is the dataset? 

The dataset is based on the latest 2017 GHG inventory submissions.

## Come on, give me some uids to test my charts!

Sure! 
* [F05D8EF0-CD04-4769-81BE-303183271230](http://ghg-data.s3-website.eu-central-1.amazonaws.com/F05D8EF0-CD04-4769-81BE-303183271230.json) - Total direct national emissions in `kt CO2 equivalent`
* [B3C6CE61-81BF-440C-A5EC-3451AB9205B8](http://ghg-data.s3-website.eu-central-1.amazonaws.com/B3C6CE61-81BF-440C-A5EC-3451AB9205B8.json) - Total Methane emissions in `kt`
* [1D3FFBBD-28D5-4AD6-A543-9C6CC01B3F3B](http://ghg-data.s3-website.eu-central-1.amazonaws.com/1D3FFBBD-28D5-4AD6-A543-9C6CC01B3F3B.json) - Emissions from agriculture in `kt CO2 equivalent`
* [A4543811-91B0-4DE7-B239-83F43DF6DF4E](http://ghg-data.s3-website.eu-central-1.amazonaws.com/A4543811-91B0-4DE7-B239-83F43DF6DF4E.json) - Emissions from waste in `kt CO2 equivalent`
* [A5A0958C-BDF7-43CA-BE3C-EB76B9A24348](http://ghg-data.s3-website.eu-central-1.amazonaws.com/A5A0958C-BDF7-43CA-BE3C-EB76B9A24348.json) - Number of sheep in the country :) in `thousands`

A simple [matplotlib](http://matplotlib.org)-based demo in [chart.py](https://github.com/sphericalpm/ghgdata/blob/master/chart.py) shows the great progress of EU countries in 
reducing Methane emissions: 

![Methane Down](https://raw.githubusercontent.com/sphericalpm/ghgdata/master/images/methane_down.png)
 

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
* We also reserve the right to change the API at any moment and without notice. Such changes will be made primarily to 
enrich data offered and therefore have backward compatibility. If you are using the dataset, you are advised to program 
your solutions in a way that they are tolerant to the expansion of the schema and changes to data volume.

 
 