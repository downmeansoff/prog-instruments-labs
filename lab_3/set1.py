var = 73
csv_file = 'C:\\Users\\glebo\\Desktop\\lab1\\prog-instruments-labs\\lab_3\\sariant73.csv'
json_file = 'C:\\Users\\glebo\\Desktop\\lab1\\prog-instruments-labs\\lab_3\\result.json'

regulars = {
    "email": "^[a-z0-9]+(?:[._][a-z0-9]+)*\@[a-z]+(?:\.[a-z]+)+$",
    "http_status_message": "^\\d{3} [A-Za-z ]+$",
    "snils": "^\\d{11}$",
    "passport": "^\d{2}\s\d{2}\s\d{6}$",
    "ip_v4": "^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$",
    "longitude": "^\\-?(180|1[0-7][0-9]|\\d{1,2})\\.\\d+$",
    "hex_color": "^\#[0-9a-fA-F]{6}$",
    "isbn": "^\\d+-\\d+-\\d+-\\d+(?:-\\d+)?$",
    "locale_code": "^[a-z]{2,3}(-[a-z]{2})?$",
    "time": "^(2[0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]\.\d{6}$"
}