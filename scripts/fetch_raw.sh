#!/usr/bin/env bash
# Download every public source the analysis reads into data/raw/ (gitignored).
# SEC EDGAR requires a contact in the User-Agent: set SEC_UA="Name email@example.com".
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/raw/crtc data/raw/netflix data/raw/sources data/raw/statcan
get() { curl -sSL --fail -A "${UA:-Mozilla/5.0}" -o "$1" "$2"; echo "ok  $1"; }
WB="https://web.archive.org/web"
C="https://applications.crtc.gc.ca/OpenData/CASP"
# CRTC open data (Open Government Licence - Canada)
get data/raw/crtc/sfs2016_discretionary_ondemand.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202016/Discretionary/2016%20Discretionary%20and%20On-Demand_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2016_distribution.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202016/BDU/2016%20Distribution_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2016_individual_discretionary.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202016/Individual%20Discretionary/2016%20Individual%20Discretionary%20and%20On-Demand_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2016_conventional.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202016/OTA/2016%20Conventional%20Television_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2020_discretionary_ondemand.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202020/2020%20Broadcasting%20Statistical%20and%20Financial%20Summaries%20-%20Discretionary%20and%20On-demand/English/2020%20Discretionary%20and%20On-Demand%20-%20Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2020_distribution.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202020/2020%20Industry%20Statistical%20and%20Financial%20Summaries/English/2020%20Distribution_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2020_individual_discretionary.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202020/2020%20Broadcasting%20Statistical%20and%20Financial%20Summaries%20-%20Individual%20Discretionary%20and%20On-Demand%20Services/English/2020%20Individual%20Discretionary%20and%20On-Demand_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/sfs2020_conventional.xlsx "$C/Financial%20Broadcasting%20Summaries/Books%202020/2020%20Broadcasting%20Statistical%20and%20Financial%20Summaries%20-%20Conventional%20Television/English/2020%20Conventional%20Television_Statistical%20and%20Financial%20Summaries.xlsx"
get data/raw/crtc/cmr_bdu_sector_2013-2024.xlsx "$C/COMMUNICATION%20MONITORING%20REPORTS/Broadcasting%20Distribution%20Sector/English/data-broadcasting-distribution-sector.xlsx"
# Consumer price index, annual, table 18-10-0005-01 (Statistics Canada Open Licence)
get data/raw/statcan/18100005-eng.zip "https://www150.statcan.gc.ca/n1/tbl/csv/18100005-eng.zip"
# The forecast
get data/raw/sources/nordicity_miller_2015_canadian_television_2020.pdf "https://friends.ca/wp-content/uploads/Canadian-Television-2020-Technological-and-Regulatory-Impacts.pdf"
# CRTC uptake counts (Internet Archive copies; crtc.gc.ca refuses scripted requests)
get data/raw/sources/crtc_2016-04-15_66000.html "$WB/20170720185113id_/https://www.canada.ca/en/radio-television-telecommunications/news/2016/04/more-than-66-000-canadians-have-already-signed-up-to-the-new-basic-tv-package.html"
get data/raw/sources/crtc_2016-09-07_transcript.html "$WB/20180103082457id_/http://www.crtc.gc.ca/eng/transcripts/2016/tb0907.htm"
for f in crtc_2016-04-15_66000 crtc_2016-09-07_transcript; do pandoc -f html -t plain --wrap=none "data/raw/sources/$f.html" -o "data/raw/sources/$f.md"; done
cp data/raw/sources/crtc_2016-04-15_66000.md data/raw/sources/crtc_2016-04-15_66000_basic_tv_package_release.md
cp data/raw/sources/crtc_2016-09-07_transcript.md data/raw/sources/crtc_2016-09-07_hearing_transcript_bdu_renewals.md
# Netflix 10-K filings (technology calibration)
: "${SEC_UA:?set SEC_UA to 'Name email' for SEC EDGAR}"
UA="$SEC_UA" get data/raw/netflix/form10k_q418.htm "https://www.sec.gov/Archives/edgar/data/1065280/000106528019000043/form10k_q418.htm"
UA="$SEC_UA" get data/raw/netflix/q4nflx201710k.htm "https://www.sec.gov/Archives/edgar/data/1065280/000106528018000069/q4nflx201710k.htm"
